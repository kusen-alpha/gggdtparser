# -*- coding:utf-8 -*-

"""
瑞典语
"""

ACCURATE_REGEX_LIST = []

SUB_TRANSLATE = [
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
    (r"(?P<num>\d+)\s*timmar?\s+sedan", lambda m: "%s小时前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*minuter?\s+sedan", lambda m: "%s分钟前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*dagar?\s+sedan", lambda m: "%s天前" % int(m.group("num"))),
    (r"just nu", "刚刚"),
    (r"idag", "今天"),
    (r"igår", "昨天"),
]

FUZZY_REGEX_LIST = []
