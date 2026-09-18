#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/3/24

import re
import random
import logging
import calendar
import datetime

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


class StringDateTimeLanguageHandler(object):

    @classmethod
    def handle(cls, string_datetime, langs):
        """
        根据语言进行一些特殊处理
        :param string_datetime:
        :param langs:
        :return:
        """
        if not langs:
            langs = []
        if not langs:
            for _lang, sub_list in dtconfigs.LANG_SUB_TRANSLATE.items():
                for sub in sub_list:
                    repl = sub[1] if callable(sub[1]) else sub[1]
                    string_datetime = sub[0].sub(repl, string_datetime)
        for lang in langs:
            _sub_translate = dtconfigs.LANG_SUB_TRANSLATE.get(
                lang) or []
            for sub in _sub_translate:
                repl = sub[1] if callable(sub[1]) else sub[1]
                string_datetime = sub[0].sub(repl, string_datetime)
        if langs:
            for sub in dtconfigs.LANG_SUB_TRANSLATE.get('default') or []:
                repl = sub[1] if callable(sub[1]) else sub[1]
                string_datetime = sub[0].sub(repl, string_datetime)
        return string_datetime


class StringDateTimeRegexParser(object):
    # 默认时间顺序
    DEFAULT_DATETIME_SEQ = ['year', 'month', 'day', 'hour', 'minute', 'second']

    @classmethod
    def parse(cls, string_datetime, regex_list=None, langs=None,
              result_accurately=True, extract_accurately=False,
              max_datetime=None, min_datetime=None, base_datetime=None):
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
        :return:
        """
        if not isinstance(string_datetime, str):
            return None
        if not string_datetime:
            return
        string_datetime = cls.clear_string_datetime(string_datetime)
        if not langs:
            langs = []
        _langs = []
        for lang in langs:
            try:
                _langs.append(dtconfigs.LANG_MAPPING[lang.lower()])
            except KeyError:
                if lang.lower() in dtconfigs.TRANSLATE_LANGS:
                    logging.warning("语言:%s推荐先进行翻译" % lang)
                else:
                    logging.error("语言:%s设置有误" % lang)
                return
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
                max_datetime, min_datetime, base_datetime)
            if result:
                return result
        regex_list = cls.get_default_regex_list(langs, extract_accurately)
        result = cls.match_and_parse(
            string_datetime, regex_list,
            result_accurately, max_datetime, min_datetime, base_datetime)
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
        regex_list = []
        if langs:
            regex_list.extend(
                dtconfigs.LANG_ACCURATE_REGEX_LIST.get('default') or [])
            for lang in langs:
                regex_list.extend(cls._get_default_regex_list(lang, True))
            regex_list.extend(
                dtconfigs.LANG_FUZZY_REGEX_LIST.get('default') or [])
            if not extract_accurately:
                for lang in langs:
                    regex_list.extend(cls._get_default_regex_list(lang, False))
            return regex_list
        for value in dtconfigs.LANG_ACCURATE_REGEX_LIST.values():
            regex_list.extend(value or [])
        if not extract_accurately:
            for value in dtconfigs.LANG_FUZZY_REGEX_LIST.values():
                regex_list.extend(value or [])
        return regex_list

    @classmethod
    def _get_default_regex_list(cls, lang, extract_accurately):
        if extract_accurately:
            return dtconfigs.LANG_ACCURATE_REGEX_LIST.get(lang) or []
        return dtconfigs.LANG_FUZZY_REGEX_LIST.get(lang) or []

    @classmethod
    def match_and_parse(cls, string_datetime, regex_list,
                        result_accurately, max_datetime,
                        min_datetime, base_datetime):
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
                        base_datetime)
                except Exception:
                    failed_spans.append((span, specificity))
                    if cls._is_full_date_group(group_dict):
                        full_date_failed = True
                        full_date_failed_specificity = max(
                            full_date_failed_specificity, specificity)
                    continue
                if result is not None:
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
        keys = ('Y', 'mgY', 'm', 'd', 'H', 'M', 'S', 'sd', 'so',
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
                          min_datetime, base_datetime):
        un_result_accurately = not result_accurately
        now = datetime.datetime.now() if not base_datetime else base_datetime
        timestamp = int(group_dict.get('ts') or 0)
        if timestamp:
            if len(str(timestamp)) == 13:
                timestamp = int(timestamp) // 1000
            parse_datetime = datetime.datetime.fromtimestamp(timestamp)
            if max_datetime and parse_datetime > max_datetime:
                raise Exception('解析时间超出最大时间')
            if min_datetime and parse_datetime < min_datetime:
                raise Exception('解析时间超出最小时间')
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
        special_day = group_dict.get('sd') or ''
        special_other = group_dict.get('so') or ''
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
            minute=minute, second=second)
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
        if max_datetime and parse_datetime > max_datetime:
            raise Exception('解析时间超出最大时间')
        if min_datetime and parse_datetime < min_datetime:
            raise Exception('解析时间超出最小时间')
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


def parse_by_format(string_datetime, format_list=None):
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
    return s2dt(string_datetime, format_list)


def parse(string_datetime, format_list=None, regex_list=None,
          langs=None, result_accurately=True, extract_accurately=False,
          max_datetime=None, min_datetime=None, base_datetime=None,
          translate_func=None):
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
    :return: datetime.datetime
    """
    # format
    # regex
    # fanyi
    if not isinstance(string_datetime, str):
        return None
    if translate_func and callable(translate_func):
        string_datetime = translate_func(string_datetime)
    result = parse_by_format(string_datetime, format_list)
    if result:
        if max_datetime and result > max_datetime:
            return None
        if min_datetime and result < min_datetime:
            return None
        return result
    result = parse_by_regex(
        string_datetime, regex_list, langs, result_accurately,
        max_datetime=max_datetime, min_datetime=min_datetime,
        base_datetime=base_datetime,
        extract_accurately=extract_accurately)
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
    result1 = parse('2022年', fs=['%Y年'])
    print(result1)
