# -*- coding:utf-8 -*-

"""
老挝语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_LO_DIGITS = str.maketrans("໐໑໒໓໔໕໖໗໘໙", "0123456789")

_LO_MONTHS = {
    "ມັງກອນ": "1月",
    "ກຸມພາ": "2月",
    "ມີນາ": "3月",
    "ເມສາ": "4月",
    "ພຶດສະພາ": "5月",
    "ມິຖຸນາ": "6月",
    "ກໍລະກົດ": "7月",
    "ສິງຫາ": "8月",
    "ກັນຍາ": "9月",
    "ຕຸລາ": "10月",
    "ພະຈິກ": "11月",
    "ທັນວາ": "12月",
}
_LO_MONTHS_RE = "|".join(sorted(_LO_MONTHS, key=len, reverse=True))

_LO_UNIT_MAP = {
    "ວິນາທີ": "秒", "ນາທີ": "分钟", "ຊົ່ວໂມງ": "小时",
    "ມື້": "天", "ອາທິດ": "周", "ເດືອນ": "月", "ປີ": "年",
}
_LO_UNIT_BASE_RE = (
    r"ວິນາທີ|ນາທີ|ຊົ່ວໂມງ|ມື້|ອາທິດ|ເດືອນ|ປີ"
)


def _lo_ascii(value):
    return value.translate(_LO_DIGITS)


def _lo_gregorian_year(value):
    digits = _lo_ascii(value)
    if not digits.isdigit():
        return value
    year = int(digits)
    # 老挝佛历纪年通常落在 2500-2699 区间，超出范围视为公历。
    if year < 2500 or year > 2699:
        return value
    return str(year - 543)


def _lo_named_date(match):
    return "%s %s %s" % (
        _lo_ascii(match.group("d")),
        _LO_MONTHS[match.group("name")],
        _lo_gregorian_year(match.group("Y")),
    )


def _lo_month_year(match):
    return "%s %s" % (
        _LO_MONTHS[match.group("name")],
        _lo_gregorian_year(match.group("Y")),
    )


def _lo_later(match):
    return "%s%s后" % (match.group("a"), _LO_UNIT_MAP[match.group("b")])


def _lo_earlier(match):
    return "%s%s前" % (match.group("a"), _LO_UNIT_MAP[match.group("b")])


SUB_TRANSLATE = [
    (r"(?<![໐-໙])([໐-໙]{4})(?![໐-໙])",
     lambda m: _lo_gregorian_year(m.group(1))),
    (r"[໐-໙]+", lambda m: m.group(0).translate(_LO_DIGITS)),
    (r"(?P<d>\d{1,2})\s*(?P<name>%s)\s*(?P<Y>\d{4})" % _LO_MONTHS_RE,
     _lo_named_date),
    (r"(?P<name>%s)\s*(?P<d>\d{1,2})[,\s]+\s*(?P<Y>\d{4})" % _LO_MONTHS_RE,
     _lo_named_date),
    (r"(?P<name>%s)\s*(?P<Y>\d{4})" % _LO_MONTHS_RE,
     _lo_month_year),
    (r"ມື້ກ່ອນມື້ວານ", "前天"),
    (r"ມື້ອື່ນໆ", "后天"),
    (r"ມື້ວານ", "昨天"),
    (r"ມື້ນີ້", "今天"),
    (r"ມື້ອື່ນ", "明天"),
    (r"ດຽວນີ້", "刚刚"),
    (r"(?:ອີກ|ຫຼັງ)\s+(?P<a>\d+)\s*(?P<b>%s)" % _LO_UNIT_BASE_RE,
     _lo_later),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+ຕໍ່ມາ" % _LO_UNIT_BASE_RE, _lo_later),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s*ກ່ອນ" % _LO_UNIT_BASE_RE, _lo_earlier),
    (r"ອາທິດ\s*ໜ້າ", "下周"),
    (r"ອາທິດ\s*ແລ້ວ", "上周"),
    (r"ເດືອນ\s*ໜ້າ", "下个月"),
    (r"ເດືອນ\s*ແລ້ວ", "上个月"),
    (r"ປີ\s*ໜ້າ", "明年"),
    (r"ປີ\s*ແລ້ວ", "去年"),
]

for _month in sorted(_LO_MONTHS, key=len, reverse=True):
    SUB_TRANSLATE.append((_month, _LO_MONTHS[_month]))
