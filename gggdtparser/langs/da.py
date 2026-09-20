# -*- coding:utf-8 -*-

"""
丹麦语
"""

ACCURATE_REGEX_LIST = []

SUB_TRANSLATE = [
    (r"januar|jan\.?", "1月"),
    (r"februar|feb\.?", "2月"),
    (r"marts\.?|marts", "3月"),
    (r"april|apr\.?", "4月"),
    (r"maj", "5月"),
    (r"juni|jun\.?", "6月"),
    (r"juli|jul\.?", "7月"),
    (r"august|aug\.?", "8月"),
    (r"september|sept\.?", "9月"),
    (r"oktober|okt\.?", "10月"),
    (r"november|nov\.?", "11月"),
    (r"december|dec\.?", "12月"),
    (r"mandag", ""),
    (r"tirsdag", ""),
    (r"onsdag", ""),
    (r"torsdag", ""),
    (r"fredag", ""),
    (r"lørdag", ""),
    (r"søndag", ""),
    (r"(?P<num>\d+)\s*timer?\s+siden", lambda m: "%s小时前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*minutter?\s+siden", lambda m: "%s分钟前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*dage\s+siden", lambda m: "%s天前" % int(m.group("num"))),
    (r"lige nu", "刚刚"),
    (r"i\s+forgårs\b", "前天"),
    (r"i\s+overmorgen\b", "后天"),
    (r"i dag", "今天"),
    (r"i går", "昨天"),
    (r"(?:i\s+)?morgen\b", "明天"),
    (r"om\s+(?P<num>\d+)\s*(?P<unit>sekunder?|minutter?|timer?|dage|uger?|måneder?|år)",
     lambda m: "%s%s后" % (
         m.group("num"),
         {"sekund": "秒", "sekunder": "秒", "minut": "分钟",
          "minutter": "分钟", "time": "小时", "timer": "小时",
          "dag": "天", "dage": "天", "uge": "周", "uger": "周",
          "måned": "月", "måneder": "月", "år": "年"}[
             m.group("unit").lower()])),
    (r"næste\s+uge\b", "下周"),
    (r"sidste\s+uge\b", "上周"),
    (r"næste\s+måned\b", "下个月"),
    (r"sidste\s+måned\b", "上个月"),
    (r"næste\s+år\b", "明年"),
    (r"sidste\s+år\b", "去年"),
]

FUZZY_REGEX_LIST = []
