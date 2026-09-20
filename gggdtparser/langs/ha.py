# -*- coding:utf-8 -*-

"""
豪萨语（Hausa）
"""

ACCURATE_REGEX_LIST = [
    r"(?P<m>\d{1,2})\s*[月]\s*(?P<Y>\d{4})",
]
FUZZY_REGEX_LIST = []

_HA_UNITS = {
    "sakan": "秒", "dakika": "秒", "minti": "分钟",
    "awa": "小时", "kwana": "天", "mako": "周",
    "wata": "月", "shekara": "年",
}
_HA_UNIT_RE = "|".join(sorted(_HA_UNITS, key=len, reverse=True))
_HA_NUMBERS = {
    "ɗaya": "1", "biyu": "2", "uku": "3", "hudu": "4", "biyar": "5",
    "shida": "6", "bakwai": "7", "takwas": "8", "tara": "9", "goma": "10",
}
_HA_NUM_RE = "|".join(
    ["[1-9]\\d*"] + sorted(_HA_NUMBERS, key=len, reverse=True))

_HA_MONTHS = {
    "janairu": "1月", "fabrairu": "2月", "maris": "3月",
    "afrilu": "4月", "mayu": "5月", "yuni": "6月",
    "yuli": "7月", "agusta": "8月", "satumba": "9月",
    "oktoba": "10月", "nuwamba": "11月", "disamba": "12月",
}
_HA_MONTHS_RE = "|".join(sorted(_HA_MONTHS, key=len, reverse=True))


def _ha_month_no(name):
    return _HA_MONTHS[name.lower()]


def _ha_named_date(match):
    return "%s %s %s" % (
        match.group("d"), _ha_month_no(match.group("name")), match.group("Y"))


def _ha_month_first(match):
    return "%s %s, %s" % (
        _ha_month_no(match.group("name")), match.group("d"), match.group("Y"))


def _ha_month_year(match):
    return "%s %s" % (_ha_month_no(match.group("name")), match.group("Y"))


def _ha_later(match):
    return "%s%s后" % (
        _HA_NUMBERS.get(match.group("num").lower(), match.group("num")),
        _HA_UNITS[match.group("unit").lower()])


def _ha_ago(match):
    return "%s%s前" % (
        _HA_NUMBERS.get(match.group("num").lower(), match.group("num")),
        _HA_UNITS[match.group("unit").lower()])


SUB_TRANSLATE = [
    (r"(?i)(?P<d>\d{1,2})\s*(?:na\s+)?(?P<name>%s)\s+(?P<Y>\d{4})"
     % _HA_MONTHS_RE, _ha_named_date),
    (r"(?i)(?P<name>%s)\s+(?P<d>\d{1,2}),\s+(?P<Y>\d{4})"
     % _HA_MONTHS_RE, _ha_month_first),
    (r"(?i)(?P<name>%s)\s+(?P<Y>\d{4})" % _HA_MONTHS_RE, _ha_month_year),
    (r"(?i)\bkwana\s+biyu\s+da\s+suka\s+gabata\b", "前天"),
    (r"(?i)\bkwana\s+biyu\s+masu\s+zuwa\b", "后天"),
    (r"(?i)\byau\b", "今天"),
    (r"(?i)\bjiya\b", "昨天"),
    (r"(?i)\bgobe\b|\bgobi\b", "明天"),
    (r"(?i)\ba\s+yanzu\b|\byanzu\b", "刚刚"),
    (r"(?i)\bbayan\s+(?P<unit>%s)\s+(?P<num>%s)"
     % (_HA_UNIT_RE, _HA_NUM_RE), _ha_later),
    (r"(?i)(?P<unit>%s)\s+(?P<num>%s)\s+da\s+suka\s+wuce"
     % (_HA_UNIT_RE, _HA_NUM_RE),
     _ha_ago),
    (r"(?i)\bmako\s+mai\s+zuwa\b", "下周"),
    (r"(?i)\bmakon\s+da\s+ya\s+gabata\b", "上周"),
    (r"(?i)\bwata\s+mai\s+zuwa\b", "下个月"),
    (r"(?i)\bwatan\s+da\s+ya\s+gabata\b", "上个月"),
    (r"(?i)\bshekara\s+mai\s+zuwa\b", "明年"),
    (r"(?i)\bshekarar\s+da\s+ta\s+gabata\b", "去年"),
]

for _month in sorted(_HA_MONTHS, key=len, reverse=True):
    SUB_TRANSLATE.append((r"(?i)\b%s\.?\b" % _month, _HA_MONTHS[_month]))
