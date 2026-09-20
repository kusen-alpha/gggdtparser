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

_AF_WEEKDAYS = {
    "maandag": "周一",
    "dinsdag": "周二",
    "woensdag": "周三",
    "donderdag": "周四",
    "vrydag": "周五",
    "saterdag": "周六",
    "sondag": "周日",
}

SUB_TRANSLATE = [
    (r"(?i)\b(?:volgende|aankomende|komende)\s+(maandag|dinsdag|woensdag|donderdag|vrydag|saterdag|sondag)\b",
     lambda m: "下%s" % _AF_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(?:verlede|afgelope)\s+(maandag|dinsdag|woensdag|donderdag|vrydag|saterdag|sondag)\b",
     lambda m: "上%s" % _AF_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(?:hierdie|dié)\s+(maandag|dinsdag|woensdag|donderdag|vrydag|saterdag|sondag)\b",
     lambda m: "这%s" % _AF_WEEKDAYS[m.group(1).lower()]),
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
    (r"(?i)\bvanoggend\b", "今天 08:00 am"),
    (r"(?i)\b(?:vandagmiddag|vanmiddag)\b", "今天 15:00 pm"),
    (r"(?i)\b(?:vandagaand|vanaand)\b", "今天 20:00 pm"),
    (r"(?i)\b(?:môreoggend|môre\s+oggend)\b", "明天 08:00 am"),
    (r"(?i)\b(?:môremiddag|môre\s+middag)\b", "明天 15:00 pm"),
    (r"(?i)\b(?:môreaand|môre\s+aand)\b", "明天 20:00 pm"),
    (r"(?i)\b(?:gisteraand|gister\s+aand)\b", "昨天 20:00 pm"),
    (r"(?i)\bgister\s+nag\b", "昨天 22:00 pm"),
    (r"(?i)\b(?:middaguur|middag)\b", "12:00 pm"),
    (r"(?i)\bmiddernag\b", "12:00 am"),
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

for _weekday in sorted(_AF_WEEKDAYS, key=len, reverse=True):
    SUB_TRANSLATE.append((r"(?i)\b%s\b" % _weekday, _AF_WEEKDAYS[_weekday]))
