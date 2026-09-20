# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/5/16


"""
卢旺达语
"""

_RW_WEEKDAYS = {
    'Kuwa mbere': '周一',
    'Kuwa kabiri': '周二',
    'Kuwa gatatu': '周三',
    'Kuwa kane': '周四',
    'Kuwa gatanu': '周五',
    'Kuwa gatandatu': '周六',
    'Ku cyumweru': '周日',
}
_RW_WEEKDAYS_RE = "|".join(sorted(_RW_WEEKDAYS, key=len, reverse=True))

ACCURATE_REGEX_LIST = [
]

SUB_TRANSLATE = [
    (r'(%s)\s+utaha' % _RW_WEEKDAYS_RE,
     lambda m: "下%s" % _RW_WEEKDAYS[m.group(1)]),
    (r'(%s)\s+ushize' % _RW_WEEKDAYS_RE,
     lambda m: "上%s" % _RW_WEEKDAYS[m.group(1)]),
    (r'kuri\s+uyu\s+cyumweru\s+(%s)' % _RW_WEEKDAYS_RE,
     lambda m: "这%s" % _RW_WEEKDAYS[m.group(1)]),
    (r'uyu\s+munsi\s+mu\s+gitondo', '今天 08:00 am'),
    (r'uyu\s+munsi\s+saa\s+sita', '今天 12:00 pm'),
    (r'uyu\s+munsi\s+ku\s+mugoroba', '今天 20:00 pm'),
    (r'uyu\s+munsi\s+nijoro', '今天 22:00 pm'),
    (r'ejo\s+mu\s+gitondo', '明天 08:00 am'),
    (r'ejo\s+hashize\s+nijoro', '昨天 22:00 pm'),
    (r'mu\s+gicuku', '12:00 am'),
    (r'Ukwa gatatu', '3月'),
    (r'Ukwa kane', '4月'),
    (r'Iminota', '分钟'),
    (r'ejo\s+hashize', '昨天'),
    (r'uyu\s+munsi', '今天'),
    (r'ejo', '明天'),
    (r'ubu|none', '刚刚'),
    (r'ibyumweru\s+bitaha', '下周'),
    (r'ibyumweru\s+bishize', '上周'),
    (r'ukwezi\s+gutaha', '下个月'),
    (r'ukwezi\s+gushize', '上个月'),
    (r'umwaka\s+utaha', '明年'),
    (r'umwaka\s+ushize', '去年'),
]

for _weekday in sorted(_RW_WEEKDAYS, key=len, reverse=True):
    SUB_TRANSLATE.append((_weekday.replace(' ', r'\s+'),
                          _RW_WEEKDAYS[_weekday]))

FUZZY_REGEX_LIST = [
    r"(?P<bM>\d+)\s*iraheze",
    r"(?P<bM>\d+)\s*分钟\s*iraheze",
]
