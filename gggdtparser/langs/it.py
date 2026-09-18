# -*- coding:utf-8 -*-

"""
意大利语
"""

ACCURATE_REGEX_LIST = []

SUB_TRANSLATE = [
    (r"gennaio|gen\.?", "1月"),
    (r"febbraio|feb\.?", "2月"),
    (r"marzo|mar\.?", "3月"),
    (r"aprile|apr\.?", "4月"),
    (r"maggio|mag\.?", "5月"),
    (r"giugno|giu\.?", "6月"),
    (r"luglio|lug\.?", "7月"),
    (r"agosto|ago\.?", "8月"),
    (r"settembre|set\.?", "9月"),
    (r"ottobre|ott\.?", "10月"),
    (r"novembre|nov\.?", "11月"),
    (r"dicembre|dic\.?", "12月"),
    (r"lunedì|lunedi|luned", ""),
    (r"martedì|martedi|marted", ""),
    (r"mercoledì|mercoledi|mercoled", ""),
    (r"giovedì|giovedi|gioved", ""),
    (r"venerdì|venerdi|venerd", ""),
    (r"sabato|sabat", ""),
    (r"domenica|domenic", ""),
    (r"(?P<num>\d+)\s*ore?\s*fa", lambda m: "%s小时前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*minut[ie]?\s*fa", lambda m: "%s分钟前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*giorn[io]\s*fa", lambda m: "%s天前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*settiman[ae]\s*fa", lambda m: "%s周前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*m[ei]si?\s*fa", lambda m: "%s月前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*anni?\s*fa", lambda m: "%s年前" % int(m.group("num"))),
    (r"adesso|ora", "刚刚"),
    (r"oggi", "今天"),
    (r"ieri", "昨天"),
]

FUZZY_REGEX_LIST = []
