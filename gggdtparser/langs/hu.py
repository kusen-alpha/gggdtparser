# -*- coding:utf-8 -*-

"""
匈牙利语
"""

ACCURATE_REGEX_LIST = []

SUB_TRANSLATE = [
    (r"(?i)(?:jövő|a\s+következő)\s+(hétfőn|kedden|szerdán|csütörtökön|pénteken|szombaton|vasárnap|hétfő|kedd|szerda|csütörtök|péntek|szombat|vasárnap)\b",
     lambda m: "下%s" % {
         "hétfő": "周一", "hétfőn": "周一", "kedd": "周二",
         "kedden": "周二", "szerda": "周三", "szerdán": "周三",
         "csütörtök": "周四", "csütörtökön": "周四", "péntek": "周五",
         "pénteken": "周五", "szombat": "周六", "szombaton": "周六",
         "vasárnap": "周日"}[m.group(1).lower()]),
    (r"(?i)múlt\s+(hétfőn|kedden|szerdán|csütörtökön|pénteken|szombaton|vasárnap|hétfő|kedd|szerda|csütörtök|péntek|szombat|vasárnap)\b",
     lambda m: "上%s" % {
         "hétfő": "周一", "hétfőn": "周一", "kedd": "周二",
         "kedden": "周二", "szerda": "周三", "szerdán": "周三",
         "csütörtök": "周四", "csütörtökön": "周四", "péntek": "周五",
         "pénteken": "周五", "szombat": "周六", "szombaton": "周六",
         "vasárnap": "周日"}[m.group(1).lower()]),
    (r"(?i)(?:ez\s+(?:a|az)\s+|ezen\s+(?:a|az)\s+)(hétfőn|kedden|szerdán|csütörtökön|pénteken|szombaton|vasárnap|hétfő|kedd|szerda|csütörtök|péntek|szombat|vasárnap)\b",
     lambda m: "这%s" % {
         "hétfő": "周一", "hétfőn": "周一", "kedd": "周二",
         "kedden": "周二", "szerda": "周三", "szerdán": "周三",
         "csütörtök": "周四", "csütörtökön": "周四", "péntek": "周五",
         "pénteken": "周五", "szombat": "周六", "szombaton": "周六",
         "vasárnap": "周日"}[m.group(1).lower()]),
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
    (r"ma\s+reggel", "今天 08:00 am"),
    (r"délben", "12:00 pm"),
    (r"ma\s+este", "今天 20:00 pm"),
    (r"holnap\s+reggel", "明天 08:00 am"),
    (r"holnap\s+este", "明天 20:00 pm"),
    (r"tegnap\s+este", "昨天 20:00 pm"),
    (r"éjfélkor", "12:00 am"),
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
