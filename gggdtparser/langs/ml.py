# -*- coding:utf-8 -*-

"""
马拉雅拉姆语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_ML_DIGITS = str.maketrans("൦൧൨൩൪൫൬൭൮൯", "0123456789")

_ML_MONTHS = {
    "ജനുവരി": "1月",
    "ഫെബ്രുവരി": "2月",
    "മാർച്ച്": "3月",
    "ഏപ്രിൽ": "4月",
    "മേയ്": "5月",
    "ജൂൺ": "6月",
    "ജൂലൈ": "7月",
    "ഓഗസ്റ്റ്": "8月",
    "സെപ്റ്റംബർ": "9月",
    "ഒക്ടോബർ": "10月",
    "നവംബർ": "11月",
    "ഡിസംബർ": "12月",
}
_ML_MONTHS_RE = "|".join(sorted(_ML_MONTHS, key=len, reverse=True))

_ML_UNIT_MAP = {
    "സെക്കൻഡ്": "秒", "മിനിറ്റ്": "分钟", "മിനിറ്": "分钟",
    "മണിക്കൂർ": "小时",
    "മണിക്കൂറ": "小时",
    "ദിവസം": "天", "ആഴ്ച": "周", "മാസം": "月", "വർഷം": "年",
}
_ML_UNIT_BASE_RE = (
    r"സെക്കൻഡ്|മിനിറ്|മിനിറ്റ്|മണിക്കൂറ|മണിക്കൂർ|"
    r"ദിവസം|ആഴ്ച|മാസം|വർഷം"
)


def _ml_ascii(value):
    return value.translate(_ML_DIGITS)


def _ml_named_date(match):
    return "%s %s %s" % (
        _ml_ascii(match.group("d")),
        _ML_MONTHS[match.group("name")],
        _ml_ascii(match.group("Y")),
    )


def _ml_later(match):
    return "%s%s后" % (match.group("a"), _ML_UNIT_MAP[match.group("b")])


def _ml_earlier(match):
    return "%s%s前" % (match.group("a"), _ML_UNIT_MAP[match.group("b")])


SUB_TRANSLATE = [
    (r"[൦-൯]+", lambda m: m.group(0).translate(_ML_DIGITS)),
    (r"(?P<d>\d{1,2})\s*(?P<name>%s)\s*(?P<Y>\d{4})" % _ML_MONTHS_RE,
     _ml_named_date),
    (r"(?P<name>%s)\s*(?P<d>\d{1,2})[,\s]+\s*(?P<Y>\d{4})" % _ML_MONTHS_RE,
     _ml_named_date),
    (r"(?P<name>%s)\s*(?P<Y>\d{4})" % _ML_MONTHS_RE,
     lambda m: "%s %s" % (_ML_MONTHS[m.group("name")], m.group("Y"))),
    (r"മിനിഞ്ഞാന്ന്", "前天"),
    (r"മറ്റന്നാൾ", "后天"),
    (r"ഇന്നലെ", "昨天"),
    (r"ഇന്ന്", "今天"),
    (r"നാളെ", "明天"),
    (r"ഇപ്പോൾ", "刚刚"),
    (r"(?P<a>\d+)\s*(?P<b>%s)(?:കൾ|ുകൾ|റിന്|റിനു|റിനും|ിന്|ിനു|ിനും)?\s+ശേഷം"
     % _ML_UNIT_BASE_RE, _ml_later),
    (r"(?P<a>\d+)\s*(?P<b>%s)(?:കൾ|ുകൾ|റിന്|റിനു|റിനും|ിന്|ിനു|ിനും)?\s+മുമ്പ്"
     % _ML_UNIT_BASE_RE, _ml_earlier),
    (r"അടുത്ത\s+ആഴ്ച", "下周"),
    (r"കഴിഞ്ഞ\s+ആഴ്ച", "上周"),
    (r"അടുത്ത\s+മാസം", "下个月"),
    (r"കഴിഞ്ഞ\s+മാസം", "上个月"),
    (r"അടുത്ത\s+വർഷം", "明年"),
    (r"കഴിഞ്ഞ\s+വർഷം", "去年"),
]

for _month in sorted(_ML_MONTHS, key=len, reverse=True):
    SUB_TRANSLATE.append((_month, _ML_MONTHS[_month]))
