# -*- coding:utf-8 -*-

"""
马达加斯加语（Malagasy）
"""

ACCURATE_REGEX_LIST = [
    r"(?P<m>\d{1,2})\s*[月]\s*(?P<Y>\d{4})",
]
FUZZY_REGEX_LIST = []

_MG_UNITS = {
    "segondra": "秒", "minitra": "分钟", "ora": "小时",
    "andro": "天", "herinandro": "周", "volana": "月", "taona": "年",
}
_MG_UNIT_RE = "|".join(sorted(_MG_UNITS, key=len, reverse=True))

_MG_MONTHS = {
    "janoary": "1月", "febroary": "2月", "martsa": "3月",
    "aprily": "4月", "mey": "5月", "jona": "6月",
    "jolay": "7月", "aogositra": "8月", "septambra": "9月",
    "oktobra": "10月", "novambra": "11月", "desambra": "12月",
}
_MG_MONTHS_RE = "|".join(sorted(_MG_MONTHS, key=len, reverse=True))


def _mg_month_no(name):
    return _MG_MONTHS[name.lower()]


def _mg_named_date(match):
    return "%s %s %s" % (
        match.group("d"), _mg_month_no(match.group("name")), match.group("Y"))


def _mg_month_first(match):
    return "%s %s, %s" % (
        _mg_month_no(match.group("name")), match.group("d"), match.group("Y"))


def _mg_month_year(match):
    return "%s %s" % (_mg_month_no(match.group("name")), match.group("Y"))


def _mg_later(match):
    return "%s%s后" % (
        match.group("num"), _MG_UNITS[match.group("unit").lower()])


def _mg_ago(match):
    return "%s%s前" % (
        match.group("num"), _MG_UNITS[match.group("unit").lower()])


SUB_TRANSLATE = [
    (r"(?i)(?P<d>\d{1,2})\s*(?:ny\s+)?(?P<name>%s)\s+(?P<Y>\d{4})"
     % _MG_MONTHS_RE, _mg_named_date),
    (r"(?i)(?P<name>%s)\s+(?P<d>\d{1,2}),\s+(?P<Y>\d{4})"
     % _MG_MONTHS_RE, _mg_month_first),
    (r"(?i)(?P<name>%s)\s+(?P<Y>\d{4})" % _MG_MONTHS_RE, _mg_month_year),
    (r"(?i)\b2\s+andro\s+lasa\s+izay\b", "前天"),
    (r"(?i)\b2\s+andro\s+avy\s+eo\b", "后天"),
    (r"(?i)\banio\b", "今天"),
    (r"(?i)\bomaly\b", "昨天"),
    (r"(?i)\brahampitso\b", "明天"),
    (r"(?i)\bizao\s+(?:vao|ihany)\b", "刚刚"),
    (r"(?i)\bafaka\s+(?P<num>\d+)\s+(?P<unit>%s)" % _MG_UNIT_RE, _mg_later),
    (r"(?i)(?P<num>\d+)\s+(?P<unit>%s)\s+lasa\s+izay" % _MG_UNIT_RE,
     _mg_ago),
    (r"(?i)\bherinandro\s+ho\s+avy\b", "下周"),
    (r"(?i)\bherinandro\s+lasa\b", "上周"),
    (r"(?i)\bvolana\s+ho\s+avy\b", "下个月"),
    (r"(?i)\bvolana\s+lasa\b", "上个月"),
    (r"(?i)\btaona\s+ho\s+avy\b", "明年"),
    (r"(?i)\btaona\s+lasa\b", "去年"),
]

for _month in sorted(_MG_MONTHS, key=len, reverse=True):
    SUB_TRANSLATE.append((r"(?i)\b%s\.?\b" % _month, _MG_MONTHS[_month]))
