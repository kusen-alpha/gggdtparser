# -*- coding:utf-8 -*-

"""
挪威语(博克马尔/新挪威语共用词形)
"""

ACCURATE_REGEX_LIST = []

SUB_TRANSLATE = [
    (r"januar|jan\.?", "1月"),
    (r"februar|feb\.?", "2月"),
    (r"mars\.?|mars", "3月"),
    (r"april|apr\.?", "4月"),
    (r"mai", "5月"),
    (r"juni|jun\.?", "6月"),
    (r"juli|jul\.?", "7月"),
    (r"august|aug\.?", "8月"),
    (r"september|sept\.?", "9月"),
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
