# -*- coding:utf-8 -*-

"""
巴斯克语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_EU_UNIT_MAP = {
    "segundo": "秒", "minutu": "分钟", "ordu": "小时",
    "egun": "天", "aste": "周", "hilabete": "月", "urte": "年",
}
_EU_UNIT_RE = (
    r"segundo|minutu|ordu|egun|aste|hilabete|urte"
)

_EU_WEEKDAYS = {
    "astelehena": "周一",
    "asteartea": "周二",
    "asteazkena": "周三",
    "osteguna": "周四",
    "ostirala": "周五",
    "larunbata": "周六",
    "igandea": "周日",
}
_EU_WEEKDAYS_RE = "|".join(sorted(_EU_WEEKDAYS, key=len, reverse=True))
_EU_WEEKDAYS_BASE = {
    "astelehen": "周一",
    "astearte": "周二",
    "asteazken": "周三",
    "ostegun": "周四",
    "ostiral": "周五",
    "larunbat": "周六",
    "igande": "周日",
}
_EU_WEEKDAYS_BASE_RE = "|".join(
    sorted(_EU_WEEKDAYS_BASE, key=len, reverse=True))


def _eu_later(match):
    return "%s%s后" % (match.group("a"), _EU_UNIT_MAP[match.group("b")])


def _eu_earlier(match):
    return "%s%s前" % (match.group("a"), _EU_UNIT_MAP[match.group("b")])


SUB_TRANSLATE = [
    (r"(?i)\b(?:datorren|hurrengo)\s+(%s)\b" % _EU_WEEKDAYS_RE,
     lambda m: "下%s" % _EU_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(?:joan\s+den|aurreko)\s+(%s)\b" % _EU_WEEKDAYS_RE,
     lambda m: "上%s" % _EU_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(%s)\s+honetan\b" % _EU_WEEKDAYS_BASE_RE,
     lambda m: "这%s" % _EU_WEEKDAYS_BASE[m.group(1).lower()]),
    (r"(?i)\bgaur\s+goizean\b", "今天 08:00 am"),
    (r"(?i)\bgaur\s+eguerdian\b", "今天 12:00 pm"),
    (r"(?i)\bgaur\s+arratsaldean\b", "今天 15:00 pm"),
    (r"(?i)\bgaur\s+gauean\b", "今天 22:00 pm"),
    (r"(?i)\bbihar\s+goizean\b", "明天 08:00 am"),
    (r"(?i)\batzo\s+gauean\b", "昨天 22:00 pm"),
    (r"(?i)\bgauerdia\b", "12:00 am"),
    (r"(?i)\beguerdia\b", "12:00 pm"),
    (r"(?i)\burtarril(?:a)?\b", "1月"),
    (r"(?i)\botsail(?:a)?\b", "2月"),
    (r"(?i)\bmartxo(?:a)?\b", "3月"),
    (r"(?i)\bapiril(?:a)?\b", "4月"),
    (r"(?i)\bmaiatz(?:a)?\b", "5月"),
    (r"(?i)\bekain(?:a)?\b", "6月"),
    (r"(?i)\buztail(?:a)?\b", "7月"),
    (r"(?i)\babuztu(?:a)?\b", "8月"),
    (r"(?i)\birail(?:a)?\b", "9月"),
    (r"(?i)\burri(?:a)?\b", "10月"),
    (r"(?i)\bazaro(?:a)?\b", "11月"),
    (r"(?i)\babendu(?:a)?\b", "12月"),
    (r"(?i)\bherenegun\b", "前天"),
    (r"(?i)\betzi\b", "后天"),
    (r"(?i)\bgaur\b", "今天"),
    (r"(?i)\batzo\b", "昨天"),
    (r"(?i)\bbihar\b", "明天"),
    (r"(?i)\borain\b", "刚刚"),
    (r"(?i)(?P<a>\d+)\s*(?P<b>%s)(?:k|tan|an|ren)?\s+(?:barru|gero)"
     % _EU_UNIT_RE, _eu_later),
    (r"(?i)duela\s+(?P<a>\d+)\s*(?P<b>%s)(?:k)?"
     % _EU_UNIT_RE, _eu_earlier),
    (r"(?i)(?P<a>\d+)\s*(?P<b>%s)(?:k|tan|an|ren)" % _EU_UNIT_RE,
     _eu_later),
    (r"(?i)datorren\s+astea|hurrengo\s+astea", "下周"),
    (r"(?i)joan\s+den\s+astea|aurreko\s+astea", "上周"),
    (r"(?i)datorren\s+hilabetea|hurrengo\s+hilabetea", "下个月"),
    (r"(?i)joan\s+den\s+hilabetea|aurreko\s+hilabetea", "上个月"),
    (r"(?i)datorren\s+urtea|hurrengo\s+urtea", "明年"),
    (r"(?i)joan\s+den\s+urtea|aurreko\s+urtea", "去年"),
]

for _weekday in sorted(_EU_WEEKDAYS, key=len, reverse=True):
    SUB_TRANSLATE.append((r"(?i)\b%s\b" % _weekday,
                          _EU_WEEKDAYS[_weekday]))
for _weekday in sorted(_EU_WEEKDAYS_BASE, key=len, reverse=True):
    SUB_TRANSLATE.append((r"(?i)\b%s\b" % _weekday,
                          _EU_WEEKDAYS_BASE[_weekday]))
