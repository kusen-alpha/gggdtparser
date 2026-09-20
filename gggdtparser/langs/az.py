# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/4/20

"""
阿塞拜疆语
"""

_AZ_WEEKDAYS = {
    "bazar ertəsi": "周一",
    "çərşənbə axşamı": "周二",
    "çərşənbə": "周三",
    "cümə axşamı": "周四",
    "cümə": "周五",
    "şənbə": "周六",
    "bazar": "周日",
}
_AZ_WEEKDAYS_RE = "|".join(sorted(_AZ_WEEKDAYS, key=len, reverse=True))

ACCURATE_REGEX_LIST = [

]
FUZZY_REGEX_LIST = []
SUB_TRANSLATE = [
    (r"(?i)\bgələn\s+(%s)\b" % _AZ_WEEKDAYS_RE,
     lambda m: "下%s" % _AZ_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\bkeçən\s+(%s)\b" % _AZ_WEEKDAYS_RE,
     lambda m: "上%s" % _AZ_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\bbu\s+(%s)\b" % _AZ_WEEKDAYS_RE,
     lambda m: "这%s" % _AZ_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\bbu\s+gün\s+səhər\b", "今天 08:00 am"),
    (r"(?i)\bbu\s+gün\s+günorta\b", "今天 12:00 pm"),
    (r"(?i)\bbu\s+gün\s+günortadan\s+sonra\b", "今天 15:00 pm"),
    (r"(?i)\bbu\s+gün\s+axşam\b", "今天 20:00 pm"),
    (r"(?i)\bbu\s+gün\s+gecə\b", "今天 22:00 pm"),
    (r"(?i)\bsabah\s+səhər\b", "明天 08:00 am"),
    (r"(?i)\bdünən\s+axşam\b", "昨天 20:00 pm"),
    (r"(?i)\bgecə\s+yarısı\b", "12:00 am"),
    (r"(?i)\bgünorta\b", "12:00 pm"),
    (r'Yanvar', '1月'),
    (r'Fevral', '2月'),
    (r'Mart', '3月'),
    (r'Aprel', '4月'),
    (r'May', '5月'),
    (r'İyun', '6月'),
    (r'İyul', '7月'),
    (r'Avqust', '8月'),
    (r'Sentyabr', '9月'),
    (r'Oktyabr', '10月'),
    (r'Noyabr', '11月'),
    (r'Dekabr', '12月'),
    (r'dünən', '昨天'),
    (r'bu\s+gün', '今天'),
    (r'sabah', '明天'),
    (r'srağagün', '后天'),
    (r'indi|elə\s+indi', '刚刚'),
    (r'(?P<num>\d+)\s*(?:saat|小时)\s+sonra', lambda m: "%s小时后" % int(m.group("num"))),
    (r'(?P<num>\d+)\s*dəqiqə\s+sonra', lambda m: "%s分钟后" % int(m.group("num"))),
    (r'(?P<num>\d+)\s*gün\s+sonra', lambda m: "%s天后" % int(m.group("num"))),
    (r'(?P<num>\d+)\s*həftə\s+sonra', lambda m: "%s周后" % int(m.group("num"))),
    (r'(?P<num>\d+)\s*ay\s+sonra', lambda m: "%s月后" % int(m.group("num"))),
    (r'(?P<num>\d+)\s*il\s+sonra', lambda m: "%s年后" % int(m.group("num"))),
    (r'(?P<num>\d+)\s*dəqiqə\s+əvvəl', lambda m: "%s分钟前" % int(m.group("num"))),
    (r'(?P<num>\d+)\s*gün\s+əvvəl', lambda m: "%s天前" % int(m.group("num"))),
    (r'(?P<num>\d+)\s*həftə\s+əvvəl', lambda m: "%s周前" % int(m.group("num"))),
    (r'(?P<num>\d+)\s*ay\s+əvvəl', lambda m: "%s月前" % int(m.group("num"))),
    (r'(?P<num>\d+)\s*il\s+əvvəl', lambda m: "%s年前" % int(m.group("num"))),
    (r'gələn\s+həftə', '下周'),
    (r'keçən\s+həftə', '上周'),
    (r'gələn\s+ay', '下个月'),
    (r'keçən\s+ay', '上个月'),
    (r'gələn\s+il', '明年'),
    (r'keçən\s+il', '去年'),
    (r'əvvəl', '前'),
    (r'saat', '小时'),
]

for _weekday in sorted(_AZ_WEEKDAYS, key=len, reverse=True):
    SUB_TRANSLATE.append((r"(?i)\b%s\b" % _weekday,
                          _AZ_WEEKDAYS[_weekday]))
