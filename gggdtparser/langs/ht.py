# -*- coding:utf-8 -*-

"""
海地克里奥尔语（Haitian Creole）
"""

ACCURATE_REGEX_LIST = [
    r"(?P<m>\d{1,2})\s*[月]\s*(?P<Y>\d{4})",
]
FUZZY_REGEX_LIST = []

_HT_UNITS = {
    "segond": "秒", "minit": "分钟", "èdtan": "小时",
    "jou": "天", "semèn": "周", "mwa": "月", "ane": "年",
}
_HT_UNIT_RE = "|".join(sorted(_HT_UNITS, key=len, reverse=True))

_HT_MONTHS = {
    "janvye": "1月", "fevriye": "2月", "mas": "3月",
    "avril": "4月", "me": "5月", "jen": "6月",
    "jiyè": "7月", "out": "8月", "septanm": "9月",
    "oktòb": "10月", "novanm": "11月", "desanm": "12月",
}
_HT_MONTHS_RE = "|".join(sorted(_HT_MONTHS, key=len, reverse=True))


def _ht_month_no(name):
    return _HT_MONTHS[name.lower()]


def _ht_named_date(match):
    return "%s %s %s" % (
        match.group("d"), _ht_month_no(match.group("name")), match.group("Y"))


def _ht_month_first(match):
    return "%s %s, %s" % (
        _ht_month_no(match.group("name")), match.group("d"), match.group("Y"))


def _ht_month_year(match):
    return "%s %s" % (_ht_month_no(match.group("name")), match.group("Y"))


def _ht_later(match):
    return "%s%s后" % (
        match.group("num"), _HT_UNITS[match.group("unit").lower()])


def _ht_ago(match):
    return "%s%s前" % (
        match.group("num"), _HT_UNITS[match.group("unit").lower()])


SUB_TRANSLATE = [
    (r"(?i)(?P<d>\d{1,2})\s*(?:d'|de)?\s*(?P<name>%s)\s+(?P<Y>\d{4})"
     % _HT_MONTHS_RE, _ht_named_date),
    (r"(?i)(?P<name>%s)\s+(?P<d>\d{1,2}),\s+(?P<Y>\d{4})"
     % _HT_MONTHS_RE, _ht_month_first),
    (r"(?i)(?P<name>%s)\s+(?P<Y>\d{4})" % _HT_MONTHS_RE, _ht_month_year),
    (r"(?i)\bavantyè\b", "前天"),
    (r"(?i)\bapre\s+demen\b", "后天"),
    (r"(?i)\bjodi(?:\s+a)?\b", "今天"),
    (r"(?i)\byè\b", "昨天"),
    (r"(?i)\bdemen\b", "明天"),
    (r"(?i)\b(?:kounye\s+a|fèk)\b", "刚刚"),
    (r"(?i)\bnan\s+(?P<num>\d+)\s+(?P<unit>%s)" % _HT_UNIT_RE, _ht_later),
    (r"(?i)\bsa\s+gen\s+(?P<num>\d+)\s+(?P<unit>%s)" % _HT_UNIT_RE,
     _ht_ago),
    (r"(?i)\bsemèn\s+pwochèn\b", "下周"),
    (r"(?i)\bsemèn\s+pase\b", "上周"),
    (r"(?i)\bmwa\s+pwochèn\b", "下个月"),
    (r"(?i)\bmwa\s+pase\b", "上个月"),
    (r"(?i)\bane\s+pwochèn\b", "明年"),
    (r"(?i)\bane\s+pase\b", "去年"),
]

for _month in sorted(_HT_MONTHS, key=len, reverse=True):
    SUB_TRANSLATE.append((r"(?i)\b%s\b" % _month, _HT_MONTHS[_month]))
