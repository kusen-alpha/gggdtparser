# -*- coding:utf-8 -*-

"""
卢森堡语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_LB_UNIT_MAP = {
    "Sekonn": "秒", "Sekonnen": "秒",
    "Minutt": "分钟", "Minutten": "分钟",
    "Stonn": "小时", "Stonnen": "小时",
    "Dag": "天", "Deeg": "天",
    "Woch": "周", "Wochen": "周",
    "Mount": "月", "Méint": "月",
    "Joer": "年",
}
_LB_UNIT_RE = (
    r"Sekonn(?:en)?|Minutt(?:en)?|Stonn(?:en)?|Dag|Deeg|"
    r"Woch(?:en)?|Mount|Méint|Joer"
)

_LB_WEEKDAYS = {
    "méindeg": "周一",
    "dënschdeg": "周二",
    "mëttwoch": "周三",
    "donneschdeg": "周四",
    "freideg": "周五",
    "samschdeg": "周六",
    "sonndeg": "周日",
}
_LB_WEEKDAYS_RE = "|".join(sorted(_LB_WEEKDAYS, key=len, reverse=True))


def _lb_later(match):
    return "%s%s后" % (match.group("a"), _LB_UNIT_MAP[match.group("b")])


def _lb_earlier(match):
    return "%s%s前" % (match.group("a"), _LB_UNIT_MAP[match.group("b")])


SUB_TRANSLATE = [
    (r"(?i)\bnächste(?:n|r)?\s+(%s)\b" % _LB_WEEKDAYS_RE,
     lambda m: "下%s" % _LB_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\blescht(?:e|en)?\s+(%s)\b" % _LB_WEEKDAYS_RE,
     lambda m: "上%s" % _LB_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\bdëse(?:n|r)?\s+(%s)\b" % _LB_WEEKDAYS_RE,
     lambda m: "这%s" % _LB_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\bhaut\s+moies\b", "今天 08:00 am"),
    (r"(?i)\bhaut\s+mëttes\b", "今天 12:00 pm"),
    (r"(?i)\bhaut\s+nomëttes\b", "今天 15:00 pm"),
    (r"(?i)\bhaut\s+owes\b", "今天 20:00 pm"),
    (r"(?i)\bhaut\s+an\s+der\s+nuecht\b", "今天 22:00 pm"),
    (r"(?i)\bmuer\s+moies\b", "明天 08:00 am"),
    (r"(?i)\bgëschter\s+owes\b", "昨天 20:00 pm"),
    (r"(?i)\bmëtternuecht\b", "12:00 am"),
    (r"(?i)\bJanuar\b", "1月"),
    (r"(?i)\bFebruar\b", "2月"),
    (r"(?i)\bMäerz\b", "3月"),
    (r"(?i)\bAbrëll\b", "4月"),
    (r"(?i)\bMee\b", "5月"),
    (r"(?i)\bJuni\b", "6月"),
    (r"(?i)\bJuli\b", "7月"),
    (r"(?i)\bAugust\b", "8月"),
    (r"(?i)\bSeptember\b", "9月"),
    (r"(?i)\bOktober\b", "10月"),
    (r"(?i)\bNovember\b", "11月"),
    (r"(?i)\bDezember\b", "12月"),
    (r"(?i)\bvirgëschter\b", "前天"),
    (r"(?i)\biwwermuer\b", "后天"),
    (r"(?i)\bhaut\b", "今天"),
    (r"(?i)\bgëschter\b", "昨天"),
    (r"(?i)\bmuer\b", "明天"),
    (r"(?i)\belo\b", "刚刚"),
    (r"(?i)(?:an|bannen)\s+(?P<a>\d+)\s*(?P<b>%s)" % _LB_UNIT_RE,
     _lb_later),
    (r"(?i)virun\s+(?P<a>\d+)\s*(?P<b>%s)" % _LB_UNIT_RE, _lb_earlier),
    (r"(?i)nächste\s+Woch", "下周"),
    (r"(?i)lescht\s+Woch", "上周"),
    (r"(?i)nächste\s+Mount", "下个月"),
    (r"(?i)leschte\s+Mount", "上个月"),
    (r"(?i)nächst\s+Joer", "明年"),
    (r"(?i)lescht\s+Joer", "去年"),
]

for _weekday in sorted(_LB_WEEKDAYS, key=len, reverse=True):
    SUB_TRANSLATE.append((r"(?i)\b%s\b" % _weekday, _LB_WEEKDAYS[_weekday]))
