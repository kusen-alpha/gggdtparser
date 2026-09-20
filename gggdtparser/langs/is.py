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

_IS_WEEKDAYS = {
    "mánudagur": "周一", "mánudag": "周一",
    "þriðjudagur": "周二", "þriðjudag": "周二",
    "miðvikudagur": "周三", "miðvikudag": "周三",
    "fimmtudagur": "周四", "fimmtudag": "周四",
    "föstudagur": "周五", "föstudag": "周五",
    "laugardagur": "周六", "laugardag": "周六",
    "sunnudagur": "周日", "sunnudag": "周日",
}


def _is_later(match):
    return "%s%s后" % (match.group(1), _IS_UNITS[match.group(2)])


def _is_earlier(match):
    return "%s%s前" % (match.group(1), _IS_UNITS[match.group(2)])


SUB_TRANSLATE = [
    (r"(?i)\b(?:næsti|næsta)\s+(mánudagur|mánudag|þriðjudagur|þriðjudag|miðvikudagur|miðvikudag|fimmtudagur|fimmtudag|föstudagur|föstudag|laugardagur|laugardag|sunnudagur|sunnudag)\b",
     lambda m: "下%s" % _IS_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(?:síðasti|síðasta|liðinn)\s+(mánudagur|mánudag|þriðjudagur|þriðjudag|miðvikudagur|miðvikudag|fimmtudagur|fimmtudag|föstudagur|föstudag|laugardagur|laugardag|sunnudagur|sunnudag)\b",
     lambda m: "上%s" % _IS_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(?:þessi|þennan)\s+(mánudagur|mánudag|þriðjudagur|þriðjudag|miðvikudagur|miðvikudag|fimmtudagur|fimmtudag|föstudagur|föstudag|laugardagur|laugardag|sunnudagur|sunnudag)\b",
     lambda m: "这%s" % _IS_WEEKDAYS[m.group(1).lower()]),
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
    (r"(?i)\bí\s+morgun\b", "今天 08:00 am"),
    (r"(?i)\beftir\s+hádegi\b", "今天 15:00 pm"),
    (r"(?i)\bí\s+kvöld\b", "今天 20:00 pm"),
    (r"(?i)\bí\s+nótt\b", "今天 22:00 pm"),
    (r"(?i)\bí\s+fyrramálið\b", "明天 08:00 am"),
    (r"(?i)\bá\s+morgun\s+í\s+kvöld\b", "明天 20:00 pm"),
    (r"(?i)\bí\s+gærkvöldi\b", "昨天 20:00 pm"),
    (r"(?i)\bhádegi\b", "12:00 pm"),
    (r"(?i)\bmiðnætti\b", "12:00 am"),
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
