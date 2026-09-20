# -*- coding:utf-8 -*-

"""
尼泊尔语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_NE_DIGITS = str.maketrans("०१२३४५६७८९", "0123456789")


def _ne_ascii(value):
    return value.translate(_NE_DIGITS)


_NE_UNITS = {
    "सेकेन्ड": "秒", "मिनेट": "分钟", "घण्टा": "小时",
    "दिन": "天", "हप्ता": "周", "महिना": "月", "वर्ष": "年",
}
_NE_WEEKDAYS = {
    "सोमबार": "周一",
    "मङ्गलबार": "周二",
    "मंगलबार": "周二",
    "बुधबार": "周三",
    "बिहिबार": "周四",
    "बिहीबार": "周四",
    "शुक्रबार": "周五",
    "शनिबार": "周六",
    "शनिवार": "周六",
    "आइतबार": "周日",
    "आइतवार": "周日",
}
_NE_WEEKDAYS_RE = "|".join(sorted(_NE_WEEKDAYS, key=len, reverse=True))
_NE_UNIT_RE = r"सेकेन्ड|मिनेट|घण्टा|दिन|हप्ता|महिना|वर्ष"


def _ne_later(match):
    return "%s%s后" % (_ne_ascii(match.group(1)), _NE_UNITS[match.group(2)])


def _ne_earlier(match):
    return "%s%s前" % (_ne_ascii(match.group(1)), _NE_UNITS[match.group(2)])


SUB_TRANSLATE = [
    (r"(?:अर्को|आउने)\s+(%s)" % _NE_WEEKDAYS_RE,
     lambda m: "下%s" % _NE_WEEKDAYS[m.group(1)]),
    (r"(?:गत|पछिल्लो|विगत)\s+(%s)" % _NE_WEEKDAYS_RE,
     lambda m: "上%s" % _NE_WEEKDAYS[m.group(1)]),
    (r"(?:यो|यही)\s+(%s)" % _NE_WEEKDAYS_RE,
     lambda m: "这%s" % _NE_WEEKDAYS[m.group(1)]),
    (r"आज\s+बिहान", "今天 08:00 am"),
    (r"आज\s+दिउँसो", "今天 12:00 pm"),
    (r"आज\s+साँझ(?:\s+मा)?", "今天 20:00 pm"),
    (r"आज\s+राति", "今天 22:00 pm"),
    (r"भोलि\s+बिहान", "明天 08:00 am"),
    (r"हिजो\s+राति", "昨天 22:00 pm"),
    (r"मध्यराति|मध्यरात", "12:00 am"),
    (r"[०-९]+", lambda m: m.group(0).translate(_NE_DIGITS)),
    (r"जनवरी", "1月"),
    (r"फेब्रुअरी", "2月"),
    (r"मार्च", "3月"),
    (r"अप्रिल", "4月"),
    (r"मे", "5月"),
    (r"जुन", "6月"),
    (r"जुलाई", "7月"),
    (r"अगस्ट", "8月"),
    (r"सेप्टेम्बर", "9月"),
    (r"अक्टोबर", "10月"),
    (r"नोभेम्बर", "11月"),
    (r"डिसेम्बर", "12月"),
    (r"अस्ति", "前天"),
    (r"पर्सी", "后天"),
    (r"आज", "今天"),
    (r"हिजो", "昨天"),
    (r"भोलि", "明天"),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+पछि" % _NE_UNIT_RE, _ne_later),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+अघि" % _NE_UNIT_RE, _ne_earlier),
    (r"(?:अहिले|भर्खरै)", "刚刚"),
    (r"अर्को\s+हप्ता", "下周"),
    (r"गत\s+हप्ता", "上周"),
    (r"अर्को\s+महिना", "下个月"),
    (r"गत\s+महिना", "上个月"),
    (r"अर्को\s+वर्ष", "明年"),
    (r"गत\s+वर्ष", "去年"),
]

for _weekday in sorted(_NE_WEEKDAYS, key=len, reverse=True):
    SUB_TRANSLATE.append((_weekday, _NE_WEEKDAYS[_weekday]))
