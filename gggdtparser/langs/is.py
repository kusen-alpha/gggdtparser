# -*- coding:utf-8 -*-

"""
冰岛语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_IS_UNITS = {
    "sekúnda": "秒", "sekúndur": "秒",
    "mínúta": "分钟", "mínútur": "分钟", "mínútum": "分钟",
    "klukkustund": "小时", "klukkustundir": "小时", "klukkustundum": "小时",
    "dagur": "天", "daga": "天", "dögum": "天",
    "vika": "周", "vikur": "周", "vikum": "周",
    "mánuður": "月", "mánuði": "月", "mánuðum": "月",
    "ár": "年", "árum": "年",
}
_IS_UNIT_RE = (
    r"sekúnd[au]r?|mínútum|mínút[au]r?|klukkustund(?:ir|um)?|"
    r"dag(?:ur|a|ögum)|vik(?:a|ur|um)|mánuð(?:i|um)|ár(?:um)?"
)


def _is_later(match):
    return "%s%s后" % (match.group(1), _IS_UNITS[match.group(2)])


def _is_earlier(match):
    return "%s%s前" % (match.group(1), _IS_UNITS[match.group(2)])


SUB_TRANSLATE = [
    (r"\bjanúar\b", "1月"),
    (r"\bfebrúar\b", "2月"),
    (r"\bmars\b", "3月"),
    (r"\bapríl\b", "4月"),
    (r"\bmaí\b", "5月"),
    (r"\bjúní\b", "6月"),
    (r"\bjúlí\b", "7月"),
    (r"\bágúst\b", "8月"),
    (r"\bseptember\b", "9月"),
    (r"\boktóber\b", "10月"),
    (r"\bnóvember\b", "11月"),
    (r"\bdesember\b", "12月"),
    (r"\bí\s+fyrradag\b", "前天"),
    (r"\bhinn\s+daginn\b", "后天"),
    (r"\bí\s+dag\b", "今天"),
    (r"\bí\s+gær\b", "昨天"),
    (r"\bá\s+morgun\b", "明天"),
    (r"eftir\s+(?P<a>\d+)\s*(?P<b>%s)" % _IS_UNIT_RE, _is_later),
    (r"fyrir\s+(?P<a>\d+)\s*(?P<b>%s)" % _IS_UNIT_RE, _is_earlier),
    (r"\b(?:núna|í\s+bessu)\b", "刚刚"),
    (r"\bnæstu\s+viku\b", "下周"),
    (r"\bsíðustu\s+viku\b", "上周"),
    (r"\bnæsta\s+mánuði\b", "下个月"),
    (r"\bsíðasta\s+mánuði\b", "上个月"),
    (r"\bnæsta\s+ári\b", "明年"),
    (r"\bsíðasta\s+ári\b", "去年"),
]
