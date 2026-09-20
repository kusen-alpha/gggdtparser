# -*- coding:utf-8 -*-

"""
爱尔兰语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_GA_UNIT_MAP = {
    "soicind": "秒", "soicindí": "秒",
    "nóiméad": "分钟", "nóiméid": "分钟",
    "uair": "小时", "uaireanta": "小时",
    "lá": "天", "laethanta": "天",
    "seachtain": "周", "seachtainí": "周",
    "mí": "月", "míonna": "月",
    "bliain": "年", "blianta": "年",
}
_GA_UNIT_RE = (
    r"soicind(?:í)?|nóimé(?:ad|id)|uair(?:eanta)?|"
    r"l(?:á|aethanta)|seachtain(?:í)?|mí(?:onna)?|bliain|blianta"
)

_GA_WEEKDAYS = {
    "dé luain": "周一",
    "luan": "周一",
    "dé máirt": "周二",
    "máirt": "周二",
    "dé céadaoin": "周三",
    "céadaoin": "周三",
    "déardaoin": "周四",
    "dé haoine": "周五",
    "haoine": "周五",
    "dé sathairn": "周六",
    "sathairn": "周六",
    "dé domhnaigh": "周日",
    "domhnach": "周日",
}
_GA_WEEKDAYS_RE = "|".join(sorted(_GA_WEEKDAYS, key=len, reverse=True))


def _ga_later(match):
    return "%s%s后" % (match.group("a"), _GA_UNIT_MAP[match.group("b")])


def _ga_earlier(match):
    return "%s%s前" % (match.group("a"), _GA_UNIT_MAP[match.group("b")])


SUB_TRANSLATE = [
    (r"(?i)\b(%s)\s+seo\s+chugainn\b" % _GA_WEEKDAYS_RE,
     lambda m: "下%s" % _GA_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(%s)\s+seo\s+caite\b" % _GA_WEEKDAYS_RE,
     lambda m: "上%s" % _GA_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(%s)\s+seo\b" % _GA_WEEKDAYS_RE,
     lambda m: "这%s" % _GA_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\binniu\s+ar\s+maidin\b", "今天 08:00 am"),
    (r"(?i)\binniu\s+tráthnóna\b", "今天 15:00 pm"),
    (r"(?i)\banocht\b", "今天 22:00 pm"),
    (r"(?i)\bamárach\s+ar\s+maidin\b", "明天 08:00 am"),
    (r"(?i)\baréir\b", "昨天 22:00 pm"),
    (r"(?i)\bmeán\s+oíche\b", "12:00 am"),
    (r"(?i)\bmeán\s+lae\b", "12:00 pm"),
    (r"(?i)\bEanáir\b", "1月"),
    (r"(?i)\bFeabhra\b", "2月"),
    (r"(?i)\bMárta\b", "3月"),
    (r"(?i)\bAibreán\b", "4月"),
    (r"(?i)\bBealtaine\b", "5月"),
    (r"(?i)\bMeitheamh\b", "6月"),
    (r"(?i)\bIúil\b", "7月"),
    (r"(?i)\bLúnasa\b", "8月"),
    (r"(?i)\bMeán\s+Fómhair\b", "9月"),
    (r"(?i)\bDeireadh\s+Fómhair\b", "10月"),
    (r"(?i)\bSamhain\b", "11月"),
    (r"(?i)\bNollaig\b", "12月"),
    (r"(?i)\barú\s+inné\b", "前天"),
    (r"(?i)\barú\s+amárach\b", "后天"),
    (r"(?i)\binniu\b", "今天"),
    (r"(?i)\binné\b", "昨天"),
    (r"(?i)\bamárach\b", "明天"),
    (r"(?i)\b(?:anois|ar\s+an\s+toirt)\b", "刚刚"),
    (r"(?i)(?:i\s+gceann\s+|i\s+)(?P<a>\d+)\s*(?P<b>%s)" % _GA_UNIT_RE,
     _ga_later),
    (r"(?i)(?P<a>\d+)\s*(?P<b>%s)\s+ó\s+shin" % _GA_UNIT_RE, _ga_earlier),
    (r"(?i)an\s+tseachtain\s+seo\s+chugainn|an\s+tseachtain\s+chugainn",
     "下周"),
    (r"(?i)an\s+tseachtain\s+seo\s+caite|an\s+tseachtain\s+chaite", "上周"),
    (r"(?i)an\s+mhí\s+seo\s+chugainn|an\s+mhí\s+chugainn", "下个月"),
    (r"(?i)an\s+mhí\s+seo\s+caite", "上个月"),
    (r"(?i)an\s+bhliain\s+seo\s+chugainn|an\s+bhliain\s+chugainn", "明年"),
    (r"(?i)an\s+bhliain\s+seo\s+caite", "去年"),
]

for _weekday in sorted(_GA_WEEKDAYS, key=len, reverse=True):
    SUB_TRANSLATE.append((r"(?i)\b%s\b" % _weekday,
                          _GA_WEEKDAYS[_weekday]))
