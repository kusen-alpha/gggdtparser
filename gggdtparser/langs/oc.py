# -*- coding:utf-8 -*-

"""
奥克语（Occitan）
"""

ACCURATE_REGEX_LIST = [
    r"(?P<m>\d{1,2})\s*[月]\s*(?P<Y>\d{4})",
]
FUZZY_REGEX_LIST = []

_OC_UNITS = {
    "segonda": "秒", "minuta": "分钟", "ora": "小时",
    "jorn": "天", "setmana": "周", "mes": "月", "an": "年",
}
_OC_UNITS.update({
    "segondas": "秒", "minutas": "分钟", "oras": "小时",
    "jorns": "天", "setmanas": "周", "meses": "月", "ans": "年",
})
_OC_UNIT_RE = "|".join(sorted(_OC_UNITS, key=len, reverse=True))

_OC_MONTHS = {
    "genièr": "1月", "febrièr": "2月", "març": "3月",
    "abril": "4月", "mai": "5月", "junh": "6月",
    "julhet": "7月", "agost": "8月", "setembre": "9月",
    "octobre": "10月", "novembre": "11月", "decembre": "12月",
}
_OC_MONTHS_RE = "|".join(sorted(_OC_MONTHS, key=len, reverse=True))


def _oc_month_no(name):
    return _OC_MONTHS[name.lower()]


def _oc_named_date(match):
    return "%s %s %s" % (
        match.group("d"), _oc_month_no(match.group("name")), match.group("Y"))


def _oc_month_first(match):
    return "%s %s, %s" % (
        _oc_month_no(match.group("name")), match.group("d"), match.group("Y"))


def _oc_month_year(match):
    return "%s %s" % (_oc_month_no(match.group("name")), match.group("Y"))


def _oc_later(match):
    return "%s%s后" % (
        match.group("num"), _OC_UNITS[match.group("unit").lower()])


def _oc_ago(match):
    return "%s%s前" % (
        match.group("num"), _OC_UNITS[match.group("unit").lower()])


SUB_TRANSLATE = [
    (r"(?i)(?P<d>\d{1,2})\s*(?:de\s+)?(?P<name>%s)\s+(?P<Y>\d{4})"
     % _OC_MONTHS_RE, _oc_named_date),
    (r"(?i)(?P<name>%s)\s+(?P<d>\d{1,2}),\s+(?P<Y>\d{4})"
     % _OC_MONTHS_RE, _oc_month_first),
    (r"(?i)(?P<name>%s)\s+(?P<Y>\d{4})" % _OC_MONTHS_RE, _oc_month_year),
    (r"(?i)\babans\s+ièr\b", "前天"),
    (r"(?i)\baprèp\s+deman\b", "后天"),
    (r"(?i)\buèi\b", "今天"),
    (r"(?i)\bièr\b", "昨天"),
    (r"(?i)\bdeman\b", "明天"),
    (r"(?i)\bara\s+meteis\b", "刚刚"),
    (r"(?i)\bdins\s+(?P<num>\d+)\s+(?P<unit>%s)" % _OC_UNIT_RE, _oc_later),
    (r"(?i)\bfa\s+(?P<num>\d+)\s+(?P<unit>%s)" % _OC_UNIT_RE, _oc_ago),
    (r"(?i)\bla\s+setmana\s+que\s+ven\b", "下周"),
    (r"(?i)\bla\s+setmana\s+passada\b", "上周"),
    (r"(?i)\blo\s+mes\s+que\s+ven\b", "下个月"),
    (r"(?i)\blo\s+mes\s+passat\b", "上个月"),
    (r"(?i)\bl'an\s+que\s+ven\b", "明年"),
    (r"(?i)\bl'an\s+passat\b", "去年"),
]

for _month in sorted(_OC_MONTHS, key=len, reverse=True):
    SUB_TRANSLATE.append((r"(?i)\b%s\b" % _month, _OC_MONTHS[_month]))
