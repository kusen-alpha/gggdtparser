# -*- coding:utf-8 -*-

"""
立陶宛语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_LT_UNITS = {
    "sekundė": "秒", "sekundes": "秒", "sekundžių": "秒",
    "minutė": "分钟", "minutes": "分钟", "minučių": "分钟",
    "valanda": "小时", "valandas": "小时", "valandų": "小时",
    "diena": "天", "dienas": "天", "dienų": "天",
    "savaitė": "周", "savaites": "周", "savaičių": "周",
    "mėnuo": "月", "mėnesį": "月", "mėnesių": "月",
    "mėnesius": "月", "mėnesio": "月",
    "metai": "年", "metus": "年", "metų": "年", "metais": "年",
}
_LT_UNIT_RE = (
    r"sekund[ėe]s?|sekundžių|minut[ėe]s?|minučių|"
    r"valand[ao]s?|valandų|dien[ao]s?|dienų|"
    r"savait[ėe]s?|savaičių|mėnes(?:į|ių|ius|io)|met(?:us|ais|ų|ai|ą)"
)


def _lt_later(match):
    return "%s%s后" % (match.group(1), _LT_UNITS[match.group(2)])


def _lt_earlier(match):
    return "%s%s前" % (match.group(1), _LT_UNITS[match.group(2)])


SUB_TRANSLATE = [
    (r"\bsausis\b", "1月"),
    (r"\bvasaris\b", "2月"),
    (r"\bkovas\b", "3月"),
    (r"\bbalandis\b", "4月"),
    (r"\bgegužė\b", "5月"),
    (r"\bbirželis\b", "6月"),
    (r"\bliepa\b", "7月"),
    (r"\brugpjūtis\b", "8月"),
    (r"\brugsėjis\b", "9月"),
    (r"\bspalis\b", "10月"),
    (r"\blapkritis\b", "11月"),
    (r"\bgruodis\b", "12月"),
    (r"\bužvakar\b", "前天"),
    (r"\bporyt\b", "后天"),
    (r"\bšiandien\b", "今天"),
    (r"\bvakar\b", "昨天"),
    (r"\brytoj\b", "明天"),
    (r"po\s+(?P<a>\d+)\s*(?P<b>%s)" % _LT_UNIT_RE, _lt_later),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+vėliau" % _LT_UNIT_RE, _lt_later),
    (r"prieš\s+(?P<a>\d+)\s*(?P<b>%s)" % _LT_UNIT_RE, _lt_earlier),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+anksčiau" % _LT_UNIT_RE, _lt_earlier),
    (r"\b(?:dabar|šiuo\s+metu)\b", "刚刚"),
    (r"\bkitą\s+savaitę\b", "下周"),
    (r"\bpraėjusią\s+savaitę\b", "上周"),
    (r"\bkitą\s+mėnesį\b", "下个月"),
    (r"\bpraėjusį\s+mėnesį\b", "上个月"),
    (r"\bkitais\s+metais\b", "明年"),
    (r"\bpraėjusiais\s+metais\b", "去年"),
]
