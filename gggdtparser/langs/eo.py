# -*- coding:utf-8 -*-

"""
世界语（Esperanto）
"""

ACCURATE_REGEX_LIST = [
    r"(?P<m>\d{1,2})\s*[月]\s*(?P<Y>\d{4})",
]
FUZZY_REGEX_LIST = []

_EO_UNITS = {
    "sekundo": "秒", "minuto": "分钟", "horo": "小时",
    "tago": "天", "semajno": "周", "monato": "月", "jaro": "年",
}
_EO_UNITS.update({
    "sekundoj": "秒", "minutoj": "分钟", "horoj": "小时",
    "tagoj": "天", "semajnoj": "周", "monatoj": "月", "jaroj": "年",
})
_EO_UNIT_RE = "|".join(sorted(_EO_UNITS, key=len, reverse=True))

_EO_MONTHS = {
    "januaro": "1月", "februaro": "2月", "marto": "3月",
    "aprilo": "4月", "majo": "5月", "junio": "6月",
    "julio": "7月", "aŭgusto": "8月", "septembro": "9月",
    "oktobro": "10月", "novembro": "11月", "decembro": "12月",
}
_EO_MONTHS_RE = "|".join(sorted(_EO_MONTHS, key=len, reverse=True))

_EO_WEEKDAYS = {
    "lundo": "周一", "lundon": "周一",
    "mardo": "周二", "mardon": "周二",
    "merkredo": "周三", "merkredon": "周三",
    "ĵaŭdo": "周四", "ĵaŭdon": "周四",
    "vendredo": "周五", "vendredon": "周五",
    "sabato": "周六", "sabaton": "周六",
    "dimanĉo": "周日", "dimanĉon": "周日",
}
_EO_WEEKDAYS_RE = "|".join(sorted(_EO_WEEKDAYS, key=len, reverse=True))


def _eo_month_no(name):
    return _EO_MONTHS[name.lower()]


def _eo_named_date(match):
    return "%s %s %s" % (
        match.group("d"), _eo_month_no(match.group("name")), match.group("Y"))


def _eo_month_first(match):
    return "%s %s, %s" % (
        _eo_month_no(match.group("name")), match.group("d"), match.group("Y"))


def _eo_month_year(match):
    return "%s %s" % (_eo_month_no(match.group("name")), match.group("Y"))


def _eo_later(match):
    return "%s%s后" % (
        match.group("num"), _EO_UNITS[match.group("unit").lower()])


def _eo_ago(match):
    return "%s%s前" % (
        match.group("num"), _EO_UNITS[match.group("unit").lower()])


SUB_TRANSLATE = [
    (r"(?i)\b(?:venonta|venontan|sekva|sekvan)\s+(%s)\b"
     % _EO_WEEKDAYS_RE,
     lambda m: "下%s" % _EO_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(?:pasinta|pasintan|antaŭa|antaŭan)\s+(%s)\b"
     % _EO_WEEKDAYS_RE,
     lambda m: "上%s" % _EO_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(?:ĉi\s+tiu|tiu\s+ĉi)\s+(%s)\b" % _EO_WEEKDAYS_RE,
     lambda m: "这%s" % _EO_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\bhodiaŭ\s+matene\b", "今天 08:00 am"),
    (r"(?i)\bhodiaŭ\s+tagmeze\b", "今天 12:00 pm"),
    (r"(?i)\bhodiaŭ\s+posttagmeze\b", "今天 15:00 pm"),
    (r"(?i)\bhodiaŭ\s+vespere\b", "今天 20:00 pm"),
    (r"(?i)\bhodiaŭ\s+nokte\b", "今天 22:00 pm"),
    (r"(?i)\bmorgaŭ\s+matene\b", "明天 08:00 am"),
    (r"(?i)\bhieraŭ\s+vespere\b", "昨天 20:00 pm"),
    (r"(?i)\bnoktomezo\b", "12:00 am"),
    (r"(?i)\btagmezo\b", "12:00 pm"),
    (r"(?i)(?P<d>\d{1,2})(?:-?a)?\s*(?:de\s+)?(?P<name>%s)\s+(?P<Y>\d{4})"
     % _EO_MONTHS_RE, _eo_named_date),
    (r"(?i)(?P<name>%s)\s+(?P<d>\d{1,2}),\s+(?P<Y>\d{4})"
     % _EO_MONTHS_RE, _eo_month_first),
    (r"(?i)(?P<name>%s)\s+(?P<Y>\d{4})" % _EO_MONTHS_RE, _eo_month_year),
    (r"(?i)\bpostmorgaŭ\b", "后天"),
    (r"(?i)\bantaŭhieraŭ\b", "前天"),
    (r"(?i)\bhodiaŭ\b", "今天"),
    (r"(?i)\bhieraŭ\b", "昨天"),
    (r"(?i)\bmorgaŭ\b", "明天"),
    (r"(?i)\bĵus\s+nun\b|\bĵus\b", "刚刚"),
    (r"(?i)(?:post|en)\s+(?P<num>\d+)\s+(?P<unit>%s)" % _EO_UNIT_RE,
     _eo_later),
    (r"(?i)antaŭ\s+(?P<num>\d+)\s+(?P<unit>%s)" % _EO_UNIT_RE, _eo_ago),
    (r"(?i)\bvenonta\s+semajno\b", "下周"),
    (r"(?i)\bpasinta\s+semajno\b", "上周"),
    (r"(?i)\bvenonta\s+monato\b", "下个月"),
    (r"(?i)\bpasinta\s+monato\b", "上个月"),
    (r"(?i)\bvenonta\s+jaro\b", "明年"),
    (r"(?i)\bpasinta\s+jaro\b", "去年"),
]

for _month in sorted(_EO_MONTHS, key=len, reverse=True):
    SUB_TRANSLATE.append((r"(?i)\b%s\b" % _month, _EO_MONTHS[_month]))

for _weekday in sorted(_EO_WEEKDAYS, key=len, reverse=True):
    SUB_TRANSLATE.append((r"(?i)\b%s\b" % _weekday,
                          _EO_WEEKDAYS[_weekday]))
