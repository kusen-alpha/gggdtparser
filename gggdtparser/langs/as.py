# -*- coding:utf-8 -*-

"""
阿萨姆语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_AS_DIGITS = str.maketrans("০১২৩৪৫৬৭৮৯", "0123456789")

_AS_MONTHS = {
    "জানুৱাৰী": "1月",
    "ফেব্ৰুৱাৰী": "2月",
    "মাৰ্চ": "3月",
    "এপ্ৰিল": "4月",
    "মে'": "5月",
    "জুন": "6月",
    "জুলাই": "7月",
    "আগষ্ট": "8月",
    "ছেপ্টেম্বৰ": "9月",
    "অক্টোবৰ": "10月",
    "নৱেম্বৰ": "11月",
    "ডিচেম্বৰ": "12月",
}
_AS_MONTHS_RE = "|".join(sorted(_AS_MONTHS, key=len, reverse=True))

_AS_UNIT_MAP = {
    "চেকেণ্ড": "秒", "মিনিট": "分钟", "ঘণ্টা": "小时",
    "দিন": "天", "সপ্তাহ": "周", "মাহ": "月", "বছৰ": "年",
}
_AS_UNIT_BASE_RE = (
    r"চেকেণ্ড|মিনিট|ঘণ্টা|দিন|সপ্তাহ|মাহ|বছৰ"
)

_AS_WEEKDAYS = {
    "সোমবাৰ": "周一",
    "মঙ্গলবাৰ": "周二",
    "বুধবাৰ": "周三",
    "বৃহস্পতিবাৰ": "周四",
    "শুক্ৰবাৰ": "周五",
    "শনিবাৰ": "周六",
    "দেওবাৰ": "周日",
    "ৰবিবাৰ": "周日",
}
_AS_WEEKDAYS_RE = "|".join(sorted(_AS_WEEKDAYS, key=len, reverse=True))


def _as_ascii(value):
    return value.translate(_AS_DIGITS)


def _as_named_date(match):
    return "%s %s %s" % (
        _as_ascii(match.group("d")),
        _AS_MONTHS[match.group("name")],
        _as_ascii(match.group("Y")),
    )


def _as_later(match):
    return "%s%s后" % (match.group("a"), _AS_UNIT_MAP[match.group("b")])


def _as_earlier(match):
    return "%s%s前" % (match.group("a"), _AS_UNIT_MAP[match.group("b")])


SUB_TRANSLATE = [
    (r"(?:অহা|পৰৱৰ্তী)\s+(%s)" % _AS_WEEKDAYS_RE,
     lambda m: "下%s" % _AS_WEEKDAYS[m.group(1)]),
    (r"(?:যোৱা|গত)\s+(%s)" % _AS_WEEKDAYS_RE,
     lambda m: "上%s" % _AS_WEEKDAYS[m.group(1)]),
    (r"এই\s+(%s)" % _AS_WEEKDAYS_RE,
     lambda m: "这%s" % _AS_WEEKDAYS[m.group(1)]),
    (r"আজি\s+পুৱা", "今天 08:00 am"),
    (r"আজি\s+দুপৰীয়া", "今天 12:00 pm"),
    (r"আজি\s+আবেলি", "今天 15:00 pm"),
    (r"আজি\s+গধূলি", "今天 20:00 pm"),
    (r"আজি\s+ৰাতি", "今天 22:00 pm"),
    (r"কাইলৈ\s+পুৱা", "明天 08:00 am"),
    (r"যোৱাকালি\s+ৰাতি", "昨天 22:00 pm"),
    (r"মাজনিশা", "12:00 am"),
    (r"[০-৯]+", lambda m: m.group(0).translate(_AS_DIGITS)),
    (r"(?P<d>\d{1,2})\s*(?P<name>%s)\s*(?P<Y>\d{4})" % _AS_MONTHS_RE,
     _as_named_date),
    (r"(?P<name>%s)\s*(?P<d>\d{1,2})[,\s]+\s*(?P<Y>\d{4})" % _AS_MONTHS_RE,
     _as_named_date),
    (r"(?P<name>%s)\s*(?P<Y>\d{4})" % _AS_MONTHS_RE,
     lambda m: "%s %s" % (_AS_MONTHS[m.group("name")], m.group("Y"))),
    (r"পৰহিলৈ", "后天"),
    (r"পৰহি", "前天"),
    (r"যোৱাকালি", "昨天"),
    (r"আজি", "今天"),
    (r"কাইলৈ", "明天"),
    (r"এতিয়া", "刚刚"),
    (r"(?P<a>\d+)\s*(?P<b>%s)(?:ত|টো)?\s+(?:পিছত|পাছত|পৰে)"
     % _AS_UNIT_BASE_RE, _as_later),
    (r"(?P<a>\d+)\s*(?P<b>%s)(?:ত|টো)?\s+আগত" % _AS_UNIT_BASE_RE,
     _as_earlier),
    (r"পৰৱৰ্তী\s+সপ্তাহ", "下周"),
    (r"বিগত\s+সপ্তাহ", "上周"),
    (r"পৰৱৰ্তী\s+মাহ", "下个月"),
    (r"বিগত\s+মাহ", "上个月"),
    (r"পৰৱৰ্তী\s+বছৰ", "明年"),
    (r"বিগত\s+বছৰ", "去年"),
]

for _month in sorted(_AS_MONTHS, key=len, reverse=True):
    SUB_TRANSLATE.append((_month, _AS_MONTHS[_month]))

for _weekday in sorted(_AS_WEEKDAYS, key=len, reverse=True):
    SUB_TRANSLATE.append((_weekday, _AS_WEEKDAYS[_weekday]))
