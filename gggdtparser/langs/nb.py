# -*- coding:utf-8 -*-

"""
挪威语(博克马尔/新挪威语共用词形)
"""

ACCURATE_REGEX_LIST = []

SUB_TRANSLATE = [
    (r"(?i)\b(?:neste|kommende)\s+(mandag|tirsdag|onsdag|torsdag|fredag|lørdag|søndag)\b",
     lambda m: "下%s" % {
         "mandag": "周一", "tirsdag": "周二", "onsdag": "周三",
         "torsdag": "周四", "fredag": "周五", "lørdag": "周六",
         "søndag": "周日"}[m.group(1).lower()]),
    (r"(?i)\bforrige\s+(mandag|tirsdag|onsdag|torsdag|fredag|lørdag|søndag)\b",
     lambda m: "上%s" % {
         "mandag": "周一", "tirsdag": "周二", "onsdag": "周三",
         "torsdag": "周四", "fredag": "周五", "lørdag": "周六",
         "søndag": "周日"}[m.group(1).lower()]),
    (r"(?i)\bdenne\s+(mandag|tirsdag|onsdag|torsdag|fredag|lørdag|søndag)\b",
     lambda m: "这%s" % {
         "mandag": "周一", "tirsdag": "周二", "onsdag": "周三",
         "torsdag": "周四", "fredag": "周五", "lørdag": "周六",
         "søndag": "周日"}[m.group(1).lower()]),
    (r"(?i)\b(mandag|tirsdag|onsdag|torsdag|fredag|lørdag|søndag)\b",
     lambda m: "周%s" % {
         "mandag": "一", "tirsdag": "二", "onsdag": "三",
         "torsdag": "四", "fredag": "五", "lørdag": "六",
         "søndag": "日"}[m.group(1).lower()]),
    (r"(?i)\b(?:man|tir|ons|tor|fre|lør|søn)\.?(?!\w)",
     lambda m: "周%s" % {
         "man": "一", "tir": "二", "ons": "三", "tor": "四",
         "fre": "五", "lør": "六", "søn": "日"}[
            m.group(0).lower().rstrip(".")]),
    (r"januar|jan\.?", "1月"),
    (r"februar|feb\.?", "2月"),
    (r"mars\.?|mars", "3月"),
    (r"april|apr\.?", "4月"),
    (r"mai", "5月"),
    (r"juni|jun\.?", "6月"),
    (r"juli|jul\.?", "7月"),
    (r"august|aug\.?", "8月"),
    (r"september|sept\.?|sep\.?", "9月"),
    (r"oktober|okt\.?", "10月"),
    (r"november|nov\.?", "11月"),
    (r"desember|des\.?", "12月"),
    (r"mandag", ""),
    (r"tirsdag", ""),
    (r"onsdag", ""),
    (r"torsdag", ""),
    (r"fredag", ""),
    (r"lørdag", ""),
    (r"søndag", ""),
    (r"(?i)\bi\s+morges\b", "今天 08:00 am"),
    (r"(?i)\bi\s+ettermiddag\b", "今天 15:00 pm"),
    (r"(?i)\bi\s+kveld\b", "今天 20:00 pm"),
    (r"(?i)\bi\s+natt\b", "今天 22:00 pm"),
    (r"(?i)\bi\s+morgen\s+tidlig\b", "明天 08:00 am"),
    (r"(?i)\bi\s+morgen\s+kveld\b", "明天 20:00 pm"),
    (r"(?i)\bi\s+går\s+kveld\b", "昨天 20:00 pm"),
    (r"(?i)\b(?:ved\s+)?middag(?:s)?tid\b", "12:00 pm"),
    (r"(?i)\bmidnatt\b", "12:00 am"),
    (r"(?P<num>\d+)\s*timer?\s+siden", lambda m: "%s小时前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*minutter?\s+siden", lambda m: "%s分钟前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*dager?\s+siden", lambda m: "%s天前" % int(m.group("num"))),
    (r"akkurat nå", "刚刚"),
    (r"i\s+forgårs\b", "前天"),
    (r"i\s+overmorgen\b", "后天"),
    (r"i dag", "今天"),
    (r"i går", "昨天"),
    (r"(?:i\s+)?morgen\b", "明天"),
    (r"om\s+(?P<num>\d+)\s*(?P<unit>sekunder?|minutter?|timer?|dager?|uker?|måneder?|år)",
     lambda m: "%s%s后" % (
         m.group("num"),
         {"sekund": "秒", "sekunder": "秒", "minutt": "分钟",
          "minutter": "分钟", "time": "小时", "timer": "小时",
          "dag": "天", "dager": "天", "uke": "周", "uker": "周",
          "måned": "月", "måneder": "月", "år": "年"}[
             m.group("unit").lower()])),
    (r"neste\s+uke\b", "下周"),
    (r"forrige\s+uke\b", "上周"),
    (r"neste\s+måned\b", "下个月"),
    (r"forrige\s+måned\b", "上个月"),
    (r"neste\s+år\b", "明年"),
    (r"forrige\s+år\b", "去年"),
]

FUZZY_REGEX_LIST = []
