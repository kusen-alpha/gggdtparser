# -*- coding:utf-8 -*-

"""
瑞典语
"""

ACCURATE_REGEX_LIST = []

SUB_TRANSLATE = [
    (r"(?i)\b(?:nästa|kommande)\s+(måndag|tisdag|onsdag|torsdag|fredag|lördag|söndag)\b",
     lambda m: "下%s" % {
         "måndag": "周一", "tisdag": "周二", "onsdag": "周三",
         "torsdag": "周四", "fredag": "周五", "lördag": "周六",
         "söndag": "周日"}[m.group(1).lower()]),
    (r"(?i)\bförra\s+(måndag|tisdag|onsdag|torsdag|fredag|lördag|söndag)\b",
     lambda m: "上%s" % {
         "måndag": "周一", "tisdag": "周二", "onsdag": "周三",
         "torsdag": "周四", "fredag": "周五", "lördag": "周六",
         "söndag": "周日"}[m.group(1).lower()]),
    (r"(?i)\b(?:denna|den\s+här)\s+(måndag|tisdag|onsdag|torsdag|fredag|lördag|söndag)\b",
     lambda m: "这%s" % {
         "måndag": "周一", "tisdag": "周二", "onsdag": "周三",
         "torsdag": "周四", "fredag": "周五", "lördag": "周六",
         "söndag": "周日"}[m.group(1).lower()]),
    (r"januari|jan\.?", "1月"),
    (r"februari|feb\.?", "2月"),
    (r"mars", "3月"),
    (r"april|apr\.?", "4月"),
    (r"maj", "5月"),
    (r"juni|jun\.?", "6月"),
    (r"juli|jul\.?", "7月"),
    (r"augusti|aug\.?", "8月"),
    (r"september|sept\.?", "9月"),
    (r"oktober|okt\.?", "10月"),
    (r"november|nov\.?", "11月"),
    (r"december|dec\.?", "12月"),
    (r"måndag", ""),
    (r"tisdag", ""),
    (r"onsdag", ""),
    (r"torsdag", ""),
    (r"fredag", ""),
    (r"lördag", ""),
    (r"söndag", ""),
    (r"(?i)\bi\s+morse\b", "今天 08:00 am"),
    (r"(?i)\bi\s+eftermiddags\b", "今天 15:00 pm"),
    (r"(?i)\bikväll\b|\bi\s+kväll\b", "今天 20:00 pm"),
    (r"(?i)\binatt\b|\bi\s+natt\b", "今天 22:00 pm"),
    (r"(?i)\b(?:imorgon|i\s+morgon)\s+bitti\b", "明天 08:00 am"),
    (r"(?i)\b(?:imorgon|i\s+morgon)\s+kväll\b", "明天 20:00 pm"),
    (r"(?i)\bigår\s+kväll\b|\bigårkväll\b", "昨天 20:00 pm"),
    (r"(?i)\b(?:vid\s+)?lunch(?:tid)?\b|\bvid\s+middag\b", "12:00 pm"),
    (r"(?i)\bmidnatt\b", "12:00 am"),
    (r"(?P<num>\d+)\s*timmar?\s+sedan", lambda m: "%s小时前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*minuter?\s+sedan", lambda m: "%s分钟前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*dagar?\s+sedan", lambda m: "%s天前" % int(m.group("num"))),
    (r"just nu", "刚刚"),
    (r"i\s+förrgår\b", "前天"),
    (r"i\s+övermorgon\b", "后天"),
    (r"idag", "今天"),
    (r"igår", "昨天"),
    (r"(?:imorgon|i\s+morgon)", "明天"),
    (r"om\s+(?P<num>\d+)\s*(?P<unit>sekunder?|minuter?|timmar?|dagar?|veckor?|månader?|år)",
     lambda m: "%s%s后" % (
         m.group("num"),
         {"sekund": "秒", "sekunder": "秒", "minut": "分钟",
          "minuter": "分钟", "timme": "小时", "timmar": "小时",
          "dag": "天", "dagar": "天", "vecka": "周", "veckor": "周",
          "månad": "月", "månader": "月", "år": "年"}[
             m.group("unit").lower()])),
    (r"nästa\s+vecka\b", "下周"),
    (r"förra\s+veckan\b", "上周"),
    (r"nästa\s+månad\b", "下个月"),
    (r"förra\s+månaden\b", "上个月"),
    (r"nästa\s+år\b", "明年"),
    (r"förra\s+året\b", "去年"),
]

FUZZY_REGEX_LIST = []
