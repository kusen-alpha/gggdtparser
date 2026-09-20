# -*- coding:utf-8 -*-

"""
阿尔巴尼亚语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_SQ_UNITS = {
    "sekondë": "秒", "sekonda": "秒", "sekondash": "秒",
    "minutë": "分钟", "minuta": "分钟", "minutash": "分钟",
    "orë": "小时", "orësh": "小时",
    "ditë": "天", "ditësh": "天",
    "javë": "周", "javësh": "周",
    "muaj": "月", "muajsh": "月",
    "vit": "年", "vite": "年", "vjet": "年",
}
_SQ_UNIT_RE = (
    r"sekond[ëa]|sekondash|minut[ëa]|minutash|orë(?:sh)?|"
    r"dit[ëe]|ditësh|jav[ëe]|javësh|muaj(?:sh)?|vit(?:e)?|vjet"
)


def _sq_later(match):
    return "%s%s后" % (match.group(1), _SQ_UNITS[match.group(2)])


def _sq_earlier(match):
    return "%s%s前" % (match.group(1), _SQ_UNITS[match.group(2)])


SUB_TRANSLATE = [
    (r"\bjanar\b", "1月"),
    (r"\bshkurt\b", "2月"),
    (r"\bmars\b", "3月"),
    (r"\bprill\b", "4月"),
    (r"\bmaj\b", "5月"),
    (r"\bqershor\b", "6月"),
    (r"\bkorrik\b", "7月"),
    (r"\bgusht\b", "8月"),
    (r"\bshtator\b", "9月"),
    (r"\btetor\b", "10月"),
    (r"\bnëntor\b", "11月"),
    (r"\bdhjetor\b", "12月"),
    (r"\bpardje\b", "前天"),
    (r"\bpasnesër\b", "后天"),
    (r"\bsot\b", "今天"),
    (r"\bdje\b", "昨天"),
    (r"\bnesër\b", "明天"),
    (r"pas\s+(?P<a>\d+)\s*(?P<b>%s)" % _SQ_UNIT_RE, _sq_later),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+(?:më\s+vonë)" % _SQ_UNIT_RE, _sq_later),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+më\s+parë" % _SQ_UNIT_RE, _sq_earlier),
    (r"\b(?:tani|tani\s+menjëherë)\b", "刚刚"),
    (r"\bjava\s+e\s+ardhshme\b|\bjavën\s+e\s+ardhshme\b", "下周"),
    (r"\bjava\s+e\s+kaluar\b|\bjavën\s+e\s+kaluar\b", "上周"),
    (r"\bmuajin\s+e\s+ardhshëm\b", "下个月"),
    (r"\bmuajin\s+e\s+kaluar\b", "上个月"),
    (r"\bviti\s+e\s+ardhshëm\b|\bvitin\s+e\s+ardhshëm\b", "明年"),
    (r"\bviti\s+e\s+kaluar\b|\bvitin\s+e\s+kaluar\b", "去年"),
]
