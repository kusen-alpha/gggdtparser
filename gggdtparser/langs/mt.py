# -*- coding:utf-8 -*-

"""
马耳他语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_MT_UNIT_MAP = {
    "sekonda": "秒", "sekondi": "秒",
    "minuta": "分钟", "minuti": "分钟",
    "siegħa": "小时", "sigħat": "小时",
    "ġurnata": "天", "ġranet": "天",
    "ġimgħa": "周", "ġimgħat": "周",
    "xahar": "月", "xhur": "月",
    "sena": "年", "snin": "年",
}
_MT_UNIT_RE = (
    r"sekond[ai]|minut[ai]|sigħat|siegħa|ġranet|ġurnat[ai]|"
    r"ġimgħat|ġimgħa|xahar|xhur|sena|snin"
)

_MT_WEEKDAYS = {
    "it-tnejn": "周一",
    "tnejn": "周一",
    "it-tlieta": "周二",
    "tlieta": "周二",
    "l-erbgħa": "周三",
    "erbgħa": "周三",
    "il-ħamis": "周四",
    "ħamis": "周四",
    "il-ġimgħa": "周五",
    "ġimgħa": "周五",
    "is-sibt": "周六",
    "sibt": "周六",
    "il-ħadd": "周日",
    "ħadd": "周日",
}
_MT_WEEKDAYS_RE = "|".join(sorted(_MT_WEEKDAYS, key=len, reverse=True))


def _mt_later(match):
    return "%s%s后" % (match.group("a"), _MT_UNIT_MAP[match.group("b")])


def _mt_earlier(match):
    return "%s%s前" % (match.group("a"), _MT_UNIT_MAP[match.group("b")])


SUB_TRANSLATE = [
    (r"(?i)\b(%s)\s+li\s+jmiss\b" % _MT_WEEKDAYS_RE,
     lambda m: "下%s" % _MT_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(%s)\s+li\s+għadd(?:a|iet)\b" % _MT_WEEKDAYS_RE,
     lambda m: "上%s" % _MT_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\bdan\s+(%s)\b" % _MT_WEEKDAYS_RE,
     lambda m: "这%s" % _MT_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\billum\s+filgħodu\b", "今天 08:00 am"),
    (r"(?i)\billum\s+wara\s+nofsinhar\b", "今天 15:00 pm"),
    (r"(?i)\billum\s+nofsinhar\b", "今天 12:00 pm"),
    (r"(?i)\billum\s+filgħaxija\b", "今天 20:00 pm"),
    (r"(?i)\billum\s+bil-lejl\b", "今天 22:00 pm"),
    (r"(?i)\bgħada\s+filgħodu\b", "明天 08:00 am"),
    (r"(?i)\bilbieraħ\s+filgħaxija\b", "昨天 20:00 pm"),
    (r"(?i)\bnofs\s+il-lejl\b", "12:00 am"),
    (r"(?i)\bnofsinhar\b", "12:00 pm"),
    (r"(?i)\bJannar\b", "1月"),
    (r"(?i)\bFrar\b", "2月"),
    (r"(?i)\bMarzu\b", "3月"),
    (r"(?i)\bApril\b", "4月"),
    (r"(?i)\bMejju\b", "5月"),
    (r"(?i)\bĠunju\b", "6月"),
    (r"(?i)\bLulju\b", "7月"),
    (r"(?i)\bAwwissu\b", "8月"),
    (r"(?i)\bSettembru\b", "9月"),
    (r"(?i)\bOttubru\b", "10月"),
    (r"(?i)\bNovembru\b", "11月"),
    (r"(?i)\bDiċembru\b", "12月"),
    (r"(?i)\bilbieraħ\s+ilbieraħ\b", "前天"),
    (r"(?i)\bpitgħada\b", "后天"),
    (r"(?i)\billum\b", "今天"),
    (r"(?i)\bilbieraħ\b", "昨天"),
    (r"(?i)\bgħada\b", "明天"),
    (r"(?i)\bissa\b", "刚刚"),
    (r"(?i)wara\s+(?P<a>\d+)\s*(?P<b>%s)" % _MT_UNIT_RE, _mt_later),
    (r"(?i)(?P<a>\d+)\s*(?P<b>%s)\s+ilu" % _MT_UNIT_RE, _mt_earlier),
    (r"(?i)il-ġimgħa\s+d-dieħla", "下周"),
    (r"(?i)il-ġimgħa\s+li\s+għaddiet", "上周"),
    (r"(?i)ix-xahar\s+id-dieħel", "下个月"),
    (r"(?i)ix-xahar\s+li\s+għadda", "上个月"),
    (r"(?i)is-sena\s+d-dieħla", "明年"),
    (r"(?i)is-sena\s+li\s+għaddiet", "去年"),
]

for _weekday in sorted(_MT_WEEKDAYS, key=len, reverse=True):
    SUB_TRANSLATE.append((r"(?i)\b%s\b" % _weekday,
                          _MT_WEEKDAYS[_weekday]))
