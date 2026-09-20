# -*- coding:utf-8 -*-

import datetime


"""
波斯语
"""

_FA_DIGITS = str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789")

_FA_GREGORIAN_MONTHS = {
    "ژانویه": "1月",
    "ژانويه": "1月",
    "فوریه": "2月",
    "مارس": "3月",
    "آوریل": "4月",
    "اپریل": "4月",
    "مه": "5月",
    "می": "5月",
    "ژوئن": "6月",
    "ژوان": "6月",
    "ژوئیه": "7月",
    "جولای": "7月",
    "ژولای": "7月",
    "اوت": "8月",
    "آگوست": "8月",
    "سپتامبر": "9月",
    "اکتبر": "10月",
    "اكتبر": "10月",
    "نوامبر": "11月",
    "دسامبر": "12月",
}

_FA_JALALI_MONTHS = {
    "فروردین": 1,
    "اردیبهشت": 2,
    "خرداد": 3,
    "تیر": 4,
    "مرداد": 5,
    "شهریور": 6,
    "مهر": 7,
    "آبان": 8,
    "آذر": 9,
    "دی": 10,
    "بهمن": 11,
    "اسفند": 12,
}

_FA_JALALI_MONTHS_RE = "|".join(sorted(_FA_JALALI_MONTHS, key=len, reverse=True))
_FA_GREGORIAN_MONTHS_RE = "|".join(sorted(
    _FA_GREGORIAN_MONTHS, key=len, reverse=True))


def _to_ascii(value):
    return value.translate(_FA_DIGITS)


def _is_leap_jalali(year):
    return (25 * year + 11) % 33 < 8


def _jalali_to_gregorian(jy, jm, jd):
    day_of_year = (
        (jm - 1) * 31 + jd if jm <= 6 else 186 + (jm - 7) * 30 + jd)
    ordinal = datetime.date(2022, 3, 21).toordinal()
    if jy > 1401:
        for year in range(1401, jy):
            ordinal += 365 + int(_is_leap_jalali(year))
    else:
        for year in range(jy, 1401):
            ordinal -= 365 + int(_is_leap_jalali(year))
    return datetime.date.fromordinal(ordinal + day_of_year - 1)


def _format_gregorian(value):
    return "%04d-%02d-%02d" % (
        value.year, value.month, value.day)


def _numeric_date(match):
    year = _to_ascii(match.group("Y"))
    month = _to_ascii(match.group("m"))
    day = _to_ascii(match.group("d"))
    if year.isdigit() and 1200 <= int(year) < 1600:
        return _format_gregorian(
            _jalali_to_gregorian(int(year), int(month), int(day)))
    return "%s/%s/%s" % (year, month, day)


def _named_date(match):
    day = _to_ascii(match.group("d"))
    year = _to_ascii(match.group("Y"))
    name = match.group("name")
    if name in _FA_JALALI_MONTHS and year.isdigit() and 1200 <= int(year) < 1600:
        return _format_gregorian(
            _jalali_to_gregorian(int(year), _FA_JALALI_MONTHS[name], int(day)))
    month = _FA_GREGORIAN_MONTHS.get(name) or _FA_JALALI_MONTHS.get(name)
    if isinstance(month, str):
        month = month.rstrip("月")
    return "%s %s月 %s" % (day, month, year)


def _month_year(match):
    name = match.group("name")
    year = _to_ascii(match.group("Y"))
    if name in _FA_JALALI_MONTHS and year.isdigit() and 1200 <= int(year) < 1600:
        return _format_gregorian(
            _jalali_to_gregorian(int(year), _FA_JALALI_MONTHS[name], 1))
    month = _FA_GREGORIAN_MONTHS.get(name) or _FA_JALALI_MONTHS.get(name)
    if isinstance(month, str):
        month = month.rstrip("月")
    return "%s月 %s" % (month, year)


