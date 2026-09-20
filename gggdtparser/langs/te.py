# -*- coding:utf-8 -*-


"""
泰卢固语
"""

_TE_DIGITS = str.maketrans("౦౧౨౩౪౫౬౭౮౯", "0123456789")

_TE_MONTHS = {
    "జనవరి": "1月",
    "ఫిబ్రవరి": "2月",
    "మార్చి": "3月",
    "ఏప్రిల్": "4月",
    "మే": "5月",
    "జూన్": "6月",
    "జూలై": "7月",
    "ఆగస్టు": "8月",
    "సెప్టెంబర్": "9月",
    "సెప్టెంబరు": "9月",
    "అక్టోబర్": "10月",
    "నవంబర్": "11月",
    "డిసెంబర్": "12月",
}

_TE_MONTHS_RE = "|".join(sorted(_TE_MONTHS, key=len, reverse=True))

_TE_WEEKDAYS = {
    "సోమవారం": "周一",
    "సోమవారము": "周一",
    "మంగళవారం": "周二",
    "మంగళవారము": "周二",
    "బుధవారం": "周三",
    "బుధవారము": "周三",
    "గురువారం": "周四",
    "గురువారము": "周四",
    "శుక్రవారం": "周五",
    "శుక్రవారము": "周五",
    "శనివారం": "周六",
    "శనివారము": "周六",
    "ఆదివారం": "周日",
    "ఆదివారము": "周日",
}

_TE_WEEKDAYS_RE = "|".join(sorted(_TE_WEEKDAYS, key=len, reverse=True))


def _to_ascii(value):
    return value.translate(_TE_DIGITS)


def _numeric_date(match):
    return "%s/%s/%s" % (
        _to_ascii(match.group("Y")),
        _to_ascii(match.group("m")),
        _to_ascii(match.group("d")),
    )


def _named_date(match):
    day = _to_ascii(match.group("d"))
    year = _to_ascii(match.group("Y"))
    return "%s %s %s" % (day, _TE_MONTHS[match.group("name")], year)


SUB_TRANSLATE = [
    (r"(?:వచ్చే|రాబోయే|తర్వాతి)\s+(%s)" % _TE_WEEKDAYS_RE,
     lambda m: "下%s" % _TE_WEEKDAYS[m.group(1)]),
    (r"(?:గత|మునుపటి|వెళ్లిన)\s+(%s)" % _TE_WEEKDAYS_RE,
     lambda m: "上%s" % _TE_WEEKDAYS[m.group(1)]),
    (r"ఈ\s+(%s)" % _TE_WEEKDAYS_RE,
     lambda m: "这%s" % _TE_WEEKDAYS[m.group(1)]),
    (r"ఈ\s+ఉదయం", "今天 08:00 am"),
    (r"ఈ\s+మధ్యాహ్నం", "今天 12:00 pm"),
    (r"ఈ\s+సాయంత్రం", "今天 20:00 pm"),
    (r"ఈ\s+రాత్రి", "今天 22:00 pm"),
    (r"రేపు\s+ఉదయం", "明天 08:00 am"),
    (r"నిన్న\s+రాత్రి", "昨天 22:00 pm"),
    (r"అర్ధరాత్రి", "12:00 am"),
    (r"(?<!\d)(?P<Y>[౦-౯]{4})[\-\/\.]\s*(?P<m>[౦-౯]{1,2})[\-\/\.]\s*(?P<d>[౦-౯]{1,2})(?!\d)",
     _numeric_date),
    (r"(?P<d>[౦-౯]{1,2}|\d{1,2})\s*(?P<name>%s)\s*(?P<Y>[౦-౯]{4}|\d{4})"
     % _TE_MONTHS_RE, _named_date),
    (r"(?P<name>%s)\s*(?P<d>[౦-౯]{1,2}|\d{1,2})[,\s]+\s*(?P<Y>[౦-౯]{4}|\d{4})"
     % _TE_MONTHS_RE, _named_date),
    (r"(?P<name>%s)\s*(?P<Y>[౦-౯]{4})" % _TE_MONTHS_RE,
     lambda m: "%s %s" % (_TE_MONTHS[m.group("name")], _to_ascii(m.group("Y")))),
    (r"మొన్న", "前天"),
    (r"ఎల్లుండి", "后天"),
    (r"నిన్న", "昨天"),
    (r"ఈరోజు|నేడు", "今天"),
    (r"రేపు", "明天"),
    (r"ఇప్పుడే", "刚刚"),
    (r"(?P<num>\d+)\s*(?P<unit>సెకన్ల|నిమిషాల|గంటల|రోజుల|వారాల|నెలల|సంవత్సరాల)\s+తర్వాత",
     lambda m: "%s%s后" % (
         _to_ascii(m.group("num")),
         {"సెకన్ల": "秒", "నిమిషాల": "分钟", "గంటల": "小时",
          "రోజుల": "天", "వారాల": "周", "నెలల": "月",
          "సంవత్సరాల": "年"}[m.group("unit")])),
    (r"(?P<num>\d+)\s*(?P<unit>సెకన్ల|నిమిషాల|గంటల|రోజుల|వారాల|నెలల|సంవత్సరాల)\s+క్రితం",
     lambda m: "%s%s前" % (
         _to_ascii(m.group("num")),
         {"సెకన్ల": "秒", "నిమిషాల": "分钟", "గంటల": "小时",
          "రోజుల": "天", "వారాల": "周", "నెలల": "月",
          "సంవత్సరాల": "年"}[m.group("unit")])),
    (r"వచ్చే\s+వారం", "下周"),
    (r"గత\s+వారం", "上周"),
    (r"వచ్చే\s+నెల", "下个月"),
    (r"గత\s+నెల", "上个月"),
    (r"వచ్చే\s+సంవత్సరం", "明年"),
    (r"గత\s+సంవత్సరం", "去年"),
]

for _month in sorted(_TE_MONTHS, key=len, reverse=True):
    SUB_TRANSLATE.append((_month, _TE_MONTHS[_month]))

for _weekday in sorted(_TE_WEEKDAYS, key=len, reverse=True):
    SUB_TRANSLATE.append((_weekday, _TE_WEEKDAYS[_weekday]))

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []
