# -*- coding:utf-8 -*-

"""
缅甸语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_MY_DIGITS = str.maketrans("၀၁၂၃၄၅၆၇၈၉", "0123456789")

_MY_MONTHS = {
    "ဇန်နဝါရီ": "1月",
    "ဖေဖော်ဝါရီ": "2月",
    "မတ်": "3月",
    "ဧပြီ": "4月",
    "မေ": "5月",
    "ဇွန်": "6月",
    "ဇူလိုင်": "7月",
    "ဩဂုတ်": "8月",
    "စက်တင်ဘာ": "9月",
    "အောက်တိုဘာ": "10月",
    "နိုဝင်ဘာ": "11月",
    "ဒီဇင်ဘာ": "12月",
}
_MY_MONTHS_RE = "|".join(sorted(_MY_MONTHS, key=len, reverse=True))

_MY_UNIT_MAP = {
    "စက္ကန့်": "秒", "မိနစ်": "分钟", "နာရီ": "小时", "ရက်": "天",
    "ရက်သတ္တပတ်": "周", "လ": "月", "နှစ်": "年",
}
_MY_UNIT_BASE_RE = (
    r"စက္ကန့်|မိနစ်|နာရီ|ရက်သတ္တပတ်|ရက်|လ|နှစ်"
)

_MY_WEEKDAYS = {
    "တနင်္လာ": "周一",
    "အင်္ဂါ": "周二",
    "ဗုဒ္ဓဟူး": "周三",
    "ကြာသပတေး": "周四",
    "သောကြာ": "周五",
    "စနေ": "周六",
    "တနင်္ဂနွေ": "周日",
}
_MY_WEEKDAYS_RE = "|".join(sorted(_MY_WEEKDAYS, key=len, reverse=True))


def _my_ascii(value):
    return value.translate(_MY_DIGITS)


def _my_named_date(match):
    return "%s %s %s" % (
        _my_ascii(match.group("d")),
        _MY_MONTHS[match.group("name")],
        _my_ascii(match.group("Y")),
    )


def _my_later(match):
    return "%s%s后" % (match.group("a"), _MY_UNIT_MAP[match.group("b")])


def _my_earlier(match):
    return "%s%s前" % (match.group("a"), _MY_UNIT_MAP[match.group("b")])


SUB_TRANSLATE = [
    (r"(?:လာမယ့်|နောက်)\s*(%s)" % _MY_WEEKDAYS_RE,
     lambda m: "下%s" % _MY_WEEKDAYS[m.group(1)]),
    (r"ပြီးခဲ့တဲ့\s*(%s)" % _MY_WEEKDAYS_RE,
     lambda m: "上%s" % _MY_WEEKDAYS[m.group(1)]),
    (r"ဒီ\s*(%s)" % _MY_WEEKDAYS_RE,
     lambda m: "这%s" % _MY_WEEKDAYS[m.group(1)]),
    (r"ဒီနေ့\s+မနက်", "今天 08:00 am"),
    (r"ဒီနေ့\s+မွန်းတည့်", "今天 12:00 pm"),
    (r"ဒီနေ့\s+မွန်းလွဲ", "今天 15:00 pm"),
    (r"ဒီနေ့\s+ညနေ", "今天 20:00 pm"),
    (r"ဒီနေ့\s+ည", "今天 22:00 pm"),
    (r"မနက်ဖြန်\s+မနက်", "明天 08:00 am"),
    (r"မနေ့က\s+ည", "昨天 22:00 pm"),
    (r"သန်းခေါင်ယံ", "12:00 am"),
    (r"[၀-၉]+", lambda m: m.group(0).translate(_MY_DIGITS)),
    (r"(?P<d>\d{1,2})\s*(?P<name>%s)\s*(?P<Y>\d{4})" % _MY_MONTHS_RE,
     _my_named_date),
    (r"(?P<name>%s)\s*(?P<d>\d{1,2})[,\s]+\s*(?P<Y>\d{4})" % _MY_MONTHS_RE,
     _my_named_date),
    (r"(?P<name>%s)\s*(?P<Y>\d{4})" % _MY_MONTHS_RE,
     lambda m: "%s %s" % (_MY_MONTHS[m.group("name")], m.group("Y"))),
    (r"တစ်နေ့က", "前天"),
    (r"သန်ဘက်ခါ", "后天"),
    (r"မနေ့က", "昨天"),
    (r"ဒီနေ့", "今天"),
    (r"မနက်ဖြန်", "明天"),
    (r"အခု", "刚刚"),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s*အကြာက" % _MY_UNIT_BASE_RE, _my_earlier),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s*အကြာ" % _MY_UNIT_BASE_RE, _my_later),
    (r"လွန်ခဲ့တဲ့\s*(?P<a>\d+)\s*(?P<b>%s)" % _MY_UNIT_BASE_RE,
     _my_earlier),
    (r"နောက်\s*(?:အပတ်|တစ်ပါတ်)", "下周"),
    (r"ပြီးခဲ့တဲ့\s*(?:အပတ်|တစ်ပါတ်)", "上周"),
    (r"နောက်\s*လ", "下个月"),
    (r"ပြီးခဲ့တဲ့\s*လ", "上个月"),
    (r"နောက်\s*နှစ်", "明年"),
    (r"ပြီးခဲ့တဲ့\s*နှစ်", "去年"),
]

for _month in sorted(_MY_MONTHS, key=len, reverse=True):
    SUB_TRANSLATE.append((_month, _MY_MONTHS[_month]))

for _weekday in sorted(_MY_WEEKDAYS, key=len, reverse=True):
    SUB_TRANSLATE.append((_weekday, _MY_WEEKDAYS[_weekday]))
