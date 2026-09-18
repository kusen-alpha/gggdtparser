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
    (r"i dag", "今天"),
    (r"i går", "昨天"),
]

FUZZY_REGEX_LIST = []
