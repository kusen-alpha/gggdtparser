# -*- coding:utf-8 -*-

"""
宿务语（Cebuano）
"""

ACCURATE_REGEX_LIST = [
    r"(?P<m>\d{1,2})\s*[月]\s*(?P<Y>\d{4})",
]
FUZZY_REGEX_LIST = []

_CEB_UNITS = {
    "segundo": "秒", "minuto": "分钟", "oras": "小时",
    "adlaw": "天", "semana": "周", "bulan": "月", "tuig": "年",
}
_CEB_UNIT_RE = "|".join(sorted(_CEB_UNITS, key=len, reverse=True))

_CEB_MONTHS = {
    "enero": "1月", "pebrero": "2月", "marso": "3月",
    "abril": "4月", "mayo": "5月", "hunyo": "6月",
    "hulyo": "7月", "agosto": "8月", "septiyembre": "9月",
    "oktubre": "10月", "nobiyembre": "11月", "disiyembre": "12月",
}
_CEB_MONTHS_RE = "|".join(sorted(_CEB_MONTHS, key=len, reverse=True))

_CEB_WEEKDAYS = {
    "lunes": "周一",
    "martes": "周二",
    "miyerkules": "周三",
    "huwebes": "周四",
    "biyernes": "周五",
    "sabado": "周六",
    "domingo": "周日",
}
_CEB_WEEKDAYS_RE = "|".join(sorted(_CEB_WEEKDAYS, key=len, reverse=True))


def _ceb_month_no(name):
    return _CEB_MONTHS[name.lower()]


def _ceb_named_date(match):
    return "%s %s %s" % (
        match.group("d"), _ceb_month_no(match.group("name")), match.group("Y"))


def _ceb_month_first(match):
    return "%s %s, %s" % (
        _ceb_month_no(match.group("name")), match.group("d"), match.group("Y"))


def _ceb_month_year(match):
    return "%s %s" % (_ceb_month_no(match.group("name")), match.group("Y"))


def _ceb_later(match):
    return "%s%s后" % (
        match.group("num"), _CEB_UNITS[match.group("unit").lower()])


def _ceb_ago(match):
    return "%s%s前" % (
        match.group("num"), _CEB_UNITS[match.group("unit").lower()])


SUB_TRANSLATE = [
    (r"(?i)\b(%s)\s+nga\s+sunod\b" % _CEB_WEEKDAYS_RE,
     lambda m: "下%s" % _CEB_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\bmiaging\s+(%s)\b" % _CEB_WEEKDAYS_RE,
     lambda m: "上%s" % _CEB_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\bkarong\s+(%s)\b" % _CEB_WEEKDAYS_RE,
     lambda m: "这%s" % _CEB_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\bkaron\s+sa\s+buntag\b", "今天 08:00 am"),
    (r"(?i)\bkaron\s+sa\s+udto\b", "今天 12:00 pm"),
    (r"(?i)\bkaron\s+sa\s+hapon\b", "今天 15:00 pm"),
    (r"(?i)\bkaron\s+sa\s+gabii\b", "今天 20:00 pm"),
    (r"(?i)\bkaron\s+sa\s+kagabhion\b", "今天 22:00 pm"),
    (r"(?i)\bugma\s+sa\s+buntag\b", "明天 08:00 am"),
    (r"(?i)\bgahapon\s+sa\s+gabii\b", "昨天 22:00 pm"),
    (r"(?i)\btungang\s+gabii\b", "12:00 am"),
    (r"(?i)(?P<d>\d{1,2})\s*(?:ika-?\d*\s+sa\s+|ng\s+)?(?P<name>%s)\s+(?P<Y>\d{4})"
     % _CEB_MONTHS_RE, _ceb_named_date),
    (r"(?i)(?P<name>%s)\s+(?P<d>\d{1,2}),\s+(?P<Y>\d{4})"
     % _CEB_MONTHS_RE, _ceb_month_first),
    (r"(?i)(?P<name>%s)\s+(?P<Y>\d{4})" % _CEB_MONTHS_RE, _ceb_month_year),
    (r"(?i)\bang\s+adlaw\s+sa\s+wala\s+pa\s+gahapon\b", "前天"),
    (r"(?i)\bang\s+adlaw\s+pagkahuman\s+sa\s+ugma\b", "后天"),
    (r"(?i)\bkaron\b", "今天"),
    (r"(?i)\bgahapon\b", "昨天"),
    (r"(?i)\bugma\b", "明天"),
    (r"(?i)\bbag-o\s+lang\b", "刚刚"),
    (r"(?i)\bhuman\s+sa\s+(?P<num>\d+)\s+ka\s+(?P<unit>%s)"
     % _CEB_UNIT_RE, _ceb_later),
    (r"(?i)(?P<num>\d+)\s+ka\s+(?P<unit>%s)\s+ang\s+milabay"
     % _CEB_UNIT_RE, _ceb_ago),
    (r"(?i)\bsunod\s+nga\s+semana\b", "下周"),
    (r"(?i)\bmiaging\s+semana\b", "上周"),
    (r"(?i)\bsunod\s+nga\s+bulan\b", "下个月"),
    (r"(?i)\bmiaging\s+bulan\b", "上个月"),
    (r"(?i)\bsunod\s+nga\s+tuig\b", "明年"),
    (r"(?i)\bmiaging\s+tuig\b", "去年"),
]

for _month in sorted(_CEB_MONTHS, key=len, reverse=True):
    SUB_TRANSLATE.append((r"(?i)\b%s\.?\b" % _month, _CEB_MONTHS[_month]))

for _weekday in sorted(_CEB_WEEKDAYS, key=len, reverse=True):
    SUB_TRANSLATE.append((r"(?i)\b%s\b" % _weekday, _CEB_WEEKDAYS[_weekday]))
