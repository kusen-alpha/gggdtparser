# -*- coding:utf-8 -*-

"""
土库曼语（Turkmen）
"""

ACCURATE_REGEX_LIST = [
    r"(?P<m>\d{1,2})\s*[月]\s*(?P<Y>\d{4})",
]
FUZZY_REGEX_LIST = []

_TK_UNITS = {
    "sekunt": "秒", "minut": "分钟", "sagat": "小时",
    "gün": "天", "hepde": "周", "aý": "月", "ýyl": "年",
}
_TK_UNIT_RE = "|".join(sorted(_TK_UNITS, key=len, reverse=True))

_TK_MONTHS = {
    "ýanwar": "1月", "fewral": "2月", "mart": "3月",
    "aprel": "4月", "maý": "5月", "iýun": "6月",
    "iýul": "7月", "awgust": "8月", "sentýabr": "9月",
    "oktýabr": "10月", "noýabr": "11月", "dekabr": "12月",
}
_TK_MONTHS_RE = "|".join(sorted(_TK_MONTHS, key=len, reverse=True))


def _tk_month_no(name):
    return _TK_MONTHS[name.lower()]


def _tk_named_date(match):
    return "%s %s %s" % (
        match.group("d"), _tk_month_no(match.group("name")), match.group("Y"))


def _tk_month_first(match):
    return "%s %s, %s" % (
        _tk_month_no(match.group("name")), match.group("d"), match.group("Y"))


def _tk_month_year(match):
    return "%s %s" % (_tk_month_no(match.group("name")), match.group("Y"))


def _tk_later(match):
    return "%s%s后" % (
        match.group("num"), _TK_UNITS[match.group("unit").lower()])


def _tk_ago(match):
    return "%s%s前" % (
        match.group("num"), _TK_UNITS[match.group("unit").lower()])


SUB_TRANSLATE = [
    (r"(?i)(?P<d>\d{1,2})\s*(?:nji|njy)?\s*(?P<name>%s)\s+(?P<Y>\d{4})"
     % _TK_MONTHS_RE, _tk_named_date),
    (r"(?i)(?P<name>%s)\s+(?P<d>\d{1,2}),\s+(?P<Y>\d{4})"
     % _TK_MONTHS_RE, _tk_month_first),
    (r"(?i)(?P<name>%s)\s+(?P<Y>\d{4})" % _TK_MONTHS_RE, _tk_month_year),
    (r"(?i)\bşu\s+gün\b", "今天"),
    (r"(?i)\bdüýn\b", "昨天"),
    (r"(?i)\bertir\b", "明天"),
    (r"(?i)\b(?:häzir|ýaňy)\b", "刚刚"),
    (r"(?i)(?P<num>\d+)\s*(?P<unit>%s)(?:dan|den|an|en)?\s+soň"
     % _TK_UNIT_RE, _tk_later),
    (r"(?i)(?P<num>\d+)\s*(?P<unit>%s)\s+öň" % _TK_UNIT_RE, _tk_ago),
    (r"(?i)\bindiki\s+hepde\b", "下周"),
    (r"(?i)\bgeçen\s+hepde\b", "上周"),
    (r"(?i)\bindiki\s+aý\b", "下个月"),
    (r"(?i)\bgeçen\s+aý\b", "上个月"),
    (r"(?i)\bindiki\s+ýyl\b", "明年"),
    (r"(?i)\bgeçen\s+ýyl\b", "去年"),
]

for _month in sorted(_TK_MONTHS, key=len, reverse=True):
    SUB_TRANSLATE.append((r"(?i)\b%s\.?\b" % _month, _TK_MONTHS[_month]))
