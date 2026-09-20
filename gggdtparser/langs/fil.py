# -*- coding:utf-8 -*-

"""
菲律宾语（他加禄语）
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_FIL_UNITS = {
    "segundo": "秒", "minuto": "分钟", "oras": "小时",
    "araw": "天", "linggo": "周", "buwan": "月", "taon": "年",
}

_FIL_WEEKDAYS = {
    "lunes": "周一",
    "martes": "周二",
    "miyerkules": "周三",
    "huwebes": "周四",
    "biyernes": "周五",
    "sabado": "周六",
}

SUB_TRANSLATE = [
    (r"\bika-(\d+)\b", lambda m: m.group(1)),
    (r"(?i)\b(?:sa\s+)?(?:susunod\s+na|darating\s+na)\s+(lunes|martes|miyerkules|huwebes|biyernes|sabado)\b",
     lambda m: "下%s" % _FIL_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(?:noong\s+)?(?:nakaraang|naunang|huling)\s+(lunes|martes|miyerkules|huwebes|biyernes|sabado)\b",
     lambda m: "上%s" % _FIL_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\bngayong\s+(lunes|martes|miyerkules|huwebes|biyernes|sabado)\b",
     lambda m: "这%s" % _FIL_WEEKDAYS[m.group(1).lower()]),
    (r"\bEnero\b", "1月"),
    (r"\bPebrero\b", "2月"),
    (r"\bMarso\b", "3月"),
    (r"\bAbril\b", "4月"),
    (r"\bMayo\b", "5月"),
    (r"\bHunyo\b", "6月"),
    (r"\bHulyo\b", "7月"),
    (r"\bAgosto\b", "8月"),
    (r"\bSetyembre\b", "9月"),
    (r"\bOktubre\b", "10月"),
    (r"\bNobyembre\b", "11月"),
    (r"\bDisyembre\b", "12月"),
    (r"\bnoong\s+isang\s+araw\b", "前天"),
    (r"\bsa\s+makalawa\b", "后天"),
    (r"(?i)\b(?:ngayong\s+umaga|kaninang\s+umaga)\b", "今天 08:00 am"),
    (r"(?i)\bngayong\s+hapon\b", "今天 15:00 pm"),
    (r"(?i)\bngayong\s+gabi\b", "今天 20:00 pm"),
    (r"(?i)\bmamayang\s+gabi\b", "今天 22:00 pm"),
    (r"(?i)\bbukas\s+(?:ng\s+)?umaga\b", "明天 08:00 am"),
    (r"(?i)\bbukas\s+(?:ng\s+)?gabi\b", "明天 20:00 pm"),
    (r"(?i)\bkagabi\b", "昨天 22:00 pm"),
    (r"(?i)\btanghali\b", "12:00 pm"),
    (r"(?i)\bhatinggabi\b", "12:00 am"),
    (r"\b(?:ngayon\s+din|sa\s+ngayon)\b", "刚刚"),
    (r"\bngayon\b", "今天"),
    (r"\bkahapon\b", "昨天"),
    (r"\bbukas\b", "明天"),
    (r"sa\s+loob\s+ng\s+(?P<num>\d+)\s*(?P<unit>segundo|minuto|oras|araw|linggo|buwan|taon)",
     lambda m: "%s%s后" % (
         m.group("num"), _FIL_UNITS[m.group("unit")])),
    (r"(?P<num>\d+)\s*(?P<unit>segundo|minuto|oras|araw|linggo|buwan|taon)\s+ang\s+nakalipas",
     lambda m: "%s%s前" % (
         m.group("num"), _FIL_UNITS[m.group("unit")])),
    (r"\bng\s+", ""),
    (r"\bsusunod\s+na\s+linggo\b", "下周"),
    (r"\bnakaraang\s+linggo\b", "上周"),
    (r"\bsusunod\s+na\s+buwan\b", "下个月"),
    (r"\bnakaraang\s+buwan\b", "上个月"),
    (r"\bsusunod\s+na\s+taon\b", "明年"),
    (r"\bnakaraang\s+taon\b", "去年"),
]
