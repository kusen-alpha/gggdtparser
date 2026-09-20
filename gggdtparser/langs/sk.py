# -*- coding:utf-8 -*-

"""
斯洛伐克语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_SK_UNITS = {
    "sekunda": "秒", "sekundy": "秒", "sekúnd": "秒",
    "minúta": "分钟", "minúty": "分钟", "minút": "分钟",
    "hodina": "小时", "hodiny": "小时", "hodín": "小时",
    "deň": "天", "dni": "天", "dní": "天",
    "týždeň": "周", "týždne": "周", "týždňov": "周",
    "mesiac": "月", "mesiace": "月", "mesiacov": "月",
    "rok": "年", "roky": "年", "rokov": "年",
}
_SK_UNIT_RE = (
    r"sekund[ay]|sekúnd|minút[ay]?|hodin[ay]|hodín|"
    r"deň|dn[ií]|týždeň|týždne|týždňov|mesiac(?:e|ov)?|rok(?:y|ov)?"
)


def _sk_later(match):
    return "%s%s后" % (match.group(1), _SK_UNITS[match.group(2)])


def _sk_earlier(match):
    return "%s%s前" % (match.group(1), _SK_UNITS[match.group(2)])


SUB_TRANSLATE = [
    (r"\bjanuár\b", "1月"),
    (r"\bfebruár\b", "2月"),
    (r"\bmarec\b", "3月"),
    (r"\bapríl\b", "4月"),
    (r"\bmáj\b", "5月"),
    (r"\bjún\b", "6月"),
    (r"\bjúl\b", "7月"),
    (r"\baugust\b", "8月"),
    (r"\bseptember\b", "9月"),
    (r"\boktóber\b", "10月"),
    (r"\bnovember\b", "11月"),
    (r"\bdecember\b", "12月"),
    (r"\bpredvčerom\b", "前天"),
    (r"\bpozajtra\b", "后天"),
    (r"\bdnes\b", "今天"),
    (r"\bvčera\b", "昨天"),
    (r"\bzajtra\b", "明天"),
    (r"o\s+(?P<a>\d+)\s*(?P<b>%s)" % _SK_UNIT_RE, _sk_later),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+neskôr" % _SK_UNIT_RE, _sk_later),
    (r"pred\s+(?P<a>\d+)\s*(?P<b>%s)" % _SK_UNIT_RE, _sk_earlier),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+skôr" % _SK_UNIT_RE, _sk_earlier),
    (r"\b(?:práve\s+teraz|teraz)\b", "刚刚"),
    (r"\bbudúci\s+týždeň\b", "下周"),
    (r"\bminulý\s+týždeň\b", "上周"),
    (r"\bbudúci\s+mesiac\b", "下个月"),
    (r"\bminulý\s+mesiac\b", "上个月"),
    (r"\bbudúci\s+rok\b", "明年"),
    (r"\bminulý\s+rok\b", "去年"),
]
