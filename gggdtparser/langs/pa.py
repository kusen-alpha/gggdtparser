# -*- coding:utf-8 -*-


"""
旁遮普语
"""

_PA_DIGITS = str.maketrans("੦੧੨੩੪੫੬੭੮੯", "0123456789")

_PA_MONTHS = {
    "ਜਨਵਰੀ": "1月",
    "ਫਰਵਰੀ": "2月",
    "ਮਾਰਚ": "3月",
    "ਅਪ੍ਰੈਲ": "4月",
    "ਮਈ": "5月",
    "ਜੂਨ": "6月",
    "ਜੁਲਾਈ": "7月",
    "ਅਗਸਤ": "8月",
    "ਸਤੰਬਰ": "9月",
    "ਅਕਤੂਬਰ": "10月",
    "ਨਵੰਬਰ": "11月",
    "ਦਸੰਬਰ": "12月",
}

_PA_MONTHS_RE = "|".join(sorted(_PA_MONTHS, key=len, reverse=True))


def _to_ascii(value):
    return value.translate(_PA_DIGITS)


def _numeric_date(match):
    return "%s/%s/%s" % (
        _to_ascii(match.group("Y")),
        _to_ascii(match.group("m")),
        _to_ascii(match.group("d")),
    )


def _named_date(match):
    day = _to_ascii(match.group("d"))
    year = _to_ascii(match.group("Y"))
    return "%s %s %s" % (day, _PA_MONTHS[match.group("name")], year)


SUB_TRANSLATE = [
    (r"(?<!\d)(?P<Y>[੦-੯]{4})[\-\/\.]\s*(?P<m>[੦-੯]{1,2})[\-\/\.]\s*(?P<d>[੦-੯]{1,2})(?!\d)",
     _numeric_date),
    (r"(?P<d>[੦-੯]{1,2}|\d{1,2})\s*(?P<name>%s)\s*(?P<Y>[੦-੯]{4}|\d{4})"
     % _PA_MONTHS_RE, _named_date),
    (r"(?P<name>%s)\s*(?P<d>[੦-੯]{1,2}|\d{1,2})[,\s]+\s*(?P<Y>[੦-੯]{4}|\d{4})"
     % _PA_MONTHS_RE, _named_date),
    (r"(?P<name>%s)\s*(?P<Y>[੦-੯]{4})" % _PA_MONTHS_RE,
     lambda m: "%s %s" % (_PA_MONTHS[m.group("name")], _to_ascii(m.group("Y")))),
    (r"ਬੀਤਿਆ\s+ਕੱਲ੍ਹ", "昨天"),
    (r"ਅੱਜ", "今天"),
    (r"ਕੱਲ੍ਹ", "明天"),
    (r"ਪਰਸੋਂ", "后天"),
    (r"ਹੁਣੇ", "刚刚"),
    (r"(?P<num>\d+)\s*(?P<unit>ਸਕਿੰਟ|ਮਿੰਟ|ਘੰਟਾ|ਘੰਟੇ|ਦਿਨ|ਹਫ਼ਤਾ|ਮਹੀਨਾ|ਮਹੀਨੇ|ਸਾਲ)\s+ਬਾਅਦ",
     lambda m: "%s%s后" % (
         _to_ascii(m.group("num")),
         {"ਸਕਿੰਟ": "秒", "ਮਿੰਟ": "分钟", "ਘੰਟਾ": "小时",
          "ਘੰਟੇ": "小时", "ਦਿਨ": "天", "ਹਫ਼ਤਾ": "周",
          "ਮਹੀਨਾ": "月", "ਮਹੀਨੇ": "月", "ਸਾਲ": "年"}[m.group("unit")])),
    (r"(?P<num>\d+)\s*(?P<unit>ਸਕਿੰਟ|ਮਿੰਟ|ਘੰਟਾ|ਘੰਟੇ|ਦਿਨ|ਹਫ਼ਤਾ|ਮਹੀਨਾ|ਮਹੀਨੇ|ਸਾਲ)\s+ਪਹਿਲਾਂ",
     lambda m: "%s%s前" % (
         _to_ascii(m.group("num")),
         {"ਸਕਿੰਟ": "秒", "ਮਿੰਟ": "分钟", "ਘੰਟਾ": "小时",
          "ਘੰਟੇ": "小时", "ਦਿਨ": "天", "ਹਫ਼ਤਾ": "周",
          "ਮਹੀਨਾ": "月", "ਮਹੀਨੇ": "月", "ਸਾਲ": "年"}[m.group("unit")])),
    (r"ਅਗਲੇ\s+ਹਫ਼ਤੇ", "下周"),
    (r"ਪਿਛਲੇ\s+ਹਫ਼ਤੇ", "上周"),
    (r"ਅਗਲੇ\s+ਮਹੀਨੇ", "下个月"),
    (r"ਪਿਛਲੇ\s+ਮਹੀਨੇ", "上个月"),
    (r"ਅਗਲੇ\s+ਸਾਲ", "明年"),
    (r"ਪਿਛਲੇ\s+ਸਾਲ", "去年"),
]

for _month in sorted(_PA_MONTHS, key=len, reverse=True):
    SUB_TRANSLATE.append((_month, _PA_MONTHS[_month]))

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []
