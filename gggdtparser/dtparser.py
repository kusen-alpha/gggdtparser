#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/3/24

import re
import random
import functools
import logging
import calendar
import datetime

try:
    from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
except ImportError:  # pragma: no cover - Python 3.8 without backports.zoneinfo
    try:
        from backports.zoneinfo import (
            ZoneInfo,
            ZoneInfoNotFoundError,
        )
    except ImportError:
        ZoneInfo = None
        ZoneInfoNotFoundError = ValueError

from gggdtparser.utils import s2dt
from . import dtconfigs


_FULLWIDTH_TRANSLATE = {
    chr(code): chr(code - 0xFEE0)
    for code in range(0xFF01, 0xFF5F)
}
_FULLWIDTH_TRANSLATE.update({
    '\u2212': '-',  # minus sign
    '\u2010': '-',  # hyphen
    '\u2011': '-',
    '\u2012': '-',
    '\u2013': '-',  # en dash
    '\u2014': '-',  # em dash
    '\u2015': '-',
    '\u3000': ' ',
})
_FULLWIDTH_TRANSLATE = str.maketrans(_FULLWIDTH_TRANSLATE)

_NO_TRANSLATION_TOKEN_REGEX = re.compile(
    r'(?i)(?<=\d)T(?=\d)|\b(?:am|pm)\b|\b(?:z|utc|gmt)\b')
_OFFSET_TEXT_REGEX = re.compile(
    r'[ \t]*(?P<zone>Z|UTC|GMT|[+-]\d{2}:?\d{2})(?=\s|[^\w]|$)',
    re.I)


def _timezone_from_text(zone_text):
    upper = zone_text.upper()
    if upper in ('Z', 'UTC', 'GMT'):
        return datetime.timezone.utc
    digits = zone_text[1:].replace(':', '')
    if len(digits) != 4:
        raise ValueError('时区偏移格式不正确: %s' % zone_text)
    hours = int(digits[:2])
    minutes = int(digits[2:])
    if hours > 23 or minutes > 59:
        raise ValueError('时区偏移超出范围: %s' % zone_text)
    sign = 1 if zone_text[0] == '+' else -1
    return datetime.timezone(
        sign * datetime.timedelta(hours=hours, minutes=minutes))


def _fraction_to_microseconds(fraction):
    if not fraction:
        return 0
    digits = fraction[:6]
    return int(digits) * 10 ** (6 - len(digits))


def _resolve_timezone(timezone):
    if isinstance(timezone, datetime.tzinfo):
        return timezone
    if isinstance(timezone, str):
        if '/' in timezone:
            if ZoneInfo is None:
                raise ValueError(
                    'IANA 时区解析需要 zoneinfo（Python 3.9+）'
                    '或 backports.zoneinfo 包')
            try:
                return ZoneInfo(timezone)
            except ZoneInfoNotFoundError:
                raise ValueError('未知的 IANA 时区: %s' % timezone)
        return _timezone_from_text(timezone)
    raise ValueError(
        'timezone 参数仅支持 tzinfo、IANA 时区名'
        '或时区偏移字符串，如 Asia/Shanghai、UTC、+08:00')


def _apply_datetime_timezone(dt, timezone):
    if timezone is None or timezone is False:
        return dt
    target = _resolve_timezone(timezone)
    if dt.tzinfo is not None:
        return dt.astimezone(target)
    return dt.replace(tzinfo=target)


def _detect_zone_text(text, span):
    match = _OFFSET_TEXT_REGEX.match(text, span[1])
    if not match:
        return None
    return match.group('zone')


def _apply_text_timezone(dt, text, span, timezone):
    if timezone is None:
        return dt
    zone_text = _detect_zone_text(text, span)
    if timezone is False:
        if zone_text is None:
            return dt
        return dt.replace(tzinfo=_timezone_from_text(zone_text))
    target = _resolve_timezone(timezone)
    if zone_text is not None:
        return dt.replace(
            tzinfo=_timezone_from_text(zone_text)).astimezone(target)
    if dt.tzinfo is not None:
        return dt.astimezone(target)
    return dt.replace(tzinfo=target)


