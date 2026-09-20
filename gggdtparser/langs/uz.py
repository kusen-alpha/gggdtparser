# -*- coding:utf-8 -*-

"""
乌兹别克语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_UZ_UNITS = {
    "soniya": "秒", "soniyadan": "秒",
    "daqiqa": "分钟", "daqiqadan": "分钟",
    "soat": "小时", "soatdan": "小时",
    "kun": "天", "kundan": "天",
    "hafta": "周", "haftadan": "周",
    "oy": "月", "oydan": "月",
    "yil": "年", "yildan": "年",
}
_UZ_UNIT_RE = (
    r"soniya(?:dan)?|daqiqa(?:dan)?|soat(?:dan)?|kun(?:dan)?|"
    r"hafta(?:dan)?|oy(?:dan)?|yil(?:dan)?"
)

_UZ_WEEKDAYS = {
    "dushanba": "周一",
    "seshanba": "周二",
    "chorshanba": "周三",
    "payshanba": "周四",
    "juma": "周五",
    "shanba": "周六",
    "yakshanba": "周日",
}


def _uz_later(match):
    return "%s%s后" % (match.group(1), _UZ_UNITS[match.group(2)])


def _uz_earlier(match):
    return "%s%s前" % (match.group(1), _UZ_UNITS[match.group(2)])


SUB_TRANSLATE = [
    (r"(?i)\b(?:kelasi|keyingi)\s+(dushanba|seshanba|chorshanba|payshanba|juma|shanba|yakshanba)\b",
     lambda m: "下%s" % _UZ_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(?:o'tgan|o'tggan|otgan)\s+(dushanba|seshanba|chorshanba|payshanba|juma|shanba|yakshanba)\b",
     lambda m: "上%s" % _UZ_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\bshu\s+(dushanba|seshanba|chorshanba|payshanba|juma|shanba|yakshanba)\b",
     lambda m: "这%s" % _UZ_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(dushanba|seshanba|chorshanba|payshanba|juma|shanba|yakshanba)\b",
     lambda m: "周%s" % {
         "dushanba": "一", "seshanba": "二", "chorshanba": "三",
         "payshanba": "四", "juma": "五", "shanba": "六",
         "yakshanba": "日"}[m.group(1).lower()]),
    (r"\byanvar\b", "1月"),
    (r"\bfevral\b", "2月"),
    (r"\bmart\b", "3月"),
    (r"\baprel\b", "4月"),
    (r"\bmay\b", "5月"),
    (r"\biyun\b", "6月"),
    (r"\biyul\b", "7月"),
    (r"\bavgust\b", "8月"),
    (r"\bsentabr\b", "9月"),
    (r"\boktabr\b", "10月"),
    (r"\bnoyabr\b", "11月"),
    (r"\bdekabr\b", "12月"),
    (r"\boldin\s+kecha\b", "前天"),
    (r"\bindin\b", "后天"),
    (r"(?i)\bbugun\s+ertalab\b", "今天 08:00 am"),
    (r"(?i)\bbugun\s+(?:tushda|tush\s+paytida)\b", "12:00 pm"),
    (r"(?i)\bbugun\s+tushdan\s+keyin\b", "今天 15:00 pm"),
    (r"(?i)\bbugun\s+kechqurun\b", "今天 20:00 pm"),
    (r"(?i)\bbugun\s+kechasi\b", "今天 22:00 pm"),
    (r"(?i)\bertaga\s+ertalab\b", "明天 08:00 am"),
    (r"(?i)\bertaga\s+kechqurun\b", "明天 20:00 pm"),
    (r"(?i)\bkecha\s+kechqurun\b", "昨天 20:00 pm"),
    (r"(?i)\bkecha\s+tunda\b", "昨天 22:00 pm"),
    (r"(?i)\b(?:yarim\s+tun|yarimtun)\b", "12:00 am"),
    (r"\bbugun\b", "今天"),
    (r"\bkecha\b", "昨天"),
    (r"\bertaga\b", "明天"),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+keyin" % _UZ_UNIT_RE, _uz_later),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+oldin" % _UZ_UNIT_RE, _uz_earlier),
    (r"\b(?:hozir|hoziroq)\b", "刚刚"),
    (r"\bkeyingi\s+hafta\b", "下周"),
    (r"\bo'tgan\s+hafta\b", "上周"),
    (r"\bkeyingi\s+oy\b", "下个月"),
    (r"\bo'tgan\s+oy\b", "上个月"),
    (r"\bkeyingi\s+yil\b", "明年"),
    (r"\bo'tgan\s+yil\b", "去年"),
]
