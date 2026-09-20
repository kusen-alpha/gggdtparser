# -*- coding:utf-8 -*-

"""
克罗地亚语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_HR_UNITS = {
    "sekund": "秒", "sekunda": "秒", "sekunde": "秒",
    "minut": "分钟", "minuta": "分钟", "minute": "分钟",
    "sat": "小时", "sata": "小时", "sati": "小时",
    "dan": "天", "dana": "天",
    "tjedan": "周", "tjedna": "周", "tjedni": "周", "tjedana": "周",
    "mjesec": "月", "mjeseca": "月", "mjeseci": "月",
    "godina": "年", "godine": "年",
}
_HR_UNIT_RE = (
    r"sekund[ae]?|minut[ae]?|sat(?:i|a)?|dan(?:a)?|"
    r"tjedn[ai]|tjedana|mjesec(?:a|i)?|godin[ae]"
)


def _hr_later(match):
    return "%s%s后" % (match.group(1), _HR_UNITS[match.group(2)])


def _hr_earlier(match):
    return "%s%s前" % (match.group(1), _HR_UNITS[match.group(2)])


SUB_TRANSLATE = [
    (r"\bsiječanj\b", "1月"),
    (r"\bveljača\b", "2月"),
    (r"\božujak\b", "3月"),
    (r"\btravanj\b", "4月"),
    (r"\bsvibanj\b", "5月"),
    (r"\blipanj\b", "6月"),
    (r"\bsrpanj\b", "7月"),
    (r"\bkolovoz\b", "8月"),
    (r"\brujan\b", "9月"),
    (r"\blistopad\b", "10月"),
    (r"\bstudeni\b", "11月"),
    (r"\bprosinac\b", "12月"),
    (r"\bprekjučer\b", "前天"),
    (r"\bprekosutra\b", "后天"),
    (r"\bdanas\b", "今天"),
    (r"\bjučer\b", "昨天"),
    (r"\bsutra\b", "明天"),
    (r"za\s+(?P<a>\d+)\s*(?P<b>%s)" % _HR_UNIT_RE, _hr_later),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+kasnije" % _HR_UNIT_RE, _hr_later),
    (r"prije\s+(?P<a>\d+)\s*(?P<b>%s)" % _HR_UNIT_RE, _hr_earlier),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+ranije" % _HR_UNIT_RE, _hr_earlier),
    (r"\b(?:upravo\s+sada|sada)\b", "刚刚"),
    (r"\bsljedeći\s+tjedan\b", "下周"),
    (r"\bprošli\s+tjedan\b", "上周"),
    (r"\bsljedeći\s+mjesec\b", "下个月"),
    (r"\bprošli\s+mjesec\b", "上个月"),
    (r"\bsljedeća\s+godina\b", "明年"),
    (r"\bprošla\s+godina\b", "去年"),
]
