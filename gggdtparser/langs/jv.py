# -*- coding:utf-8 -*-

"""
爪哇语（Javanese）
"""

ACCURATE_REGEX_LIST = [
    r"(?P<m>\d{1,2})\s*[月]\s*(?P<Y>\d{4})",
]
FUZZY_REGEX_LIST = []

_JV_UNITS = {
    "detik": "秒", "menit": "分钟", "jam": "小时",
    "dina": "天", "minggu": "周", "sasi": "月",
    "wulan": "月", "taun": "年",
}
_JV_UNIT_RE = "|".join(sorted(_JV_UNITS, key=len, reverse=True))

_JV_MONTHS = {
    "januari": "1月", "februari": "2月", "maret": "3月",
    "april": "4月", "mei": "5月", "juni": "6月",
    "juli": "7月", "agustus": "8月", "september": "9月",
    "oktober": "10月", "nopember": "11月", "desember": "12月",
}
_JV_MONTHS_RE = "|".join(sorted(_JV_MONTHS, key=len, reverse=True))

_JV_WEEKDAYS = {
    "senin": "周一",
    "selasa": "周二",
    "rebo": "周三",
    "kemis": "周四",
    "jumat": "周五",
    "setu": "周六",
    "minggu": "周日",
}
_JV_WEEKDAYS_RE = "|".join(sorted(_JV_WEEKDAYS, key=len, reverse=True))


def _jv_month_no(name):
    return _JV_MONTHS[name.lower()]


def _jv_named_date(match):
    return "%s %s %s" % (
        match.group("d"), _jv_month_no(match.group("name")), match.group("Y"))


def _jv_month_first(match):
    return "%s %s, %s" % (
        _jv_month_no(match.group("name")), match.group("d"), match.group("Y"))


def _jv_month_year(match):
    return "%s %s" % (_jv_month_no(match.group("name")), match.group("Y"))


def _jv_later(match):
    return "%s%s后" % (
        match.group("num"), _JV_UNITS[match.group("unit").lower()])


def _jv_ago(match):
    return "%s%s前" % (
        match.group("num"), _JV_UNITS[match.group("unit").lower()])


SUB_TRANSLATE = [
    (r"(?i)\b(senin|selasa|rebo|kemis|jumat|setu)\s+ngarep\b",
     lambda m: "下%s" % _JV_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(senin|selasa|rebo|kemis|jumat|setu)\s+(?:kepungkur|wingi)\b",
     lambda m: "上%s" % _JV_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(senin|selasa|rebo|kemis|jumat|setu)\s+iki\b",
     lambda m: "这%s" % _JV_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\bsesuk\s+esuk\b", "明天 08:00 am"),
    (r"(?i)\bwingi\s+bengi\b", "昨天 22:00 pm"),
    (r"(?i)\besuk\s+iki\b", "今天 08:00 am"),
    (r"(?i)\besuk\b", "今天 08:00 am"),
    (r"(?i)\bawan\s+iki\b", "今天 12:00 pm"),
    (r"(?i)\bawan\b", "今天 12:00 pm"),
    (r"(?i)\bsore\s+iki\b", "今天 15:00 pm"),
    (r"(?i)\bsore\b", "今天 15:00 pm"),
    (r"(?i)\bsonten\s+iki\b", "今天 20:00 pm"),
    (r"(?i)\bsonten\b", "今天 20:00 pm"),
    (r"(?i)\bbengi\s+iki\b", "今天 22:00 pm"),
    (r"(?i)\bbengi\b", "今天 22:00 pm"),
    (r"(?i)\btengah\s+wengi\b", "12:00 am"),
    (r"(?i)(?P<d>\d{1,2})\s*(?:tanggal\s+)?(?P<name>%s)\s+(?P<Y>\d{4})"
     % _JV_MONTHS_RE, _jv_named_date),
    (r"(?i)(?P<name>%s)\s+(?P<d>\d{1,2}),\s+(?P<Y>\d{4})"
     % _JV_MONTHS_RE, _jv_month_first),
    (r"(?i)(?P<name>%s)\s+(?P<Y>\d{4})" % _JV_MONTHS_RE, _jv_month_year),
    (r"(?i)\b2\s+dina\s+kepungkur\b", "前天"),
    (r"(?i)\b2\s+dina\s+maneh\b", "后天"),
    (r"(?i)\bdina\s+iki\b", "今天"),
    (r"(?i)(?<!minggu\s)(?<!sasi\s)(?<!wulan\s)(?<!taun\s)\bwingi\b",
     "昨天"),
    (r"(?i)\bsesuk\b|\bsesok\b", "明天"),
    (r"(?i)\b(?:saiki\s+iki|anyar\s+wae)\b", "刚刚"),
    (r"(?i)\b(?:sawise|sawisé)\s+(?P<num>\d+)\s+(?P<unit>%s)"
     % _JV_UNIT_RE, _jv_later),
    (r"(?i)(?P<num>\d+)\s+(?P<unit>%s)\s+maneh" % _JV_UNIT_RE, _jv_later),
    (r"(?i)(?P<num>\d+)\s+(?P<unit>%s)\s+kepungkur" % _JV_UNIT_RE,
     _jv_ago),
    (r"(?i)\bminggu\s+ngarep\b", "下周"),
    (r"(?i)\bminggu\s+wingi\b", "上周"),
    (r"(?i)\b(?:sasi|wulan)\s+ngarep\b", "下个月"),
    (r"(?i)\b(?:sasi|wulan)\s+wingi\b", "上个月"),
    (r"(?i)\btaun\s+ngarep\b", "明年"),
    (r"(?i)\btaun\s+wingi\b", "去年"),
]

for _month in sorted(_JV_MONTHS, key=len, reverse=True):
    SUB_TRANSLATE.append((r"(?i)\b%s\.?\b" % _month, _JV_MONTHS[_month]))

for _weekday in sorted(_JV_WEEKDAYS, key=len, reverse=True):
    SUB_TRANSLATE.append((r"(?i)\b%s\b" % _weekday, _JV_WEEKDAYS[_weekday]))
