# -*- coding:utf-8 -*-

"""
祖鲁语（Zulu）
"""

ACCURATE_REGEX_LIST = [
    r"(?P<m>\d{1,2})\s*[月]\s*(?P<Y>\d{4})",
]
FUZZY_REGEX_LIST = []

_ZU_UNITS = {
    "amahora": "小时", "imizuzu": "分钟", "izinsuku": "天",
    "amaviki": "周", "izinyanga": "月", "iminyaka": "年",
}
_ZU_UNIT_RE = "|".join(sorted(_ZU_UNITS, key=len, reverse=True))

_ZU_MONTHS = {
    "ujanuwari": "1月", "ufebruwari": "2月", "umashi": "3月",
    "u-ephreli": "4月", "umeyi": "5月", "ujuni": "6月",
    "ujulayi": "7月", "uagasti": "8月", "usepthemba": "9月",
    "u-okthoba": "10月", "unovemba": "11月", "udisemba": "12月",
}
_ZU_MONTHS_RE = "|".join(sorted(_ZU_MONTHS, key=len, reverse=True))


def _zu_month_no(name):
    return _ZU_MONTHS[name.lower()]


def _zu_named_date(match):
    return "%s %s %s" % (
        match.group("d"), _zu_month_no(match.group("name")), match.group("Y"))


def _zu_month_first(match):
    return "%s %s, %s" % (
        _zu_month_no(match.group("name")), match.group("d"), match.group("Y"))


def _zu_month_year(match):
    return "%s %s" % (_zu_month_no(match.group("name")), match.group("Y"))


def _zu_later(match):
    return "%s%s后" % (
        match.group("num"), _ZU_UNITS[match.group("unit").lower()])


def _zu_ago(match):
    return "%s%s前" % (
        match.group("num"), _ZU_UNITS[match.group("unit").lower()])


SUB_TRANSLATE = [
    (r"(?i)(?P<d>\d{1,2})\s*(?:ngosuku\s+lwe-?\d*\.?\s*)?(?P<name>%s)"
     r"\s+(?P<Y>\d{4})" % _ZU_MONTHS_RE, _zu_named_date),
    (r"(?i)(?P<name>%s)\s+(?P<d>\d{1,2}),\s+(?P<Y>\d{4})"
     % _ZU_MONTHS_RE, _zu_month_first),
    (r"(?i)(?P<name>%s)\s+(?P<Y>\d{4})" % _ZU_MONTHS_RE, _zu_month_year),
    (r"(?i)\bnamuhla\b", "今天"),
    (r"(?i)\bizolo\b", "昨天"),
    (r"(?i)\bkusasa\b", "明天"),
    (r"(?i)\bmanje\b", "刚刚"),
    (r"(?i)(?P<num>\d+)\s*(?P<unit>%s)\s+ezayo" % _ZU_UNIT_RE, _zu_later),
    (r"(?i)(?P<num>\d+)\s*(?P<unit>%s)\s+adlulile" % _ZU_UNIT_RE, _zu_ago),
    (r"(?i)\bisonto\s+ezayo\b", "下周"),
    (r"(?i)\bisonto\s+edlule\b", "上周"),
    (r"(?i)\binyanga\s+ezayo\b", "下个月"),
    (r"(?i)\binyanga\s+edlule\b", "上个月"),
    (r"(?i)\bunyaka\s+ozayo\b", "明年"),
    (r"(?i)\bunyaka\s+odlule\b", "去年"),
]

for _month in sorted(_ZU_MONTHS, key=len, reverse=True):
    SUB_TRANSLATE.append((r"(?i)\b%s\b" % _month, _ZU_MONTHS[_month]))
