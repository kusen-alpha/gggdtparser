# -*- coding:utf-8 -*-

"""
拉丁语（Latin）
"""

ACCURATE_REGEX_LIST = [
    r"(?P<m>\d{1,2})\s*[月]\s*(?P<Y>\d{4})",
]
FUZZY_REGEX_LIST = []

_LA_UNITS = {
    "secunda": "秒", "minuta": "分钟", "hora": "小时",
    "dies": "天", "septimana": "周", "mensis": "月", "annus": "年",
}
_LA_UNITS.update({
    "secundas": "秒", "minutas": "分钟", "horas": "小时",
    "septimanae": "周", "menses": "月", "anni": "年",
})
_LA_UNIT_RE = "|".join(sorted(_LA_UNITS, key=len, reverse=True))

_LA_MONTHS = {
    "ianuarius": "1月", "ianuarii": "1月",
    "februarius": "2月", "februarii": "2月",
    "martius": "3月", "martii": "3月",
    "aprilis": "4月",
    "maius": "5月", "maii": "5月",
    "iunius": "6月", "iunii": "6月",
    "iulius": "7月", "iulii": "7月",
    "augustus": "8月", "augusti": "8月",
    "september": "9月", "septembris": "9月",
    "october": "10月", "octobris": "10月",
    "november": "11月", "novembris": "11月",
    "december": "12月", "decembris": "12月",
}
_LA_MONTHS_RE = "|".join(sorted(_LA_MONTHS, key=len, reverse=True))


def _la_month_no(name):
    return _LA_MONTHS[name.lower()]


def _la_named_date(match):
    return "%s %s %s" % (
        match.group("d"), _la_month_no(match.group("name")), match.group("Y"))


def _la_month_first(match):
    return "%s %s, %s" % (
        _la_month_no(match.group("name")), match.group("d"), match.group("Y"))


def _la_month_year(match):
    return "%s %s" % (_la_month_no(match.group("name")), match.group("Y"))


def _la_later(match):
    return "%s%s后" % (
        match.group("num"), _LA_UNITS[match.group("unit").lower()])


def _la_ago(match):
    return "%s%s前" % (
        match.group("num"), _LA_UNITS[match.group("unit").lower()])


SUB_TRANSLATE = [
    (r"(?i)(?P<d>\d{1,2})\s*(?:mensis\s+)?(?P<name>%s)\s+(?P<Y>\d{4})"
     % _LA_MONTHS_RE, _la_named_date),
    (r"(?i)(?P<name>%s)\s+(?P<d>\d{1,2}),\s+(?P<Y>\d{4})"
     % _LA_MONTHS_RE, _la_month_first),
    (r"(?i)(?P<name>%s)\s+(?P<Y>\d{4})" % _LA_MONTHS_RE, _la_month_year),
    (r"(?i)\bante\s+heri\b", "前天"),
    (r"(?i)\bpost\s+cras\b", "后天"),
    (r"(?i)\bhodie\b", "今天"),
    (r"(?i)\bheri\b", "昨天"),
    (r"(?i)\bcras\b", "明天"),
    (r"(?i)\b(?:modo|iam\s+nunc)\b", "刚刚"),
    (r"(?i)\bpost\s+(?P<num>\d+)\s+(?P<unit>%s)" % _LA_UNIT_RE, _la_later),
    (r"(?i)\bante\s+(?P<num>\d+)\s+(?P<unit>%s)" % _LA_UNIT_RE, _la_ago),
    (r"(?i)\bproxima\s+septimana\b", "下周"),
    (r"(?i)\bpraeterita\s+septimana\b", "上周"),
    (r"(?i)\bproximo\s+mense\b", "下个月"),
    (r"(?i)\bpraeterito\s+mense\b", "上个月"),
    (r"(?i)\bproximo\s+anno\b", "明年"),
    (r"(?i)\bpraeterito\s+anno\b", "去年"),
]

for _month in sorted(_LA_MONTHS, key=len, reverse=True):
    SUB_TRANSLATE.append((r"(?i)\b%s\b" % _month, _LA_MONTHS[_month]))