def _check_datetime_bounds(dt, max_datetime, min_datetime):
    """边界校验，naive 与 aware 混用时按 UTC 比较。"""
    if max_datetime is None and min_datetime is None:
        return
    compare_dt = dt
    if dt.tzinfo is None:
        compare_dt = dt.replace(tzinfo=datetime.timezone.utc)
    if max_datetime is not None:
        compare_max = max_datetime
        if compare_max.tzinfo is None:
            compare_max = compare_max.replace(tzinfo=datetime.timezone.utc)
        if compare_dt > compare_max:
            raise Exception('解析时间超出最大时间')
    if min_datetime is not None:
        compare_min = min_datetime
        if compare_min.tzinfo is None:
            compare_min = compare_min.replace(tzinfo=datetime.timezone.utc)
        if compare_dt < compare_min:
            raise Exception('解析时间超出最小时间')


def _needs_language_translation(string_datetime):
    """纯数字/分隔符和 ISO 约定字符不需要多语言翻译。"""
    return bool(re.search(
        r'[^\x00-\x7F]|[A-Za-z]',
        _NO_TRANSLATION_TOKEN_REGEX.sub('', string_datetime)))


@functools.lru_cache(maxsize=4096)
def _translate_cached(string_datetime, langs):
    if not langs and not _needs_language_translation(string_datetime):
        return string_datetime
    if not langs:
        for _lang, sub_list in dtconfigs.get_all_lang_sub_translates():
            for sub in sub_list:
                string_datetime = sub[0].sub(sub[1], string_datetime)
        return string_datetime
    for lang in langs:
        _sub_translate = dtconfigs.get_lang_sub_translate(lang)
        for sub in _sub_translate:
            string_datetime = sub[0].sub(sub[1], string_datetime)
    for sub in dtconfigs.get_lang_sub_translate('default'):
        string_datetime = sub[0].sub(sub[1], string_datetime)
    return string_datetime


class StringDateTimeLanguageHandler(object):

    @classmethod
    def handle(cls, string_datetime, langs):
        """
        根据语言进行一些特殊处理
        :param string_datetime:
        :param langs:
        :return:
        """
        return _translate_cached(string_datetime, tuple(langs or ()))


