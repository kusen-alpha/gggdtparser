# -*- coding:utf-8 -*-

"""
科萨语（Xhosa）
"""

ACCURATE_REGEX_LIST = [
    r"(?P<m>\d{1,2})\s*[月]\s*(?P<Y>\d{4})",
]
FUZZY_REGEX_LIST = []

_XH_UNITS = {
    "iiyure": "小时", "imizuzu": "分钟", "iintsuku": "天",
    "iiveki": "周", "iinyanga": "月", "iminyaka": "年",
}
_XH_UNIT_RE = "|".join(sorted(_XH_UNITS, key=len, reverse=True))

_XH_MONTHS = {
    "ujanuwari": "1月", "ufebruwari": "2月", "umatshi": "3月",
    "uaprili": "4月", "umeyi": "5月", "ujuni": "6月",
    "ujulayi": "7月", "uagasti": "8月", "useptemba": "9月",
    "uoktobha": "10月", "unovemba": "11月", "udisemba": "12月",
}
_XH_MONTHS_RE = "|".join(sorted(_XH_MONTHS, key=len, reverse=True))

_XH_WEEKDAYS = {
    "mvulo": "周一",
    "lwesibini": "周二", "ulwesibini": "周二",
    "lwesithathu": "周三", "ulwesithathu": "周三",
    "lwesine": "周四", "ulwesine": "周四",
    "lwesihlanu": "周五", "ulwesihlanu": "周五",
    "umgqibelo": "周六",
    "icawa": "周日",
}
_XH_WEEKDAYS_RE = "|".join(sorted(_XH_WEEKDAYS, key=len, reverse=True))


def _xh_month_no(name):
    return _XH_MONTHS[name.lower()]


def _xh_named_date(match):
    return "%s %s %s" % (
        match.group("d"), _xh_month_no(match.group("name")), match.group("Y"))


def _xh_month_first(match):
    return "%s %s, %s" % (
        _xh_month_no(match.group("name")), match.group("d"), match.group("Y"))


def _xh_month_year(match):
    return "%s %s" % (_xh_month_no(match.group("name")), match.group("Y"))


def _xh_later(match):
    return "%s%s后" % (
        match.group("num"), _XH_UNITS[match.group("unit").lower()])


def _xh_ago(match):
    return "%s%s前" % (
        match.group("num"), _XH_UNITS[match.group("unit").lower()])


SUB_TRANSLATE = [
    (r"(?i)\b(%s)\s+olandela(?:yo)?\b" % _XH_WEEKDAYS_RE,
     lambda m: "下%s" % _XH_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(%s)\s+odlulileyo\b" % _XH_WEEKDAYS_RE,
     lambda m: "上%s" % _XH_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(?:kulo|lo)\s+(%s)\b" % _XH_WEEKDAYS_RE,
     lambda m: "这%s" % _XH_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\bnamhlanje\s+kusasa\b", "今天 08:00 am"),
    (r"(?i)\bnamhlanje\s+emini\b", "今天 12:00 pm"),
    (r"(?i)\bnamhlanje\s+emvakwemini\b", "今天 15:00 pm"),
    (r"(?i)\bnamhlanje\s+ngokuhlwa\b", "今天 20:00 pm"),
    (r"(?i)\bnamhlanje\s+ebusuku\b", "今天 22:00 pm"),
    (r"(?i)\bngomso\s+kusasa\b", "明天 08:00 am"),
    (r"(?i)\bizolo\s+ngokuhlwa\b", "昨天 20:00 pm"),
    (r"(?i)\bezinzulwini\s+zobusuku\b", "12:00 am"),
    (r"(?i)(?P<d>\d{1,2})\s*(?:ngomhla\s+)?(?P<name>%s)\s+(?P<Y>\d{4})"
     % _XH_MONTHS_RE, _xh_named_date),
    (r"(?i)(?P<name>%s)\s+(?P<d>\d{1,2}),\s+(?P<Y>\d{4})"
     % _XH_MONTHS_RE, _xh_month_first),
    (r"(?i)(?P<name>%s)\s+(?P<Y>\d{4})" % _XH_MONTHS_RE, _xh_month_year),
    (r"(?i)\bnamhlanje\b", "今天"),
    (r"(?i)\bizolo\b", "昨天"),
    (r"(?i)\bngomso\b", "明天"),
    (r"(?i)\bngoku\b", "刚刚"),
    (r"(?i)(?P<num>\d+)\s*(?P<unit>%s)\s+ezizayo" % _XH_UNIT_RE,
     _xh_later),
    (r"(?i)(?P<num>\d+)\s*(?P<unit>%s)\s+ezidlulileyo" % _XH_UNIT_RE,
     _xh_ago),
    (r"(?i)\biveki\s+ezayo\b", "下周"),
    (r"(?i)\biveki\s+ephelileyo\b", "上周"),
    (r"(?i)\binyanga\s+ezayo\b", "下个月"),
    (r"(?i)\binyanga\s+ephelileyo\b", "上个月"),
    (r"(?i)\bunyaka\s+ozayo\b", "明年"),
    (r"(?i)\bunyaka\s+ophelileyo\b", "去年"),
]

for _month in sorted(_XH_MONTHS, key=len, reverse=True):
    SUB_TRANSLATE.append((r"(?i)\b%s\b" % _month, _XH_MONTHS[_month]))

for _weekday in sorted(_XH_WEEKDAYS, key=len, reverse=True):
    SUB_TRANSLATE.append((r"(?i)\b%s\b" % _weekday, _XH_WEEKDAYS[_weekday]))
