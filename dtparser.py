#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/3/24

import re
import random
import datetime
import dtconfigs


class StringDateTimeLanguageHandler(object):
    @classmethod
    def handle(cls, s, langs):
        """
        根据语言进行一些特殊处理
        :param s:
        :param langs:
        :return:
        """
        if not langs:
            langs = []
        if not langs:
            for di in dir(dtconfigs):
                if not re.search(r'.+2.+', di):
                    continue
                for conf in getattr(dtconfigs, di):
                    s = re.sub(conf[0], conf[1], s)
        for lang in langs:
            to_arab = '%s2ARAB' % lang.upper()
            to_zh_cn = '%s2ZH_CN' % lang.upper()
            if hasattr(dtconfigs, to_arab):
                for conf in getattr(dtconfigs, to_arab):
                    s = re.sub(conf[0], conf[1], s)
            if hasattr(dtconfigs, to_zh_cn):
                for conf in getattr(dtconfigs, to_zh_cn):
                    s = re.sub(conf[0], conf[1], s)
        return s


class StringDateTimeRegexParser(object):

    @classmethod
    def parse(cls, s, regex_list=None, langs=None, accurately=True):
        """
        通过正则对文本的时间进行抽取和解析
        :param s: 文本时间
        :param regex_list: 正则列表
        :param langs: 语言
        :param accurately: 是否遵循严格判断
        :return:
        """
        if not regex_list:
            regex_list = []
        if isinstance(regex_list, str):
            regex_list = [regex_list, ]
        s = StringDateTimeLanguageHandler.handle(s, langs)
        if regex_list:
            result = cls.match_and_parse(s, regex_list, accurately)
            if result:
                return
        if langs:
            for lang in langs:
                lang_regex_list = '%s_STRING_DATE_TIME_REGEX_LIST' % lang.upper()
                if hasattr(dtconfigs, lang_regex_list):
                    result = cls.match_and_parse(
                        s, getattr(dtconfigs, lang_regex_list),
                        accurately)
                    if result:
                        return result
        result = cls.match_and_parse(
            s, dtconfigs.STRING_DATE_TIME_REGEX_LIST, accurately)
        if result:
            return result
        for di in dir(dtconfigs):
            if re.search(r'.+_STRING_DATE_TIME_REGEX_LIST', di):
                result = cls.match_and_parse(
                    s, getattr(dtconfigs, di), accurately)
                if result:
                    return result
        return cls.match_and_parse(
            s, dtconfigs.STRING_DATE_TIME_REGEX_LIST_FUZZY,
            accurately)

    @classmethod
    def match_and_parse(cls, s, regex_list, accurately):
        for regex in regex_list:
            match_obj = None
            try:
                match_obj = re.search(regex, s, flags=re.M | re.I | re.S)
            except (ValueError, re.error) as e:
                # print(regex, s, e)
                continue
            if not match_obj:
                continue
            group_dict = match_obj.groupdict()
            if group_dict:
                try:
                    result = cls._parse_group_dict(group_dict, accurately)
                    # print(regex)
                    return result
                except ValueError as e:
                    continue

    @classmethod
    def _parse_group_dict(cls, group_dict, accurately):
        un_accurately = not accurately
        now = datetime.datetime.now()
        timestamp = int(group_dict.get('ts') or 0)
        if timestamp:
            if len(str(timestamp)) == 13:
                timestamp = int(timestamp) // 1000
            return datetime.datetime.fromtimestamp(timestamp)
        year = group_dict.get('Y') or now.year
        if isinstance(year, str) and len(year) == 2:
            year = '20' + year
        year = int(year)
        if year < 1970:
            raise ValueError
        month = int(group_dict.get('m') or 0)
        day = int(group_dict.get('d') or 0)
        hour = int(group_dict.get('H') or 0)
        minute = int(group_dict.get('M') or 0)
        second = int(group_dict.get('S') or 0)
        # 常见异常组合
        use_now_config = dict()
        use_now_config['year'] = use_now_config['month'] = False
        use_now_config['day'] = use_now_config['hour'] = False
        use_now_config['minute'] = use_now_config['second'] = False
        # 抽取到的具有变化含义的时间
        change_day = 0
        change_hour = 0
        change_minute = 0
        change_second = 0
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
            if change_before[key] <= 0 or accurately:
                continue
            change_before[key] += round(random.random(), 1)
        if change_before['bY'] > 0:
            change_day += change_before['bY'] * 365
            month = month if month else 1
            cls._update_use_now_config(use_now_config, year=True)
        if change_before['bm'] > 0:
            change_day += change_before['bm'] * 30
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
            if change_within[key] <= 0 or accurately:
                continue
            change_within[key] -= round(random.random(), 1)
        if change_within['wY'] > 0:
            change_day += change_within['wY'] * 365
            month = month if month else 1
            cls._update_use_now_config(use_now_config, year=True)
        if change_within['wm'] > 0:
            change_day += change_within['wm'] * 30
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
        # 抽取到具有特殊时间 special
        special_day = group_dict.get('sd') or ''
        special_other = group_dict.get('so') or ''
        if special_day:
            if special_day == "今天":
                change_day += 0
                cls._update_use_now_config(
                    use_now_config, year=True, month=True, day=True,
                    hour=un_accurately, minute=un_accurately,
                    second=un_accurately)
            elif special_day == "昨天":
                change_day += 1
                cls._update_use_now_config(
                    use_now_config, year=True, month=True, day=True,
                    hour=un_accurately, minute=un_accurately,
                    second=un_accurately)
            elif special_day == "前天":
                change_day += 2
                cls._update_use_now_config(
                    use_now_config, year=True, month=True, day=True,
                    hour=un_accurately, minute=un_accurately,
                    second=un_accurately)
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
        change_date_time = datetime.timedelta(
            days=change_day, hours=change_hour,
            minutes=change_minute, seconds=change_second)
        year = cls._get_default_or_now(
            accurately, use_now_config['year'], now.year, year)
        month = cls._get_default_or_now(
            accurately, use_now_config['month'], now.month, month)
        day = cls._get_default_or_now(
            accurately, use_now_config['day'], now.day, day)
        hour = cls._get_default_or_now(
            accurately, use_now_config['hour'], now.hour, hour)
        minute = cls._get_default_or_now(
            accurately, use_now_config['minute'], now.minute, minute)
        second = cls._get_default_or_now(
            accurately, use_now_config['second'], now.second, second)
        month = 1 if not month else month
        day = 1 if not day else day
        parse_date_time = now.replace(
            year=year, month=month, day=day, hour=hour,
            minute=minute, second=second, microsecond=0)
        return parse_date_time - change_date_time

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
    def _get_default_or_now(cls, accurately, use_now_enabled,
                            now_value, default_value):
        return now_value if not default_value and (
                use_now_enabled or not accurately) else default_value


parse_string_datetime_by_regex = StringDateTimeRegexParser.parse


def parse_string_datetime_by_format(s, fs=None):
    """
    通过format进行时间解析
    :param s:
    :param fs:
    :return:
    """
    if not fs:
        fs = []
    for f in fs:
        try:
            return datetime.datetime.strptime(s, f)
        except ValueError:
            continue
    for f in dtconfigs.DATE_TIME_FORMATS:
        try:
            return datetime.datetime.strptime(s, f)
        except ValueError:
            continue


def parse_string_datetime(s, format_list=None, regex_list=None,
                          langs=None, accurately=True):
    """
    解析文本时间
    :param s: 字符串时间文本
    :param format_list: 时间解析模板列表，如%Y-%m-%d
    :param regex_list: 正则解析规则列表，统一为有名分组格式，参考dtconfigs.py
    :param langs: 语言列表，优先设置的语言进行翻译替换和解析
    :param accurately: 是否为严格模式
    :return: datetime.datetime
    """
    # format
    # regex
    # fanyi
    result = parse_string_datetime_by_format(s, format_list)
    if result:
        return result
    result = parse_string_datetime_by_regex(s, regex_list, langs, accurately)
    if result:
        return result


parse = parse_string_datetime
