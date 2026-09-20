# -*- coding:utf-8 -*-

"""
阿姆哈拉语（Amharic）
"""

ACCURATE_REGEX_LIST = [
    r"(?P<m>\d{1,2})\s*[月]\s*(?P<Y>\d{4})",
]
FUZZY_REGEX_LIST = []

_AM_UNITS = {
    "ሰከንድ": "秒", "ደቂቃ": "分钟", "ሰዓት": "小时",
    "ቀን": "天", "ሳምንት": "周", "ወር": "月",
    "ዓመት": "年", "አመት": "年",
}
_AM_UNIT_RE = "|".join(sorted(_AM_UNITS, key=len, reverse=True))

_AM_MONTHS = {
    "ጃንዋሪ": "1月", "ፌብሩዋሪ": "2月", "ማርች": "3月",
    "ኤፕሪል": "4月", "ሜይ": "5月", "ጁን": "6月",
    "ጁላይ": "7月", "ኦገስት": "8月", "ሴፕቴምበር": "9月",
    "ኦክቶበር": "10月", "ኖቬምበር": "11月", "ዲሴምበር": "12月",
}
_AM_MONTHS_RE = "|".join(sorted(_AM_MONTHS, key=len, reverse=True))

_AM_WEEKDAYS = {
    "ሰኞ": "周一",
    "ማክሰኞ": "周二",
    "ረቡዕ": "周三",
    "ሐሙስ": "周四",
    "ዓርብ": "周五",
    "ቅዳሜ": "周六",
    "እሑድ": "周日",
}
_AM_WEEKDAYS_RE = "|".join(sorted(_AM_WEEKDAYS, key=len, reverse=True))


def _am_named_date(match):
    return "%s %s %s" % (
        match.group("d"), _AM_MONTHS[match.group("name")], match.group("Y"))


def _am_month_first(match):
    return "%s %s, %s" % (
        _AM_MONTHS[match.group("name")], match.group("d"), match.group("Y"))


def _am_month_year(match):
    return "%s %s" % (_AM_MONTHS[match.group("name")], match.group("Y"))


def _am_later(match):
    return "%s%s后" % (
        match.group("num"), _AM_UNITS[match.group("unit")])


def _am_ago(match):
    return "%s%s前" % (
        match.group("num"), _AM_UNITS[match.group("unit")])


SUB_TRANSLATE = [
    (r"(?:በሚቀጥለው|የሚቀጥለው)\s+(%s)" % _AM_WEEKDAYS_RE,
     lambda m: "下%s" % _AM_WEEKDAYS[m.group(1)]),
    (r"ባለፈው\s+(%s)" % _AM_WEEKDAYS_RE,
     lambda m: "上%s" % _AM_WEEKDAYS[m.group(1)]),
    (r"(?:በዚህ|ይህን)\s+(%s)" % _AM_WEEKDAYS_RE,
     lambda m: "这%s" % _AM_WEEKDAYS[m.group(1)]),
    (r"ዛሬ\s+ጠዋት", "今天 08:00 am"),
    (r"ዛሬ\s+እኩለ\s+ቀን", "今天 12:00 pm"),
    (r"ዛሬ\s+ከሰዓት", "今天 15:00 pm"),
    (r"ዛሬ\s+ማታ", "今天 20:00 pm"),
    (r"ዛሬ\s+ሌሊት", "今天 22:00 pm"),
    (r"ነገ\s+ጠዋት", "明天 08:00 am"),
    (r"ትናንት\s+ማታ", "昨天 20:00 pm"),
    (r"እኩለ\s+ሌሊት", "12:00 am"),
    (r"(?P<d>\d{1,2})\s*(?P<name>%s)\s*(?:ቀን\s*)?(?P<Y>\d{4})"
     % _AM_MONTHS_RE, _am_named_date),
    (r"(?P<name>%s)\s+(?P<d>\d{1,2})[,\s]+\s*(?P<Y>\d{4})"
     % _AM_MONTHS_RE, _am_month_first),
    (r"(?P<name>%s)\s+(?P<Y>\d{4})" % _AM_MONTHS_RE, _am_month_year),
    (r"(?:ከ)?ትናንት\s+በፊት", "前天"),
    (r"(?:ከ)?ነገ\s+በኋላ", "后天"),
    (r"ዛሬ", "今天"),
    (r"ትናንት", "昨天"),
    (r"ነገ", "明天"),
    (r"አሁን\s+ብቻ|አሁን", "刚刚"),
    (r"ከ(?P<num>\d+)\s*(?P<unit>%s)\s+በኋላ" % _AM_UNIT_RE, _am_later),
    (r"ከ(?P<num>\d+)\s*(?P<unit>%s)\s+በፊት" % _AM_UNIT_RE, _am_ago),
    (r"በሚቀጥለው\s+ሳምንት", "下周"),
    (r"ባለፈው\s+ሳምንት", "上周"),
    (r"በሚቀጥለው\s+ወር", "下个月"),
    (r"ባለፈው\s+ወር", "上个月"),
    (r"በሚቀጥለው\s+ዓመት", "明年"),
    (r"ባለፈው\s+ዓመት", "去年"),
]

for _month in sorted(_AM_MONTHS, key=len, reverse=True):
    SUB_TRANSLATE.append((_month, _AM_MONTHS[_month]))

for _weekday in sorted(_AM_WEEKDAYS, key=len, reverse=True):
    SUB_TRANSLATE.append((_weekday, _AM_WEEKDAYS[_weekday]))
