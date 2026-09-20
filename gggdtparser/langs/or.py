# -*- coding:utf-8 -*-

"""
奥里亚语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_OR_DIGITS = str.maketrans("୦୧୨୩୪୫୬୭୮୯", "0123456789")

_OR_MONTHS = {
    "ଜାନୁଆରୀ": "1月",
    "ଫେବୃଆରୀ": "2月",
    "ମାର୍ଚ୍ଚ": "3月",
    "ଅପ୍ରେଲ": "4月",
    "ମଇ": "5月",
    "ଜୁନ": "6月",
    "ଜୁଲାଇ": "7月",
    "ଅଗଷ୍ଟ": "8月",
    "ସେପ୍ଟେମ୍ବର": "9月",
    "ଅକ୍ଟୋବର": "10月",
    "ନଭେମ୍ବର": "11月",
    "ଡିସେମ୍ବର": "12月",
}
_OR_MONTHS_RE = "|".join(sorted(_OR_MONTHS, key=len, reverse=True))

_OR_UNIT_MAP = {
    "ସେକେଣ୍ଡ": "秒", "ମିନିଟ": "分钟", "ଘଣ୍ଟା": "小时",
    "ଦିନ": "天", "ସପ୍ତାହ": "周", "ମାସ": "月", "ବର୍ଷ": "年",
}
_OR_UNIT_BASE_RE = (
    r"ସେକେଣ୍ଡ|ମିନିଟ|ଘଣ୍ଟା|ଦିନ|ସପ୍ତାହ|ମାସ|ବର୍ଷ"
)

_OR_WEEKDAYS = {
    "ସୋମବାର": "周一",
    "ମଙ୍ଗଳବାର": "周二",
    "ବୁଧବାର": "周三",
    "ଗୁରୁବାର": "周四",
    "ଶୁକ୍ରବାର": "周五",
    "ଶନିବାର": "周六",
    "ରବିବାର": "周日",
}
_OR_WEEKDAYS_RE = "|".join(sorted(_OR_WEEKDAYS, key=len, reverse=True))


def _or_ascii(value):
    return value.translate(_OR_DIGITS)


def _or_named_date(match):
    return "%s %s %s" % (
        _or_ascii(match.group("d")),
        _OR_MONTHS[match.group("name")],
        _or_ascii(match.group("Y")),
    )


def _or_later(match):
    return "%s%s后" % (match.group("a"), _OR_UNIT_MAP[match.group("b")])


def _or_earlier(match):
    return "%s%s前" % (match.group("a"), _OR_UNIT_MAP[match.group("b")])


SUB_TRANSLATE = [
    (r"ଆସନ୍ତା\s+(%s)" % _OR_WEEKDAYS_RE,
     lambda m: "下%s" % _OR_WEEKDAYS[m.group(1)]),
    (r"ଗତ\s+(%s)" % _OR_WEEKDAYS_RE,
     lambda m: "上%s" % _OR_WEEKDAYS[m.group(1)]),
    (r"ଏହି\s+(%s)" % _OR_WEEKDAYS_RE,
     lambda m: "这%s" % _OR_WEEKDAYS[m.group(1)]),
    (r"ଆଜି\s+ସକାଳ", "今天 08:00 am"),
    (r"ଆଜି\s+ମଧ୍ୟାହ୍ନ", "今天 12:00 pm"),
    (r"ଆଜି\s+ଅପରାହ୍ନ", "今天 15:00 pm"),
    (r"ଆଜି\s+ସନ୍ଧ୍ୟା", "今天 20:00 pm"),
    (r"ଆଜି\s+ରାତି", "今天 22:00 pm"),
    (r"ଆସନ୍ତାକାଲି\s+ସକାଳ", "明天 08:00 am"),
    (r"ଗତକାଲି\s+ରାତି", "昨天 22:00 pm"),
    (r"ମଧ୍ୟରାତ୍ରି", "12:00 am"),
    (r"[୦-୯]+", lambda m: m.group(0).translate(_OR_DIGITS)),
    (r"(?P<d>\d{1,2})\s*(?P<name>%s)\s*(?P<Y>\d{4})" % _OR_MONTHS_RE,
     _or_named_date),
    (r"(?P<name>%s)\s*(?P<d>\d{1,2})[,\s]+\s*(?P<Y>\d{4})" % _OR_MONTHS_RE,
     _or_named_date),
    (r"(?P<name>%s)\s*(?P<Y>\d{4})" % _OR_MONTHS_RE,
     lambda m: "%s %s" % (_OR_MONTHS[m.group("name")], m.group("Y"))),
    (r"ଗତ\s+ପରଶୁ", "前天"),
    (r"ଆସନ୍ତା\s+ପରଶୁ", "后天"),
    (r"ଗତକାଲି", "昨天"),
    (r"ଆଜି", "今天"),
    (r"ଆସନ୍ତାକାଲି", "明天"),
    (r"ଏବେ", "刚刚"),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+(?:ପରେ|ପର)" % _OR_UNIT_BASE_RE, _or_later),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+ପୂର୍ବେ" % _OR_UNIT_BASE_RE, _or_earlier),
    (r"ଆସନ୍ତା\s+ସପ୍ତାହ", "下周"),
    (r"ଗତ\s+ସପ୍ତାହ", "上周"),
    (r"ଆସନ୍ତା\s+ମାସ", "下个月"),
    (r"ଗତ\s+ମାସ", "上个月"),
    (r"ଆସନ୍ତା\s+ବର୍ଷ", "明年"),
    (r"ଗତ\s+ବର୍ଷ", "去年"),
]

for _month in sorted(_OR_MONTHS, key=len, reverse=True):
    SUB_TRANSLATE.append((_month, _OR_MONTHS[_month]))

for _weekday in sorted(_OR_WEEKDAYS, key=len, reverse=True):
    SUB_TRANSLATE.append((_weekday, _OR_WEEKDAYS[_weekday]))
