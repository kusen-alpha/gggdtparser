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


def _eu_later(match):
    return "%s%s后" % (match.group("a"), _EU_UNIT_MAP[match.group("b")])


def _eu_earlier(match):
    return "%s%s前" % (match.group("a"), _EU_UNIT_MAP[match.group("b")])


SUB_TRANSLATE = [
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
