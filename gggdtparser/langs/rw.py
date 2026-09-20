# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/5/16


"""
卢旺达语
"""

ACCURATE_REGEX_LIST = [
]

SUB_TRANSLATE = [
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
FUZZY_REGEX_LIST = [
    r"(?P<bM>\d+)\s*iraheze",
    r"(?P<bM>\d+)\s*分钟\s*iraheze",
]
