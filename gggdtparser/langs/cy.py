# -*- coding:utf-8 -*-

"""
威尔士语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_CY_UNIT_MAP = {
    "eiliad": "秒", "eiliadau": "秒",
    "munud": "分钟", "funud": "分钟", "munudau": "分钟", "funudau": "分钟",
    "awr": "小时", "oriau": "小时",
    "diwrnod": "天", "diwrnodau": "天",
    "wythnos": "周", "wythnosau": "周",
    "mis": "月", "misoedd": "月",
    "blwyddyn": "年", "blynyddoedd": "年",
}
_CY_UNIT_RE = (
    r"eiliad(?:au)?|funud(?:au)?|munud(?:au)?|awr(?:iau)?|"
    r"diwrnod(?:au)?|wythnos(?:au)?|mis(?:oedd)?|blwyddyn|blynyddoedd"
)


def _cy_later(match):
    return "%s%s后" % (match.group("a"), _CY_UNIT_MAP[match.group("b")])


def _cy_earlier(match):
    return "%s%s前" % (match.group("a"), _CY_UNIT_MAP[match.group("b")])


SUB_TRANSLATE = [
    (r"(?i)\bIonawr\b", "1月"),
    (r"(?i)\bChwefror\b", "2月"),
    (r"(?i)\bMawrth\b", "3月"),
    (r"(?i)\bEbrill\b", "4月"),
    (r"(?i)\bMai\b", "5月"),
    (r"(?i)\bMehefin\b", "6月"),
    (r"(?i)\bGorffennaf\b", "7月"),
    (r"(?i)\bAwst\b", "8月"),
    (r"(?i)\bMedi\b", "9月"),
    (r"(?i)\bHydref\b", "10月"),
    (r"(?i)\bTachwedd\b", "11月"),
    (r"(?i)\bRhagfyr\b", "12月"),
    (r"(?i)\bechdoe\b", "前天"),
    (r"(?i)\bdrennydd\b", "后天"),
    (r"(?i)\bheddiw\b", "今天"),
    (r"(?i)\bddoe\b", "昨天"),
    (r"(?i)\byfory\b", "明天"),
    (r"(?i)\b(?:nawr|ar hyn o bryd)\b", "刚刚"),
    (r"(?i)(?:mewn|ymhen)\s+(?P<a>\d+)\s*(?P<b>%s)" % _CY_UNIT_RE,
     _cy_later),
    (r"(?i)(?P<a>\d+)\s*(?P<b>%s)\s+yn\s+[ôo]l" % _CY_UNIT_RE, _cy_earlier),
    (r"(?i)\bwythnos\s+nesaf\b", "下周"),
    (r"(?i)\bwythnos\s+(?:ddiwethaf|diwethaf)\b", "上周"),
    (r"(?i)\bmis\s+nesaf\b", "下个月"),
    (r"(?i)\bmis\s+diwethaf\b", "上个月"),
    (r"(?i)\bblwyddyn\s+nesaf\b", "明年"),
    (r"(?i)\bblwyddyn\s+ddiwethaf\b", "去年"),
]
