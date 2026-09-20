# -*- coding:utf-8 -*-

"""
爱沙尼亚语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_ET_UNITS = {
    "sekund": "秒", "sekundit": "秒",
    "minut": "分钟", "minutit": "分钟",
    "minuti": "分钟",
    "tund": "小时", "tundi": "小时",
    "tunni": "小时",
    "päev": "天", "päeva": "天",
    "nädal": "周", "nädalat": "周",
    "nädala": "周",
    "kuu": "月", "kuud": "月",
    "aasta": "年", "aastat": "年",
}
_ET_UNIT_RE = (
    r"sekundit?|minuti|minutit?|tunni|tund|tundi|päeva|päev|"
    r"nädala|nädalat?|kuud?|aasta|aastat"
)


def _et_later(match):
    return "%s%s后" % (match.group(1), _ET_UNITS[match.group(2)])


def _et_earlier(match):
    return "%s%s前" % (match.group(1), _ET_UNITS[match.group(2)])


SUB_TRANSLATE = [
    (r"\bjaanuar\b", "1月"),
    (r"\bveebruar\b", "2月"),
    (r"\bmärts\b", "3月"),
    (r"\baprill\b", "4月"),
    (r"\bmai\b", "5月"),
    (r"\bjuuni\b", "6月"),
    (r"\bjuuli\b", "7月"),
    (r"\baugust\b", "8月"),
    (r"\bseptember\b", "9月"),
    (r"\boktoober\b", "10月"),
    (r"\bnovember\b", "11月"),
    (r"\bdetsember\b", "12月"),
    (r"\büleeile\b", "前天"),
    (r"\bülehomme\b", "后天"),
    (r"\btäna\b", "今天"),
    (r"\beile\b", "昨天"),
    (r"\bhomme\b", "明天"),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+pärast" % _ET_UNIT_RE, _et_later),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+tagasi" % _ET_UNIT_RE, _et_earlier),
    (r"\b(?:praegu|hetkel)\b", "刚刚"),
    (r"\bjärgmisel\s+nädalal\b", "下周"),
    (r"\beelmisel\s+nädalal\b", "上周"),
    (r"\bjärgmisel\s+kuul\b", "下个月"),
    (r"\beelmisel\s+kuul\b", "上个月"),
    (r"\bjärgmisel\s+aastal\b", "明年"),
    (r"\beelmisel\s+aastal\b", "去年"),
]
