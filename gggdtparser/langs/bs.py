# -*- coding:utf-8 -*-

"""
波斯尼亚语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_BS_UNITS = {
    "sekunda": "秒", "sekunde": "秒", "sekundi": "秒",
    "minuta": "分钟", "minute": "分钟", "minuti": "分钟",
    "sat": "小时", "sata": "小时", "sati": "小时",
    "dan": "天", "dana": "天", "dani": "天",
    "sedmica": "周", "sedmice": "周", "sedmici": "周",
    "mjesec": "月", "mjeseca": "月", "mjeseci": "月",
    "godina": "年", "godine": "年", "godini": "年",
}
_BS_UNIT_RE = (
    r"sekund[aei]?|minut[aei]?|sat[aei]?|dan[ai]?|"
    r"sedmic[aei]?|mjesec[ai]?|godin[aei]?"
)


def _bs_later(match):
    return "%s%s后" % (match.group("a"), _BS_UNITS[match.group("b")])


def _bs_earlier(match):
    return "%s%s前" % (match.group("a"), _BS_UNITS[match.group("b")])


SUB_TRANSLATE = [
    (r"\bjanuar[a]?\b", "1月"),
    (r"\bfebruar[a]?\b", "2月"),
    (r"\bmart[a]?\b", "3月"),
    (r"\bapril[a]?\b", "4月"),
    (r"\bmaj[a]?\b", "5月"),
    (r"\bjun(?:i|a)\b", "6月"),
    (r"\bjul(?:i|a)\b", "7月"),
    (r"\baugust[a]?\b", "8月"),
    (r"\bseptemb(?:ar|ra)\b", "9月"),
    (r"\boktob(?:ar|ra)\b", "10月"),
    (r"\bnovemb(?:ar|ra)\b", "11月"),
    (r"\bdecemb(?:ar|ra)\b", "12月"),
    (r"\bprekjučer\b|\bprekjucer\b", "前天"),
    (r"\bprekosutra\b", "后天"),
    (r"\bdanas\b", "今天"),
    (r"\bjučer\b|\bjucer\b", "昨天"),
    (r"\bsutra\b", "明天"),
    (r"\b(?:sada|odmah)\b", "刚刚"),
    (r"\bza\s+(?P<a>\d+)\s*(?P<b>%s)" % _BS_UNIT_RE, _bs_later),
    (r"\bprije\s+(?P<a>\d+)\s*(?P<b>%s)" % _BS_UNIT_RE, _bs_earlier),
    (r"sljedeća\s+sedmica|iduća\s+sedmica", "下周"),
    (r"prošla\s+sedmica", "上周"),
    (r"sljedeći\s+mjesec|idući\s+mjesec", "下个月"),
    (r"prošli\s+mjesec", "上个月"),
    (r"sljedeća\s+godina|iduća\s+godina", "明年"),
    (r"prošla\s+godina", "去年"),
]
