# -*- coding:utf-8 -*-


"""
古吉拉特语
"""

_GU_DIGITS = str.maketrans("૦૧૨૩૪૫૬૭૮૯", "0123456789")

_GU_MONTHS = {
    "જાન્યુઆરી": "1月",
    "ફેબ્રુઆરી": "2月",
    "માર્ચ": "3月",
    "એપ્રિલ": "4月",
    "મે": "5月",
    "જૂન": "6月",
    "જુલાઈ": "7月",
    "ઓગસ્ટ": "8月",
    "સપ્ટેમ્બર": "9月",
    "ઓક્ટોબર": "10月",
    "નવેમ્બર": "11月",
    "ડિસેમ્બર": "12月",
}

_GU_MONTHS_RE = "|".join(sorted(_GU_MONTHS, key=len, reverse=True))

_GU_WEEKDAYS = {
    "સોમવાર": "周一",
    "મંગળવાર": "周二",
    "બુધવાર": "周三",
    "ગુરુવાર": "周四",
    "શુક્રવાર": "周五",
    "શનિવાર": "周六",
    "રવિવાર": "周日",
}

_GU_WEEKDAYS_RE = "|".join(sorted(_GU_WEEKDAYS, key=len, reverse=True))


def _to_ascii(value):
    return value.translate(_GU_DIGITS)


def _numeric_date(match):
    return "%s/%s/%s" % (
        _to_ascii(match.group("Y")),
        _to_ascii(match.group("m")),
        _to_ascii(match.group("d")),
    )


def _named_date(match):
    day = _to_ascii(match.group("d"))
    year = _to_ascii(match.group("Y"))
    return "%s %s %s" % (day, _GU_MONTHS[match.group("name")], year)


SUB_TRANSLATE = [
    (r"(?:આવતા|આવતી|આવનાર)\s+(%s)" % _GU_WEEKDAYS_RE,
     lambda m: "下%s" % _GU_WEEKDAYS[m.group(1)]),
    (r"(?:ગયા|ગઈ|પાછલા)\s+(%s)" % _GU_WEEKDAYS_RE,
     lambda m: "上%s" % _GU_WEEKDAYS[m.group(1)]),
    (r"આ\s+(%s)" % _GU_WEEKDAYS_RE,
     lambda m: "这%s" % _GU_WEEKDAYS[m.group(1)]),
    (r"આજે\s+સવારે", "今天 08:00 am"),
    (r"આજે\s+બપોરે", "今天 12:00 pm"),
    (r"આજે\s+સાંજે", "今天 20:00 pm"),
    (r"આજે\s+રાત્રે", "今天 22:00 pm"),
    (r"આવતીકાલે\s+સવારે", "明天 08:00 am"),
    (r"ગઈકાલે\s+રાત્રે", "昨天 22:00 pm"),
    (r"મધ્યરાત્રિ", "12:00 am"),
    (r"(?<!\d)(?P<Y>[૦-૯]{4})[\-\/\.]\s*(?P<m>[૦-૯]{1,2})[\-\/\.]\s*(?P<d>[૦-૯]{1,2})(?!\d)",
     _numeric_date),
    (r"(?P<d>[૦-૯]{1,2}|\d{1,2})\s*(?P<name>%s)\s*(?P<Y>[૦-૯]{4}|\d{4})"
     % _GU_MONTHS_RE, _named_date),
    (r"(?P<name>%s)\s*(?P<d>[૦-૯]{1,2}|\d{1,2})[,\s]+\s*(?P<Y>[૦-૯]{4}|\d{4})"
     % _GU_MONTHS_RE, _named_date),
    (r"(?P<name>%s)\s*(?P<Y>[૦-૯]{4})" % _GU_MONTHS_RE,
     lambda m: "%s %s" % (_GU_MONTHS[m.group("name")], _to_ascii(m.group("Y")))),
    (r"ગઈકાલે", "昨天"),
    (r"આજે", "今天"),
    (r"આવતીકાલે", "明天"),
    (r"પરમદિવસે", "后天"),
    (r"હમણાં", "刚刚"),
    (r"(?P<num>\d+)\s*(?P<unit>સેકન્ડ|મિનિટ|કલાક|દિવસ|અઠવાડિયું|મહિનો|મહિના|વર્ષ)\s+પછી",
     lambda m: "%s%s后" % (
         _to_ascii(m.group("num")),
         {"સેકન્ડ": "秒", "મિનિટ": "分钟", "કલાક": "小时",
          "દિવસ": "天", "અઠવાડિયું": "周", "મહિનો": "月",
          "મહિના": "月", "વર્ષ": "年"}[m.group("unit")])),
    (r"(?P<num>\d+)\s*(?P<unit>સેકન્ડ|મિનિટ|કલાક|દિવસ|અઠવાડિયું|મહિનો|મહિના|વર્ષ)\s+પહેલાં",
     lambda m: "%s%s前" % (
         _to_ascii(m.group("num")),
         {"સેકન્ડ": "秒", "મિનિટ": "分钟", "કલાક": "小时",
          "દિવસ": "天", "અઠવાડિયું": "周", "મહિનો": "月",
          "મહિના": "月", "વર્ષ": "年"}[m.group("unit")])),
    (r"આવતા\s+અઠવાડિયે", "下周"),
    (r"ગયા\s+અઠવાડિયે", "上周"),
    (r"આવતા\s+મહિને", "下个月"),
    (r"ગયા\s+મહિને", "上个月"),
    (r"આવતા\s+વર્ષે", "明年"),
    (r"ગયા\s+વર્ષે", "去年"),
]

for _month in sorted(_GU_MONTHS, key=len, reverse=True):
    SUB_TRANSLATE.append((_month, _GU_MONTHS[_month]))

for _weekday in sorted(_GU_WEEKDAYS, key=len, reverse=True):
    SUB_TRANSLATE.append((_weekday, _GU_WEEKDAYS[_weekday]))

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []
