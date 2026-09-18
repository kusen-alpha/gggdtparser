# -*- coding:utf-8 -*-

"""
波兰语
"""

ACCURATE_REGEX_LIST = []

SUB_TRANSLATE = [
    (r"stycznia|styczeń|stycze?nia", "1月"),
    (r"lutego|luty|lut", "2月"),
    (r"marca|marzec|mar", "3月"),
    (r"kwietnia|kwiecień", "4月"),
    (r"maja|maj", "5月"),
    (r"czerwca|czerwiec", "6月"),
    (r"lipca|lipiec", "7月"),
    (r"sierpnia|sierpień", "8月"),
    (r"września|wrzesień", "9月"),
    (r"października|październik", "10月"),
    (r"listopada|listopad", "11月"),
    (r"grudnia|grudzień", "12月"),
    (r"poniedziałek|poniedział", ""),
    (r"wtorek|wtork", ""),
    (r"środa|środ|środe", ""),
    (r"czwartek|czwartk", ""),
    (r"piątek|piąt|piatek", ""),
    (r"sobota|sobot", ""),
    (r"niedziela|niedziel", ""),
    (r"(?P<num>\d+)\s*godzin[aiy]?\s*temu", lambda m: "%s小时前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*minut[aoy]?\s*temu", lambda m: "%s分钟前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*dni?\s*temu", lambda m: "%s天前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*tygodni\s*temu", lambda m: "%s周前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*miesięc[yi]?\s*temu", lambda m: "%s月前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*lat\s*temu", lambda m: "%s年前" % int(m.group("num"))),
    (r"przed chwilą|właśnie", "刚刚"),
    (r"dzisiaj|dziś", "今天"),
    (r"wczoraj", "昨天"),
]

FUZZY_REGEX_LIST = []
