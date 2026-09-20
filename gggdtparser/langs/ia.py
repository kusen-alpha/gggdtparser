# -*- coding:utf-8 -*-

"""
国际语（Interlingua）
"""

ACCURATE_REGEX_LIST = [
    r"(?P<m>\d{1,2})\s*[月]\s*(?P<Y>\d{4})",
]
FUZZY_REGEX_LIST = []

_IA_UNITS = {
    "secunda": "秒", "minuta": "分钟", "hora": "小时",
    "die": "天", "septimana": "周", "mense": "月", "anno": "年",
}
_IA_UNITS.update({
    "secundas": "秒", "minutas": "分钟", "horas": "小时",
    "dies": "天", "septimanas": "周", "menses": "月", "annos": "年",
})
_IA_UNIT_RE = "|".join(sorted(_IA_UNITS, key=len, reverse=True))

_IA_MONTHS = {
    "januario": "1月", "februario": "2月", "martio": "3月",
    "april": "4月", "maio": "5月", "junio": "6月",
    "julio": "7月", "augusto": "8月", "septembre": "9月",
    "octobre": "10月", "novembre": "11月", "decembre": "12月",
}
_IA_MONTHS_RE = "|".join(sorted(_IA_MONTHS, key=len, reverse=True))

_IA_WEEKDAYS = {
    "lunedi": "周一",
    "martedi": "周二",
    "mercuridi": "周三",
    "jovedi": "周四",
    "venerdi": "周五",
    "sabbato": "周六",
    "dominica": "周日",
}
_IA_WEEKDAYS_RE = "|".join(sorted(_IA_WEEKDAYS, key=len, reverse=True))


def _ia_month_no(name):
    return _IA_MONTHS[name.lower()]


def _ia_named_date(match):
    return "%s %s %s" % (
        match.group("d"), _ia_month_no(match.group("name")), match.group("Y"))


def _ia_month_first(match):
    return "%s %s, %s" % (
        _ia_month_no(match.group("name")), match.group("d"), match.group("Y"))


def _ia_month_year(match):
    return "%s %s" % (_ia_month_no(match.group("name")), match.group("Y"))


def _ia_later(match):
    return "%s%s后" % (
        match.group("num"), _IA_UNITS[match.group("unit").lower()])


def _ia_ago(match):
    return "%s%s前" % (
        match.group("num"), _IA_UNITS[match.group("unit").lower()])


SUB_TRANSLATE = [
    (r"(?i)\bproxime\s+(%s)\b" % _IA_WEEKDAYS_RE,
     lambda m: "下%s" % _IA_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\bpassate\s+(%s)\b" % _IA_WEEKDAYS_RE,
     lambda m: "上%s" % _IA_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\biste\s+(%s)\b" % _IA_WEEKDAYS_RE,
     lambda m: "这%s" % _IA_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\bhodie\s+matino\b", "今天 08:00 am"),
    (r"(?i)\bhodie\s+meridie\b", "今天 12:00 pm"),
    (r"(?i)\bhodie\s+postmeridie\b", "今天 15:00 pm"),
    (r"(?i)\bhodie\s+vespere\b", "今天 20:00 pm"),
    (r"(?i)\bhodie\s+nocte\b", "今天 22:00 pm"),
    (r"(?i)\bdeman\s+matino\b", "明天 08:00 am"),
    (r"(?i)\bheri\s+vespere\b", "昨天 20:00 pm"),
    (r"(?i)\bmedianocte\b", "12:00 am"),
    (r"(?i)(?P<d>\d{1,2})\s*(?:de\s+)?(?P<name>%s)\s+(?P<Y>\d{4})"
     % _IA_MONTHS_RE, _ia_named_date),
    (r"(?i)(?P<name>%s)\s+(?P<d>\d{1,2}),\s+(?P<Y>\d{4})"
     % _IA_MONTHS_RE, _ia_month_first),
    (r"(?i)(?P<name>%s)\s+(?P<Y>\d{4})" % _IA_MONTHS_RE, _ia_month_year),
    (r"(?i)\bheri\s+ante\b", "前天"),
    (r"(?i)\bpost\s+deman\b", "后天"),
    (r"(?i)\bhodie\b", "今天"),
    (r"(?i)\bheri\b", "昨天"),
    (r"(?i)\bdeman\b", "明天"),
    (r"(?i)\bjusto\s+nunc\b", "刚刚"),
    (r"(?i)(?:post|in)\s+(?P<num>\d+)\s+(?P<unit>%s)" % _IA_UNIT_RE,
     _ia_later),
    (r"(?i)(?P<num>\d+)\s+(?P<unit>%s)\s+retro" % _IA_UNIT_RE, _ia_ago),
    (r"(?i)\bproxime\s+septimana\b", "下周"),
    (r"(?i)\bseptimana\s+passate\b", "上周"),
    (r"(?i)\bproxime\s+mense\b", "下个月"),
    (r"(?i)\bmense\s+passate\b", "上个月"),
    (r"(?i)\bproxime\s+anno\b", "明年"),
    (r"(?i)\banno\s+passate\b", "去年"),
]

for _month in sorted(_IA_MONTHS, key=len, reverse=True):
    SUB_TRANSLATE.append((r"(?i)\b%s\b" % _month, _IA_MONTHS[_month]))

for _weekday in sorted(_IA_WEEKDAYS, key=len, reverse=True):
    SUB_TRANSLATE.append((r"(?i)\b%s\b" % _weekday, _IA_WEEKDAYS[_weekday]))
