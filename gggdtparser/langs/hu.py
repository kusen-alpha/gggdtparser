# -*- coding:utf-8 -*-

"""
匈牙利语
"""

ACCURATE_REGEX_LIST = []

SUB_TRANSLATE = [
    (r"január\.?", "1月"),
    (r"február\.?", "2月"),
    (r"március\.?", "3月"),
    (r"április\.?", "4月"),
    (r"május\.?", "5月"),
    (r"június\.?", "6月"),
    (r"július\.?", "7月"),
    (r"augusztus\.?", "8月"),
    (r"szeptember\.?", "9月"),
    (r"október\.?", "10月"),
    (r"november\.?", "11月"),
    (r"december\.?", "12月"),
    (r"hétfő", ""),
    (r"kedd", ""),
    (r"szerda", ""),
    (r"csütörtök", ""),
    (r"péntek", ""),
    (r"szombat", ""),
    (r"vasárnap", ""),
    (r"(?P<num>\d+)\s*órája", lambda m: "%s小时前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*perce", lambda m: "%s分钟前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*napja", lambda m: "%s天前" % int(m.group("num"))),
    (r"most", "刚刚"),
    (r"ma", "今天"),
    (r"tegnap", "昨天"),
]

FUZZY_REGEX_LIST = []
