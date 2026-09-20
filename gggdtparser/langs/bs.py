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

_BS_WEEKDAYS = {
    "ponedjeljak": "周一",
    "utorak": "周二",
    "srijeda": "周三",
    "četvrtak": "周四",
    "petak": "周五",
    "subota": "周六",
    "nedjelja": "周日",
}


def _bs_later(match):
    return "%s%s后" % (match.group("a"), _BS_UNITS[match.group("b")])


def _bs_earlier(match):
    return "%s%s前" % (match.group("a"), _BS_UNITS[match.group("b")])


SUB_TRANSLATE = [
    (r"(?i)\b(?:sljedeć[ia]|iduć[ia])\s+(ponedjeljak|utorak|srijeda|četvrtak|petak|subota|nedjelja)\b",
     lambda m: "下%s" % _BS_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(?:prošl[ia]|prethodn[ia])\s+(ponedjeljak|utorak|srijeda|četvrtak|petak|subota|nedjelja)\b",
     lambda m: "上%s" % _BS_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(?:ovaj|ova)\s+(ponedjeljak|utorak|srijeda|četvrtak|petak|subota|nedjelja)\b",
     lambda m: "这%s" % _BS_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(ponedjeljak|utorak|srijeda|četvrtak|petak|subota|nedjelja)\b",
     lambda m: "周%s" % {
         "ponedjeljak": "一", "utorak": "二", "srijeda": "三",
         "četvrtak": "四", "petak": "五", "subota": "六",
         "nedjelja": "日"}[m.group(1).lower()]),
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
    (r"(?i)\bdanas\s+(?:ujutro|u\s+jutro)\b", "今天 08:00 am"),
    (r"(?i)\bdanas\s+popodne\b", "今天 15:00 pm"),
    (r"(?i)\bdanas\s+(?:navečer|u\s+večer)\b", "今天 20:00 pm"),
    (r"(?i)\bsutra\s+(?:ujutro|u\s+jutro)\b", "明天 08:00 am"),
    (r"(?i)\bsutra\s+(?:navečer|u\s+večer)\b", "明天 20:00 pm"),
    (r"(?i)\bjučer\s+(?:navečer|u\s+večer)\b", "昨天 20:00 pm"),
    (r"(?i)\b(?:u\s+podne|podne)\b", "12:00 pm"),
    (r"(?i)\bponoć\b", "12:00 am"),
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
