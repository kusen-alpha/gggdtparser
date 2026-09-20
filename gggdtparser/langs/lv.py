# -*- coding:utf-8 -*-

"""
拉脱维亚语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_LV_UNITS = {
    "sekunde": "秒", "sekundes": "秒", "sekundēm": "秒",
    "minūte": "分钟", "minūtes": "分钟", "minūtēm": "分钟",
    "stunda": "小时", "stundas": "小时", "stundām": "小时",
    "diena": "天", "dienas": "天", "dienām": "天",
    "nedēļa": "周", "nedēļas": "周", "nedēļām": "周",
    "mēnesis": "月", "mēnesi": "月", "mēneši": "月", "mēnešiem": "月",
    "gads": "年", "gadi": "年", "gadus": "年", "gadiem": "年",
}
_LV_UNIT_RE = (
    r"sekundes|sekundēm|minūtes|minūtēm|stundas|stundām|"
    r"dienas|dienām|nedēļas|nedēļām|mēneši|mēnešiem|gadi|gadiem"
)


def _lv_later(match):
    return "%s%s后" % (match.group(1), _LV_UNITS[match.group(2)])


def _lv_earlier(match):
    return "%s%s前" % (match.group(1), _LV_UNITS[match.group(2)])


SUB_TRANSLATE = [
    (r"\bjanvāris\b", "1月"),
    (r"\bfebruāris\b", "2月"),
    (r"\bmarts\b", "3月"),
    (r"\baprīlis\b", "4月"),
    (r"\bmaijs\b", "5月"),
    (r"\bjūnijs\b", "6月"),
    (r"\bjūlijs\b", "7月"),
    (r"\baugusts\b", "8月"),
    (r"\bseptembris\b", "9月"),
    (r"\boktobris\b", "10月"),
    (r"\bnovembris\b", "11月"),
    (r"\bdecembris\b", "12月"),
    (r"\baizvakar\b", "前天"),
    (r"\bparīt\b", "后天"),
    (r"\bšodien\b", "今天"),
    (r"\bvakar\b", "昨天"),
    (r"\brīt\b", "明天"),
    (r"pēc\s+(?P<a>\d+)\s*(?P<b>%s)" % _LV_UNIT_RE, _lv_later),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+vēlāk" % _LV_UNIT_RE, _lv_later),
    (r"pirms\s+(?P<a>\d+)\s*(?P<b>%s)" % _LV_UNIT_RE, _lv_earlier),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+agrāk" % _LV_UNIT_RE, _lv_earlier),
    (r"\b(?:tagad|šobrīd)\b", "刚刚"),
    (r"\bnākamnedēļ\b", "下周"),
    (r"\bpagājušajā\s+nedēļā\b", "上周"),
    (r"\bnākamajā\s+mēnesī\b", "下个月"),
    (r"\bpagājušajā\s+mēnesī\b", "上个月"),
    (r"\bnākamgad\b", "明年"),
    (r"\bpagājušajā\s+gadā\b", "去年"),
]
