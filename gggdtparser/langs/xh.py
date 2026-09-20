# -*- coding:utf-8 -*-

"""
科萨语（Xhosa）
"""

ACCURATE_REGEX_LIST = [
    r"(?P<m>\d{1,2})\s*[月]\s*(?P<Y>\d{4})",
]
FUZZY_REGEX_LIST = []

_XH_UNITS = {
    "iiyure": "小时", "imizuzu": "分钟", "iintsuku": "天",
    "iiveki": "周", "iinyanga": "月", "iminyaka": "年",
}
_XH_UNIT_RE = "|".join(sorted(_XH_UNITS, key=len, reverse=True))

_XH_MONTHS = {
    "ujanuwari": "1月", "ufebruwari": "2月", "umatshi": "3月",
    "uaprili": "4月", "umeyi": "5月", "ujuni": "6月",
    "ujulayi": "7月", "uagasti": "8月", "useptemba": "9月",
    "uoktobha": "10月", "unovemba": "11月", "udisemba": "12月",
}
_XH_MONTHS_RE = "|".join(sorted(_XH_MONTHS, key=len, reverse=True))


def _xh_month_no(name):
    return _XH_MONTHS[name.lower()]


def _xh_named_date(match):
    return "%s %s %s" % (
        match.group("d"), _xh_month_no(match.group("name")), match.group("Y"))


def _xh_month_first(match):
    return "%s %s, %s" % (
        _xh_month_no(match.group("name")), match.group("d"), match.group("Y"))


def _xh_month_year(match):
    return "%s %s" % (_xh_month_no(match.group("name")), match.group("Y"))


def _xh_later(match):
    return "%s%s后" % (
        match.group("num"), _XH_UNITS[match.group("unit").lower()])


def _xh_ago(match):
    return "%s%s前" % (
        match.group("num"), _XH_UNITS[match.group("unit").lower()])


SUB_TRANSLATE = [
    (r"(?i)(?P<d>\d{1,2})\s*(?:ngomhla\s+)?(?P<name>%s)\s+(?P<Y>\d{4})"
     % _XH_MONTHS_RE, _xh_named_date),
    (r"(?i)(?P<name>%s)\s+(?P<d>\d{1,2}),\s+(?P<Y>\d{4})"
     % _XH_MONTHS_RE, _xh_month_first),
    (r"(?i)(?P<name>%s)\s+(?P<Y>\d{4})" % _XH_MONTHS_RE, _xh_month_year),
    (r"(?i)\bnamhlanje\b", "今天"),
    (r"(?i)\bizolo\b", "昨天"),
    (r"(?i)\bngomso\b", "明天"),
    (r"(?i)\bngoku\b", "刚刚"),
    (r"(?i)(?P<num>\d+)\s*(?P<unit>%s)\s+ezizayo" % _XH_UNIT_RE,
     _xh_later),
    (r"(?i)(?P<num>\d+)\s*(?P<unit>%s)\s+ezidlulileyo" % _XH_UNIT_RE,
     _xh_ago),
    (r"(?i)\biveki\s+ezayo\b", "下周"),
    (r"(?i)\biveki\s+ephelileyo\b", "上周"),
    (r"(?i)\binyanga\s+ezayo\b", "下个月"),
    (r"(?i)\binyanga\s+ephelileyo\b", "上个月"),
    (r"(?i)\bunyaka\s+ozayo\b", "明年"),
    (r"(?i)\bunyaka\s+ophelileyo\b", "去年"),
]

for _month in sorted(_XH_MONTHS, key=len, reverse=True):
    SUB_TRANSLATE.append((r"(?i)\b%s\b" % _month, _XH_MONTHS[_month]))
