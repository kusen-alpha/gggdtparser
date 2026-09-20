# -*- coding:utf-8 -*-

"""
高棉语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_KM_DIGITS = str.maketrans("០១២៣៤៥៦៧៨៩", "0123456789")

_KM_MONTHS = {
    "មករា": "1月",
    "កុម្ភៈ": "2月",
    "មីនា": "3月",
    "មេសា": "4月",
    "ឧសភា": "5月",
    "មិថុនា": "6月",
    "កក្កដា": "7月",
    "សីហា": "8月",
    "កញ្ញា": "9月",
    "តុលា": "10月",
    "វិច្ឆិកា": "11月",
    "ធ្នូ": "12月",
}
_KM_MONTHS_RE = "|".join(sorted(_KM_MONTHS, key=len, reverse=True))

_KM_UNIT_MAP = {
    "វិនាទី": "秒", "នាទី": "分钟", "ម៉ោង": "小时",
    "ថ្ងៃ": "天", "សប្តាហ៍": "周", "ខែ": "月", "ឆ្នាំ": "年",
}
_KM_UNIT_BASE_RE = (
    r"វិនាទី|នាទី|ម៉ោង|ថ្ងៃ|សប្តាហ៍|ខែ|ឆ្នាំ"
)


def _km_ascii(value):
    return value.translate(_KM_DIGITS)


def _km_gregorian_year(value):
    digits = _km_ascii(value)
    if not digits.isdigit():
        return value
    year = int(digits)
    # 高棉佛历纪年通常落在 2500-2699 区间，超出范围视为公历。
    if year < 2500 or year > 2699:
        return value
    return str(year - 543)


def _km_named_date(match):
    return "%s %s %s" % (
        _km_ascii(match.group("d")),
        _KM_MONTHS[match.group("name")],
        _km_gregorian_year(match.group("Y")),
    )


def _km_month_year(match):
    return "%s %s" % (
        _KM_MONTHS[match.group("name")],
        _km_gregorian_year(match.group("Y")),
    )


def _km_later(match):
    return "%s%s后" % (match.group("a"), _KM_UNIT_MAP[match.group("b")])


def _km_earlier(match):
    return "%s%s前" % (match.group("a"), _KM_UNIT_MAP[match.group("b")])


SUB_TRANSLATE = [
    (r"(?<![០-៩])([០-៩]{4})(?![០-៩])",
     lambda m: _km_gregorian_year(m.group(1))),
    (r"[០-៩]+", lambda m: m.group(0).translate(_KM_DIGITS)),
    (r"(?P<d>\d{1,2})\s*(?P<name>%s)\s*(?P<Y>\d{4})" % _KM_MONTHS_RE,
     _km_named_date),
    (r"(?P<name>%s)\s*(?P<d>\d{1,2})[,\s]+\s*(?P<Y>\d{4})" % _KM_MONTHS_RE,
     _km_named_date),
    (r"(?P<name>%s)\s*(?P<Y>\d{4})" % _KM_MONTHS_RE,
     _km_month_year),
    (r"ម្សិលមិញទៀត", "前天"),
    (r"ខានស្អែក", "后天"),
    (r"ថ្ងៃម្សិលមិញ", "昨天"),
    (r"ថ្ងៃនេះ", "今天"),
    (r"ថ្ងៃស្អែក", "明天"),
    (r"ឥឡូវ", "刚刚"),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s*(?:ក្រោយ|ទៀត)" % _KM_UNIT_BASE_RE,
     _km_later),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s*មុន" % _KM_UNIT_BASE_RE, _km_earlier),
    (r"សប្តាហ៍ក្រោយ", "下周"),
    (r"សប្តាហ៍មុន", "上周"),
    (r"ខែក្រោយ", "下个月"),
    (r"ខែមុន", "上个月"),
    (r"ឆ្នាំក្រោយ", "明年"),
    (r"ឆ្នាំមុន", "去年"),
]

for _month in sorted(_KM_MONTHS, key=len, reverse=True):
    SUB_TRANSLATE.append((_month, _KM_MONTHS[_month]))