class StringDateTimeRegexParser(object):
    # 默认时间顺序
    DEFAULT_DATETIME_SEQ = ['year', 'month', 'day', 'hour', 'minute', 'second']

    @classmethod
    def parse(cls, string_datetime, regex_list=None, langs=None,
              result_accurately=True, extract_accurately=False,
              max_datetime=None, min_datetime=None, base_datetime=None,
              timezone=None):
        """
        通过正则对文本的时间进行抽取和解析
        :param string_datetime: 文本时间
        :param regex_list: 正则列表
        :param langs: 语言
        :param result_accurately: 是否遵循严格判断
        :param extract_accurately: 是否只进行精确抽取
        :param max_datetime: 最大时间，超过解析失败
        :param min_datetime: 最小时间，超过解析失败
        :param base_datetime: 相对时间计算的基准时间
        :param timezone: False 保留原文偏移；tzinfo/时区串则转换到目标时区
        :return:
        """
        if timezone is not None and timezone is not False:
            _resolve_timezone(timezone)
        if not isinstance(string_datetime, str):
            return None
        if not string_datetime:
            return
        string_datetime = cls.clear_string_datetime(string_datetime)
        if not langs:
            langs = []
        _langs = []
        for lang in langs:
            lang_lower = lang.lower()
            mapped_lang = dtconfigs.LANG_MAPPING.get(lang_lower)
            if mapped_lang is None and '-' in lang_lower:
                mapped_lang = dtconfigs.LANG_MAPPING.get(
                    lang_lower.split('-', 1)[0])
            if mapped_lang is None:
                if lang_lower in dtconfigs.TRANSLATE_LANGS:
                    logging.warning("语言:%s推荐先进行翻译" % lang)
                else:
                    logging.error("语言:%s设置有误" % lang)
                return
            _langs.append(mapped_lang)
        langs = _langs
        if not regex_list:
            regex_list = []
        if isinstance(regex_list, str):
            regex_list = [regex_list, ]
        string_datetime = StringDateTimeLanguageHandler.handle(
            string_datetime, langs)
        if regex_list:
            compiled_regex_list = []
            for regex in regex_list:
                try:
                    compiled_regex_list.append(re.compile(regex))
                except (re.error, TypeError, ValueError):
                    continue
            regex_list = compiled_regex_list
            result = cls.match_and_parse(
                string_datetime, regex_list, result_accurately,
                max_datetime, min_datetime, base_datetime, timezone)
            if result:
                return result
        regex_list = cls.get_default_regex_list(langs, extract_accurately)
        result = cls.match_and_parse(
            string_datetime, regex_list,
            result_accurately, max_datetime, min_datetime, base_datetime,
            timezone)
        if result:
            return result

    @classmethod
    def clear_string_datetime(cls, string_datetime):
        string_datetime = string_datetime.translate(_FULLWIDTH_TRANSLATE)
        for regex in dtconfigs.STRING_DATETIME_CLEAR_REGEX:
            string_datetime = regex.sub(' ', string_datetime)
        return string_datetime

    @classmethod
    def get_default_regex_list(cls, langs, extract_accurately):
        return cls._get_cached_default_regex_list(
            tuple(langs or ()), bool(extract_accurately))

    @staticmethod
    @functools.lru_cache(maxsize=128)
    def _get_cached_default_regex_list(langs, extract_accurately):
        regex_list = []
        if langs:
            regex_list.extend(
                dtconfigs.LANG_ACCURATE_REGEX_LIST.get('default') or [])
            for lang in langs:
                regex_list.extend(
                    dtconfigs.LANG_ACCURATE_REGEX_LIST.get(lang) or [])
            regex_list.extend(
                dtconfigs.LANG_FUZZY_REGEX_LIST.get('default') or [])
            if not extract_accurately:
                for lang in langs:
                    regex_list.extend(
                        dtconfigs.LANG_FUZZY_REGEX_LIST.get(lang) or [])
            return tuple(regex_list)
        for value in dtconfigs.LANG_ACCURATE_REGEX_LIST.values():
            regex_list.extend(value or [])
        if not extract_accurately:
            for value in dtconfigs.LANG_FUZZY_REGEX_LIST.values():
                regex_list.extend(value or [])
        return tuple(regex_list)

    @classmethod
    def match_and_parse(cls, string_datetime, regex_list,
                        result_accurately, max_datetime,
                        min_datetime, base_datetime, timezone=None):
        valid_results = []
        failed_spans = []
        full_date_failed = False
        full_date_failed_specificity = 0
        for index, regex in enumerate(regex_list):
            try:
                match_obj = regex.search(string_datetime)
            except (ValueError, re.error) as e:
                continue
            if not match_obj:
                continue
            group_dict = match_obj.groupdict()
            if group_dict:
                specificity = cls._group_specificity(group_dict)
                span = match_obj.span()
                if cls._is_blocked_by_failed(span, specificity, failed_spans):
                    continue
                try:
                    result = cls._parse_group_dict(
                        group_dict, result_accurately,
                        max_datetime, min_datetime,
                        base_datetime, timezone)
                except Exception:
                    failed_spans.append((span, specificity))
                    if cls._is_full_date_group(group_dict):
                        full_date_failed = True
                        full_date_failed_specificity = max(
                            full_date_failed_specificity, specificity)
                    continue
                if result is not None:
                    if timezone is not None:
                        result = _apply_text_timezone(
                            result, string_datetime, span, timezone)
                    valid_results.append(
                        (index, specificity, span, group_dict, result))
        if not valid_results:
            return None
        valid_results.sort(
            key=lambda item: cls._candidate_key(item))
        best_item = valid_results[-1]
        if full_date_failed and not cls._is_full_date_group(best_item[3]) \
                and best_item[1] <= full_date_failed_specificity:
            return None
        return best_item[4]

    @classmethod
    def _candidate_key(cls, item):
        index, specificity, span, group_dict, _ = item
        time_fields = sum(
            1 for key in ('H', 'M', 'S')
            if group_dict.get(key) not in (None, ''))
        year_fields = sum(
            1 for key in ('Y', 'mgY')
            if group_dict.get(key) not in (None, ''))
        return (specificity, time_fields, year_fields,
                span[1] - span[0], -index)

    @classmethod
    def _group_specificity(cls, group_dict):
        """统计匹配到的有效字段数量，用于在多个命中中选更精确的结果。"""
        keys = ('Y', 'mgY', 'm', 'd', 'H', 'M', 'S', 'f', 'sd', 'so',
                'sy', 'sm', 'wday', 'wdir',
                'bY', 'bm', 'bd', 'bH', 'bM', 'bS', 'ba',
                'wY', 'wm', 'wd', 'wH', 'wM', 'wS', 'wa',
                'aY', 'am', 'ad', 'aH', 'aM', 'aS', 'aa',
                'apm', 'apm2')
        total = sum(1 for key in keys if group_dict.get(key) not in (None, ''))
        if group_dict.get('ts'):
            total = max(total, 7)
        return total

    @classmethod
    def _is_full_date_group(cls, group_dict):
        if all(group_dict.get(key) not in (None, '') for key in ('Y', 'm', 'd')):
            return True
        return all(group_dict.get(key) not in (None, '')
                   for key in ('mgY', 'm', 'd'))

    @classmethod
    def _is_blocked_by_failed(cls, span, specificity, failed_spans):
        """同区域已有更高精度匹配失败时，跳过更低精度的兼容。"""
        start, end = span
        for failed_span, failed_specificity in failed_spans:
            f_start, f_end = failed_span
            if not (start < f_end and end > f_start):
                continue
            if specificity < failed_specificity:
                return True
            if specificity == failed_specificity and (
                    end - start) < (f_end - f_start):
                return True
        return False

    @classmethod
    def _parse_group_dict(cls, group_dict, result_accurately, max_datetime,
                          min_datetime, base_datetime, timezone=None):
        un_result_accurately = not result_accurately
        now = datetime.datetime.now() if not base_datetime else base_datetime
        timestamp = int(group_dict.get('ts') or 0)
        if timestamp:
            if len(str(timestamp)) == 13:
                timestamp = int(timestamp) // 1000
            if timezone is None or timezone is False:
                parse_datetime = datetime.datetime.fromtimestamp(timestamp)
            else:
                parse_datetime = datetime.datetime.fromtimestamp(
                    timestamp, datetime.timezone.utc)
            _check_datetime_bounds(
                parse_datetime, max_datetime, min_datetime)
            return parse_datetime
        year = group_dict.get('Y')  # or now.year
        if year and isinstance(year, str) and len(year) == 2:
            year = '20' + year
        month = group_dict.get('m')
        day = group_dict.get('d')
        hour = group_dict.get('H')
        minute = group_dict.get('M')
        second = group_dict.get('S')
        month_was_parsed = month not in (None, '')
        day_was_parsed = day not in (None, '')
        # 常见异常组合
        use_now_config = dict()
        use_now_config['year'] = use_now_config['month'] = False
        use_now_config['day'] = use_now_config['hour'] = False
        use_now_config['minute'] = use_now_config['second'] = False
        cls._update_use_now_config_by_has_parse(
            use_now_config, year, month, day, hour, minute, second)
        # 抽取到的具有变化含义的时间
        change_day = 0
        change_hour = 0
        change_minute = 0
        change_second = 0
        year_change = 0
        month_change = 0
        # xxx之前 before
        change_before = dict()
        change_before['bY'] = int(group_dict.get('bY') or 0)
        change_before['bm'] = int(group_dict.get('bm') or 0)
        change_before['bd'] = int(group_dict.get('bd') or 0)
        change_before['bH'] = int(group_dict.get('bH') or 0)
        change_before['bM'] = int(group_dict.get('bM') or 0)
        change_before['bS'] = int(group_dict.get('bS') or 0)
        change_before['ba'] = int(group_dict.get('ba') or 0)
        for key in change_before:
            if change_before[key] <= 0 or result_accurately:
                continue
            change_before[key] += round(random.random(), 2)
        if change_before['bY'] > 0:
            year_change += int(change_before['bY'])
            change_day += (change_before['bY'] - int(change_before['bY'])) * 365
            cls._update_use_now_config(use_now_config, year=True,
                                       month=not result_accurately,
                                       day=not result_accurately)
        if change_before['bm'] > 0:
            month_change += int(change_before['bm'])
            change_day += (change_before['bm'] - int(change_before['bm'])) * 30
            cls._update_use_now_config(use_now_config, year=True,
                                       month=True, day=True)
        if change_before['ba'] > 0:
            change_day += change_before['ba'] * 7
            cls._update_use_now_config(use_now_config, year=True,
                                       month=True, day=True)
        if change_before['bd'] > 0:
            change_day += change_before['bd']
            cls._update_use_now_config(use_now_config, year=True,
                                       month=True, day=True)
        if change_before['bH'] > 0:
            change_hour += change_before['bH']
            cls._update_use_now_config(use_now_config, year=True,
                                       month=True, day=True, hour=True)
        if change_before['bM'] > 0:
            change_minute += change_before['bM']
            cls._update_use_now_config(use_now_config, year=True, month=True,
                                       day=True, hour=True, minute=True)
        if change_before['bS'] > 0:
            change_second += change_before['bS']
            cls._update_use_now_config(
                use_now_config, year=True, month=True,
                day=True, hour=True, minute=True, second=True)
        # 在xxx内 within
        change_within = dict()
        change_within['wY'] = int(group_dict.get('wY') or 0)
        change_within['wm'] = int(group_dict.get('wm') or 0)
        change_within['wd'] = int(group_dict.get('wd') or 0)
        change_within['wH'] = int(group_dict.get('wH') or 0)
        change_within['wM'] = int(group_dict.get('wM') or 0)
        change_within['wS'] = int(group_dict.get('wS') or 0)
        change_within['wa'] = int(group_dict.get('wa') or 0)
        for key in change_within:
            if change_within[key] <= 0 or result_accurately:
                continue
            change_within[key] -= round(random.random(), 1)
        if change_within['wY'] > 0:
            year_change += int(change_within['wY'])
            change_day += (change_within['wY'] - int(change_within['wY'])) * 365
            cls._update_use_now_config(use_now_config, year=True,
                                       month=not result_accurately,
                                       day=not result_accurately)
        if change_within['wm'] > 0:
            month_change += int(change_within['wm'])
            change_day += (change_within['wm'] - int(change_within['wm'])) * 30
            cls._update_use_now_config(use_now_config, year=True,
                                       month=True, day=True)
        if change_within['wa'] > 0:
            change_day += change_within['wa'] * 7
            cls._update_use_now_config(use_now_config, year=True,
                                       month=True, day=True)
        if change_within['wd'] > 0:
            change_day += change_within['wd']
            cls._update_use_now_config(use_now_config, year=True,
                                       month=True, day=True)
        if change_within['wH'] > 0:
            change_hour += change_within['wH']
            cls._update_use_now_config(use_now_config, year=True,
                                       month=True, day=True, hour=True)
        if change_within['wM'] > 0:
            change_minute += change_within['wM']
            cls._update_use_now_config(use_now_config, year=True, month=True,
                                       day=True, hour=True, minute=True)
        if change_within['wS'] > 0:
            change_second += change_within['wS']
            cls._update_use_now_config(
                use_now_config, year=True, month=True,
                day=True, hour=True, minute=True, second=True)

        # 在xxx之后 after
        calc_add = False
        change_after = dict()
        change_after['aY'] = int(group_dict.get('aY') or 0)
        change_after['am'] = int(group_dict.get('am') or 0)
        change_after['ad'] = int(group_dict.get('ad') or 0)
        change_after['aH'] = int(group_dict.get('aH') or 0)
        change_after['aM'] = int(group_dict.get('aM') or 0)
        change_after['aS'] = int(group_dict.get('aS') or 0)
        change_after['aa'] = int(group_dict.get('aa') or 0)
        if any(change_after.values()):
            calc_add = True
        for key in change_after:
            if change_after[key] <= 0 or result_accurately:
                continue
            change_after[key] -= round(random.random(), 1)
        if change_after['aY'] > 0:
            year_change += int(change_after['aY'])
            change_day += (change_after['aY'] - int(change_after['aY'])) * 365
            cls._update_use_now_config(use_now_config, year=True,
                                       month=not result_accurately,
                                       day=not result_accurately)
        if change_after['am'] > 0:
            month_change += int(change_after['am'])
            change_day += (change_after['am'] - int(change_after['am'])) * 30
            cls._update_use_now_config(use_now_config, year=True,
                                       month=True, day=True)
        if change_after['aa'] > 0:
            change_day += change_after['aa'] * 7
            cls._update_use_now_config(use_now_config, year=True,
                                       month=True, day=True)
        if change_after['ad'] > 0:
            change_day += change_after['ad']
            cls._update_use_now_config(use_now_config, year=True,
                                       month=True, day=True)
        if change_after['aH'] > 0:
            change_hour += change_after['aH']
            cls._update_use_now_config(use_now_config, year=True,
                                       month=True, day=True, hour=True)
        if change_after['aM'] > 0:
            change_minute += change_after['aM']
            cls._update_use_now_config(use_now_config, year=True,
                                       month=True,
                                       day=True, hour=True, minute=True)
        if change_after['aS'] > 0:
            change_second += change_after['aS']
            cls._update_use_now_config(
                use_now_config, year=True, month=True,
                day=True, hour=True, minute=True, second=True)

        # 抽取到具有特殊时间 special
        special_year = group_dict.get('sy') or ''
        special_month = group_dict.get('sm') or ''
        special_day = group_dict.get('sd') or ''
        special_other = group_dict.get('so') or ''
        if special_year:
            if special_year == "明年":
                year_change -= 1
            elif special_year == "去年":
                year_change += 1
            cls._update_use_now_config(
                use_now_config, year=True,
                month=not result_accurately, day=not result_accurately)
        if special_month:
            if special_month in ("下个月", "下月"):
                month_change -= 1
            elif special_month in ("上个月", "上月"):
                month_change += 1
            cls._update_use_now_config(
                use_now_config, year=True, month=True, day=True)
        if special_day:
            if special_day == "今天":
                change_day += 0
                cls._update_use_now_config(
                    use_now_config, year=True, month=True, day=True,
                    hour=un_result_accurately, minute=un_result_accurately,
                    second=un_result_accurately)
            elif special_day == "昨天":
                change_day += 1
                cls._update_use_now_config(
                    use_now_config, year=True, month=True, day=True,
                    hour=un_result_accurately, minute=un_result_accurately,
                    second=un_result_accurately)
            elif special_day == "前天":
                change_day += 2
                cls._update_use_now_config(
                    use_now_config, year=True, month=True, day=True,
                    hour=un_result_accurately, minute=un_result_accurately,
                    second=un_result_accurately)
            elif special_day == "明天":
                change_day += -1
                cls._update_use_now_config(
                    use_now_config, year=True, month=True, day=True,
                    hour=un_result_accurately, minute=un_result_accurately,
                    second=un_result_accurately)
            elif special_day == "后天":
                change_day += -2
                cls._update_use_now_config(
                    use_now_config, year=True, month=True, day=True,
                    hour=un_result_accurately, minute=un_result_accurately,
                    second=un_result_accurately)
            elif special_day in ("下周", "下星期"):
                change_day += -7
                cls._update_use_now_config(
                    use_now_config, year=True, month=True, day=True,
                    hour=un_result_accurately, minute=un_result_accurately,
                    second=un_result_accurately)
            elif special_day in ("上周", "上星期"):
                change_day += 7
                cls._update_use_now_config(
                    use_now_config, year=True, month=True, day=True,
                    hour=un_result_accurately, minute=un_result_accurately,
                    second=un_result_accurately)
        weekday = group_dict.get('wday') or ''
        weekday_dir = group_dict.get('wdir') or ''
        if weekday:
            weekday_map = {
                '一': 1, '二': 2, '三': 3, '四': 4,
                '五': 5, '六': 6, '日': 7, '天': 7,
                '1': 1, '2': 2, '3': 3, '4': 4,
                '5': 5, '6': 6, '7': 7,
            }
            target_weekday = weekday_map.get(weekday)
            if target_weekday:
                base_weekday = now.weekday() + 1
                if weekday_dir in ("下下", "下下个"):
                    shift = 14 - base_weekday + target_weekday
                elif weekday_dir in ("上上", "上上个"):
                    shift = -(
                        14 + ((base_weekday - target_weekday) % 7 or 7))
                elif weekday_dir in ("下", "下个"):
                    shift = 7 - base_weekday + target_weekday
                elif weekday_dir in ("上", "上个"):
                    shift = -((base_weekday - target_weekday) % 7 or 7)
                    if target_weekday < base_weekday:
                        shift -= 7
                else:
                    shift = target_weekday - base_weekday
                change_day += -shift
                cls._update_use_now_config(
                    use_now_config, year=True, month=True, day=True,
                    hour=un_result_accurately, minute=un_result_accurately,
                    second=un_result_accurately)
        if special_other:
            if special_other == '刚刚':
                change_second += 5
                cls._update_use_now_config(
                    use_now_config, year=True, month=True,
                    day=True, hour=True, minute=True, second=True)
        # 民国时间
        mg_year = group_dict.get('mgY')
        if mg_year:
            year = 1911 + int(mg_year)
            month = month if month else 1
        # 计算时间
        year = cls._get_default_or_now(
            result_accurately, use_now_config['year'], now.year, year)
        month = cls._get_default_or_now(
            result_accurately, use_now_config['month'], now.month, month)
        day = cls._get_default_or_now(
            result_accurately, use_now_config['day'], now.day, day)
        hour = cls._get_default_or_now(
            result_accurately, use_now_config['hour'], now.hour, hour)
        minute = cls._get_default_or_now(
            result_accurately, use_now_config['minute'], now.minute, minute)
        second = cls._get_default_or_now(
            result_accurately, use_now_config['second'], now.second, second)
        if month_was_parsed and not month:
            raise ValueError('month must be in 1..12')
        if day_was_parsed and not day:
            raise ValueError('day must be in 1..31')
        month = 1 if not month else month
        day = 1 if not day else day
        # 上下午
        apm = group_dict.get('apm') or group_dict.get('apm2')
        if apm == 'pm' and hour and hour < 12:
            hour += 12
        elif apm == 'am' and hour == 12:
            hour = 0
        parse_datetime = datetime.datetime(
            year=year, month=month,
            day=day, hour=hour,
            minute=minute, second=second,
            microsecond=_fraction_to_microseconds(group_dict.get('f')))
        parse_datetime = cls._shift_years(
            parse_datetime, year_change if calc_add else -year_change)
        parse_datetime = cls._shift_months(
            parse_datetime, month_change if calc_add else -month_change)
        change_timedelta = datetime.timedelta(
            days=change_day, hours=change_hour,
            minutes=change_minute, seconds=change_second)
        if calc_add:
            parse_datetime = parse_datetime + change_timedelta
        else:
            parse_datetime = parse_datetime - change_timedelta
        _check_datetime_bounds(
            parse_datetime, max_datetime, min_datetime)
        return parse_datetime

    @classmethod
    def _update_use_now_config(cls, use_now_config, year=False, month=False,
                               day=False, hour=False, minute=False,
                               second=False):
        use_now_config['year'] = year
        use_now_config['month'] = month
        use_now_config['day'] = day
        use_now_config['hour'] = hour
        use_now_config['minute'] = minute
        use_now_config['second'] = second

    @classmethod
    def _get_default_or_now(cls, result_accurately, use_now_enabled,
                            now_value, default_value):
        if default_value is None:
            if use_now_enabled or not result_accurately:
                return int(now_value)
            return 0
        return int(default_value)

    @classmethod
    def _shift_years(cls, dt, delta):
        if not delta:
            return dt
        target_year = dt.year + delta
        try:
            return dt.replace(year=target_year)
        except ValueError:
            return dt.replace(year=target_year, day=28)

    @classmethod
    def _shift_months(cls, dt, delta):
        if not delta:
            return dt
        total = dt.year * 12 + (dt.month - 1) + delta
        target_year, month_index = divmod(total, 12)
        target_month = month_index + 1
        try:
            return dt.replace(year=target_year, month=target_month)
        except ValueError:
            last_day = calendar.monthrange(target_year, target_month)[1]
            return dt.replace(year=target_year, month=target_month, day=last_day)

    @classmethod
    def _update_use_now_config_by_has_parse(
            cls, use_now_config, year, month, day, hour, minute, second):
        parse_flag = '%s%s%s%s%s%s' % (
            int(bool(year)), int(bool(month)), int(bool(day)),
            int(bool(hour)), int(bool(minute)), int(bool(second))
        )
        for index, flag in enumerate(parse_flag):
            if flag == '1':
                break
            use_now_config[cls.DEFAULT_DATETIME_SEQ[index]] = True


parse_by_regex = StringDateTimeRegexParser.parse


def parse_by_format(string_datetime, format_list=None, timezone=None):
    """
    通过format进行时间解析
    :param string_datetime:
    :param format_list:
    :return:
    """
    if not isinstance(string_datetime, str):
        return None
    if not format_list:
        format_list = []
    if isinstance(format_list, str):
        format_list = [format_list]
    result = s2dt(string_datetime, format_list)
    if result is None or timezone is None:
        return result
    return _apply_datetime_timezone(result, timezone)


def parse(string_datetime, format_list=None, regex_list=None,
          langs=None, result_accurately=True, extract_accurately=False,
          max_datetime=None, min_datetime=None, base_datetime=None,
          translate_func=None, timezone=None):
    """
    解析文本时间
    :param string_datetime: 字符串时间文本
    :param format_list: 时间解析模板列表，如%Y-%m-%d
    :param regex_list: 正则解析规则列表，统一为有名分组格式，参考dtconfigs.py
    :param langs: 语言列表，优先设置的语言进行翻译替换和解析
    :param result_accurately: 解析結果是否为严格模式,format不支持非严格模式
    :param extract_accurately:  是否只进行精确抽取
    :param max_datetime: 最大时间
    :param min_datetime: 最小时间
    :param base_datetime: 基准时间
    :param translate_func: 翻译函数
    :param timezone: False 保留原文偏移；tzinfo/时区串则转换到目标时区
    :return: datetime.datetime
    """
    # format
    # regex
    # fanyi
    if not isinstance(string_datetime, str):
        return None
    if translate_func and callable(translate_func):
        string_datetime = translate_func(string_datetime)
    result = parse_by_format(string_datetime, format_list, timezone=timezone)
    if result:
        try:
            _check_datetime_bounds(result, max_datetime, min_datetime)
        except Exception:
            return None
        return result
    result = parse_by_regex(
        string_datetime, regex_list, langs, result_accurately,
        max_datetime=max_datetime, min_datetime=min_datetime,
        base_datetime=base_datetime,
        extract_accurately=extract_accurately, timezone=timezone)
    if result:
        return result


def check(dst_dt, check_dt):
    """
    检测解析结果
    :param dst_dt: 解析结果datetime.datetime
    :param check_dt: 验证结果datetime.datetime或两datetime.datetime元组
    :return: bool
    """
    if isinstance(check_dt, datetime.datetime):
        return dst_dt == check_dt
    start_dt, end_dt = check_dt
    return start_dt <= dst_dt <= end_dt


if __name__ == '__main__':
    result1 = parse('2022年', format_list=['%Y年'])
    print(result1)
