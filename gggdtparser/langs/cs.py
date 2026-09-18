# -*- coding:utf-8 -*-

"""
捷克语
"""

ACCURATE_REGEX_LIST = []

SUB_TRANSLATE = [
    (r"ledna|leden|led", "1月"),
    (r"února|únor|úno", "2月"),
    (r"března|březen|bře", "3月"),
    (r"dubna|duben|dub", "4月"),
    (r"května|květen|kvě", "5月"),
    (r"června|červen|čer", "6月"),
    (r"července|červenec", "7月"),
    (r"srpna|srpen|srp", "8月"),
    (r"září", "9月"),
    (r"října|říjen", "10月"),
    (r"listopadu|listopad", "11月"),
    (r"prosince|prosinec|pros", "12月"),
    (r"pondělí", ""),
    (r"úterý|úter", ""),
    (r"středa|střed", ""),
    (r"čtvrtek|čtvrtk", ""),
    (r"pátek|pátk", ""),
    (r"sobota|sobot", ""),
    (r"neděle|neděl", ""),
    (r"(?P<num>\d+)\s*hodinami?\s*zpět", lambda m: "%s小时前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*minutami?\s*zpět", lambda m: "%s分钟前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*dny?\s*zpět", lambda m: "%s天前" % int(m.group("num"))),
    (r"právě teď", "刚刚"),
    (r"dnes", "今天"),
    (r"včera", "昨天"),
]

FUZZY_REGEX_LIST = []
