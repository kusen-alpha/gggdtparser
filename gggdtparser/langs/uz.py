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


def _uz_later(match):
    return "%s%s后" % (match.group(1), _UZ_UNITS[match.group(2)])


def _uz_earlier(match):
    return "%s%s前" % (match.group(1), _UZ_UNITS[match.group(2)])


SUB_TRANSLATE = [
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
