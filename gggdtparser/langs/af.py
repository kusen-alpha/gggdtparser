# -*- coding:utf-8 -*-

"""
南非荷兰语（阿非利卡语）
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_AF_UNITS = {
    "sekonde": "秒", "minuut": "分钟", "minute": "分钟",
    "uur": "小时", "dag": "天", "dae": "天",
    "week": "周", "weke": "周", "maand": "月", "maande": "月",
    "jaar": "年",
}

SUB_TRANSLATE = [
    (r"\bJanuarie\b", "1月"),
    (r"\bFebruarie\b", "2月"),
    (r"\bMaart\b", "3月"),
    (r"\bApril\b", "4月"),
    (r"\bMei\b", "5月"),
    (r"\bJunie\b", "6月"),
    (r"\bJulie\b", "7月"),
    (r"\bAugustus\b", "8月"),
    (r"\bSeptember\b", "9月"),
    (r"\bOktober\b", "10月"),
    (r"\bNovember\b", "11月"),
    (r"\bDesember\b", "12月"),
    (r"\beergister\b", "前天"),
    (r"\boormôre\b", "后天"),
    (r"\bvandag\b", "今天"),
    (r"\bgister\b", "昨天"),
    (r"\bmôre\b", "明天"),
    (r"oor\s+(?P<num>\d+)\s*(?P<unit>sekonde|minute?|uur|dae?|weke?|maande?|jaar)",
     lambda m: "%s%s后" % (
         m.group("num"), _AF_UNITS[m.group("unit")])),
    (r"(?P<num>\d+)\s*(?P<unit>sekonde|minute?|uur|dae?|weke?|maande?|jaar)\s+gelede",
     lambda m: "%s%s前" % (
         m.group("num"), _AF_UNITS[m.group("unit")])),
    (r"\b(?:nou|net\s+nou)\b", "刚刚"),
    (r"\bvolgende\s+week\b", "下周"),
    (r"\bverlede\s+week\b", "上周"),
    (r"\bvolgende\s+maand\b", "下个月"),
    (r"\bverlede\s+maand\b", "上个月"),
    (r"\bvolgende\s+jaar\b", "明年"),
    (r"\bverlede\s+jaar\b", "去年"),
]
