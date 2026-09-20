# -*- coding:utf-8 -*-

"""
荷兰语
"""

ACCURATE_REGEX_LIST = []

SUB_TRANSLATE = [
    (r"januari|jan\.?", "1月"),
    (r"februari|feb\.?", "2月"),
    (r"maart|mrt\.?", "3月"),
    (r"april|apr\.?", "4月"),
    (r"mei", "5月"),
    (r"juni|jun\.?", "6月"),
    (r"juli|jul\.?", "7月"),
    (r"augustus|aug\.?", "8月"),
    (r"september|sept?\.?", "9月"),
    (r"oktober|okt\.?", "10月"),
    (r"november|nov\.?", "11月"),
    (r"december|dec\.?", "12月"),
    (r"maandag", ""),
    (r"dinsdag", ""),
    (r"woensdag", ""),
    (r"donderdag", ""),
    (r"vrijdag", ""),
    (r"zaterdag", ""),
    (r"zondag", ""),
    (r"(?P<num>\d+)\s*uur\s+geleden", lambda m: "%s小时前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*minuten?\s+geleden", lambda m: "%s分钟前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*dagen?\s+geleden", lambda m: "%s天前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*weken?\s+geleden", lambda m: "%s周前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*maanden?\s+geleden", lambda m: "%s月前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*jaar\s+geleden", lambda m: "%s年前" % int(m.group("num"))),
    (r"zojuist|net", "刚刚"),
    (r"eergisteren", "前天"),
    (r"overmorgen", "后天"),
    (r"vandaag", "今天"),
    (r"gisteren", "昨天"),
    (r"morgen", "明天"),
    (r"over\s+(?P<num>\d+)\s*(?P<unit>seconde|seconden|minuut|minuten|uur|uren|dag|dagen|week|weken|maand|maanden|jaar|jaren)",
     lambda m: "%s%s后" % (
         m.group("num"),
         {"seconde": "秒", "seconden": "秒", "minuut": "分钟",
          "minuten": "分钟", "uur": "小时", "uren": "小时",
          "dag": "天", "dagen": "天", "week": "周", "weken": "周",
          "maand": "月", "maanden": "月", "jaar": "年",
          "jaren": "年"}[m.group("unit").lower()])),
    (r"(?P<num>\d+)\s*(?P<unit>seconde|seconden|minuut|minuten|uur|uren|dag|dagen|week|weken|maand|maanden|jaar|jaren)\s+later",
     lambda m: "%s%s后" % (
         m.group("num"),
         {"seconde": "秒", "seconden": "秒", "minuut": "分钟",
          "minuten": "分钟", "uur": "小时", "uren": "小时",
          "dag": "天", "dagen": "天", "week": "周", "weken": "周",
          "maand": "月", "maanden": "月", "jaar": "年",
          "jaren": "年"}[m.group("unit").lower()])),
    (r"volgende\s+week\b", "下周"),
    (r"vorige\s+week\b|afgelopen\s+week\b", "上周"),
    (r"volgende\s+maand\b", "下个月"),
    (r"vorige\s+maand\b|afgelopen\s+maand\b", "上个月"),
    (r"volgend\s+jaar\b", "明年"),
    (r"vorig\s+jaar\b|afgelopen\s+jaar\b", "去年"),
]

FUZZY_REGEX_LIST = []