SUB_TRANSLATE = [
    (r"(?<!\d)(?P<Y>[۰-۹]{4})[\-\/\.]\s*(?P<m>[۰-۹]{1,2})[\-\/\.]\s*(?P<d>[۰-۹]{1,2})(?!\d)",
     _numeric_date),
    (r"(?P<d>[۰-۹]{1,2}|\d{1,2})\s*(?P<name>%s)\s*(?P<Y>[۰-۹]{4}|\d{4})"
     % _FA_JALALI_MONTHS_RE, _named_date),
    (r"(?P<d>[۰-۹]{1,2}|\d{1,2})\s*(?P<name>%s)\s*(?P<Y>[۰-۹]{4}|\d{4})"
     % _FA_GREGORIAN_MONTHS_RE, _named_date),
    (r"(?P<name>%s)\s*(?P<Y>[۰-۹]{4})" % _FA_JALALI_MONTHS_RE, _month_year),
    (r"(?P<name>%s)\s*(?P<Y>[۰-۹]{4})" % _FA_GREGORIAN_MONTHS_RE, _month_year),
    (r"پریروز", "前天"),
    (r"پس‌فردا|پسفردا", "后天"),
    (r"دیروز", "昨天"),
    (r"امروز", "今天"),
    (r"فردا", "明天"),
    (r"الان|همین الان|همین حالا", "刚刚"),
    (r"(?:بعد از|بعد)\s+(?P<num>\d+)\s*(?P<unit>ثانیه|ثانیه‌ها|دقیقه|دقیقه‌ها|ساعت|ساعت‌ها|روز|روزها|هفته|هفته‌ها|ماه|ماه‌ها|سال|سال‌ها)",
     lambda m: "%s%s后" % (
         _to_ascii(m.group("num")),
         {"ثانیه": "秒", "ثانیه‌ها": "秒", "دقیقه": "分钟",
          "دقیقه‌ها": "分钟", "ساعت": "小时", "ساعت‌ها": "小时",
          "روز": "天", "روزها": "天", "هفته": "周", "هفته‌ها": "周",
          "ماه": "月", "ماه‌ها": "月", "سال": "年", "سال‌ها": "年"}[
             m.group("unit")])),
    (r"(?P<num>\d+)\s*(?P<unit>ثانیه|ثانیه‌ها|دقیقه|دقیقه‌ها|ساعت|ساعت‌ها|روز|روزها|هفته|هفته‌ها|ماه|ماه‌ها|سال|سال‌ها)\s+دیگر",
     lambda m: "%s%s后" % (
         _to_ascii(m.group("num")),
         {"ثانیه": "秒", "ثانیه‌ها": "秒", "دقیقه": "分钟",
          "دقیقه‌ها": "分钟", "ساعت": "小时", "ساعت‌ها": "小时",
          "روز": "天", "روزها": "天", "هفته": "周", "هفته‌ها": "周",
          "ماه": "月", "ماه‌ها": "月", "سال": "年", "سال‌ها": "年"}[
             m.group("unit")])),
    (r"(?:قبل از|پیش از)\s+(?P<num>\d+)\s*(?P<unit>ثانیه|ثانیه‌ها|دقیقه|دقیقه‌ها|ساعت|ساعت‌ها|روز|روزها|هفته|هفته‌ها|ماه|ماه‌ها|سال|سال‌ها)",
     lambda m: "%s%s前" % (
         _to_ascii(m.group("num")),
         {"ثانیه": "秒", "ثانیه‌ها": "秒", "دقیقه": "分钟",
          "دقیقه‌ها": "分钟", "ساعت": "小时", "ساعت‌ها": "小时",
          "روز": "天", "روزها": "天", "هفته": "周", "هفته‌ها": "周",
          "ماه": "月", "ماه‌ها": "月", "سال": "年", "سال‌ها": "年"}[
             m.group("unit")])),
    (r"(?P<num>\d+)\s*(?P<unit>ثانیه|ثانیه‌ها|دقیقه|دقیقه‌ها|ساعت|ساعت‌ها|روز|روزها|هفته|هفته‌ها|ماه|ماه‌ها|سال|سال‌ها)\s+(?:قبل|پیش)",
     lambda m: "%s%s前" % (
         _to_ascii(m.group("num")),
         {"ثانیه": "秒", "ثانیه‌ها": "秒", "دقیقه": "分钟",
          "دقیقه‌ها": "分钟", "ساعت": "小时", "ساعت‌ها": "小时",
          "روز": "天", "روزها": "天", "هفته": "周", "هفته‌ها": "周",
          "ماه": "月", "ماه‌ها": "月", "سال": "年", "سال‌ها": "年"}[
             m.group("unit")])),
    (r"هفته\s+(?:آینده|بعد)", "下周"),
    (r"هفته\s+(?:گذشته|قبل)", "上周"),
    (r"ماه\s+(?:آینده|بعد)", "下个月"),
    (r"ماه\s+(?:گذشته|قبل)", "上个月"),
    (r"سال\s+(?:آینده|بعد)", "明年"),
    (r"سال\s+(?:گذشته|قبل)", "去年"),
]

for _month in sorted(_FA_GREGORIAN_MONTHS, key=len, reverse=True):
    SUB_TRANSLATE.append((_month, _FA_GREGORIAN_MONTHS[_month]))
for _month in sorted(_FA_JALALI_MONTHS, key=len, reverse=True):
    SUB_TRANSLATE.append((_month, "%s月" % _FA_JALALI_MONTHS[_month]))

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []
