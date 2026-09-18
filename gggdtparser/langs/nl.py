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
    (r"vandaag", "今天"),
    (r"gisteren", "昨天"),
]

FUZZY_REGEX_LIST = []
