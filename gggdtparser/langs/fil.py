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

SUB_TRANSLATE = [
    (r"\bika-(\d+)\b", lambda m: m.group(1)),
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
