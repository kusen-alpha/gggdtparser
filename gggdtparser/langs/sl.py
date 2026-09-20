# -*- coding:utf-8 -*-

"""
斯洛文尼亚语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_SL_UNITS = {
    "sekunda": "秒", "sekundi": "秒", "sekund": "秒",
    "minuta": "分钟", "minuti": "分钟", "minut": "分钟",
    "ura": "小时", "uri": "小时", "ur": "小时",
    "dan": "天", "dneva": "天", "dni": "天",
    "teden": "周", "tedna": "周", "tednov": "周",
    "mesec": "月", "meseca": "月", "mesecev": "月",
    "leto": "年", "leti": "年", "let": "年",
}
_SL_UNIT_RE = (
    r"sekund[ai]?|minut[ai]?|ur[ai]?|dan|dneva|dni|"
    r"teden|tedna|tednov|mesec(?:a|ev)?|let[io]?|let"
)


def _sl_later(match):
    return "%s%s后" % (match.group(1), _SL_UNITS[match.group(2)])


def _sl_earlier(match):
    return "%s%s前" % (match.group(1), _SL_UNITS[match.group(2)])


SUB_TRANSLATE = [
    (r"\bjanuar\b", "1月"),
    (r"\bfebruar\b", "2月"),
    (r"\bmarec\b", "3月"),
    (r"\bapril\b", "4月"),
    (r"\bmaj\b", "5月"),
    (r"\bjunij\b", "6月"),
    (r"\bjulij\b", "7月"),
    (r"\bavgust\b", "8月"),
    (r"\bseptember\b", "9月"),
    (r"\boktober\b", "10月"),
    (r"\bnovember\b", "11月"),
    (r"\bdecember\b", "12月"),
    (r"\bpredvčerajšnjim\b", "前天"),
    (r"\bpojutrišnjem\b", "后天"),
    (r"\bdanes\b", "今天"),
    (r"\bvčeraj\b", "昨天"),
    (r"\bjutri\b", "明天"),
    (r"čez\s+(?P<a>\d+)\s*(?P<b>%s)" % _SL_UNIT_RE, _sl_later),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+pozneje" % _SL_UNIT_RE, _sl_later),
    (r"pred\s+(?P<a>\d+)\s*(?P<b>%s)" % _SL_UNIT_RE, _sl_earlier),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+prej" % _SL_UNIT_RE, _sl_earlier),
    (r"\b(?:prav\s+zdaj|zdaj)\b", "刚刚"),
    (r"\bnaslednji\s+teden\b", "下周"),
    (r"\bprejšnji\s+teden\b", "上周"),
    (r"\bnaslednji\s+mesec\b", "下个月"),
    (r"\bprejšnji\s+mesec\b", "上个月"),
    (r"\bnaslednje\s+leto\b", "明年"),
    (r"\bprejšnje\s+leto\b", "去年"),
]
