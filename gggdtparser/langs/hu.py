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
    (r"tegnapelőtt", "前天"),
    (r"holnapután", "后天"),
    (r"ma", "今天"),
    (r"tegnap", "昨天"),
    (r"holnap", "明天"),
    (r"(?P<num>\d+)\s*(?P<unit>másodperc[ei]?|perc[ei]?|óra\s+múlva|órával\s+később|nap\s+múlva|hét\s+múlva|hónap\s+múlva|év\s+múlva)",
     lambda m: "%s%s后" % (
         m.group("num"),
         {"másodperc": "秒", "másodpercek": "秒", "másodperce": "秒",
          "perc": "分钟", "percek": "分钟", "perce": "分钟",
          "óra múlva": "小时", "órával később": "小时",
          "nap múlva": "天", "hét múlva": "周", "hónap múlva": "月",
          "év múlva": "年"}[m.group("unit")])),
    (r"jövő\s+héten\b|a\s+következő\s+hét\b", "下周"),
    (r"múlt\s+héten\b|az\s+előző\s+hét\b", "上周"),
    (r"jövő\s+hónapban\b|a\s+következő\s+hónap\b", "下个月"),
    (r"múlt\s+hónapban\b|az\s+előző\s+hónap\b", "上个月"),
    (r"jövő\s+évben\b|a\s+következő\s+év\b", "明年"),
    (r"múlt\s+évben\b|az\s+előző\s+év\b", "去年"),
]

FUZZY_REGEX_LIST = []
