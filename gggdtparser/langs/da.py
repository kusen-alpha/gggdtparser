# -*- coding:utf-8 -*-

"""
丹麦语
"""

ACCURATE_REGEX_LIST = []

SUB_TRANSLATE = [
    (r"(?i)\b(?:næste|kommende)\s+(mandag|tirsdag|onsdag|torsdag|fredag|lørdag|søndag)\b",
     lambda m: "下%s" % {
         "mandag": "周一", "tirsdag": "周二", "onsdag": "周三",
         "torsdag": "周四", "fredag": "周五", "lørdag": "周六",
         "søndag": "周日"}[m.group(1).lower()]),
    (r"(?i)\bsidste\s+(mandag|tirsdag|onsdag|torsdag|fredag|lørdag|søndag)\b",
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
    (r"marts\.?|marts", "3月"),
    (r"april|apr\.?", "4月"),
    (r"maj", "5月"),
    (r"juni|jun\.?", "6月"),
    (r"juli|jul\.?", "7月"),
    (r"august|aug\.?", "8月"),
    (r"september|sept\.?|sep\.?", "9月"),
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
    (r"(?i)\bi\s+morges\b", "今天 08:00 am"),
    (r"(?i)\bi\s+eftermiddags\b", "今天 15:00 pm"),
    (r"(?i)\bi\s+aften\b", "今天 20:00 pm"),
    (r"(?i)\bi\s+nat\b", "今天 22:00 pm"),
    (r"(?i)\bi\s+morgen\s+tidlig\b", "明天 08:00 am"),
    (r"(?i)\bi\s+morgen\s+aften\b", "明天 20:00 pm"),
    (r"(?i)\bi\s+går\s+aftes\b", "昨天 20:00 pm"),
    (r"(?i)\bher\s+til\s+morgen\b", "今天 08:00 am"),
    (r"(?i)\bher\s+til\s+formiddag\b", "今天 08:00 am"),
    (r"(?i)\bher\s+til\s+middag\b", "今天 12:00 pm"),
    (r"(?i)\bher\s+til\s+eftermiddag\b", "今天 15:00 pm"),
    (r"(?i)\bher\s+til\s+aften\b", "今天 20:00 pm"),
    (r"(?i)\b(?:ved\s+)?middag(?:s)?tid\b", "12:00 pm"),
    (r"(?i)\bmidnat\b", "12:00 am"),
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
