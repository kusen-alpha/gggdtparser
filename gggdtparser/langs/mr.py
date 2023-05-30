# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/5/16


"""
马拉地语
"""

ACCURATE_REGEX_LIST = [
    r"(?P<bM>\d+)\s*तासांपूर्वी",
    r"(?P<bM>\d+)\s*मिनिटांपूर्व",
]

SUB_TRANSLATE = [
    (r'एप्रिल', '4月')
]
FUZZY_REGEX_LIST = []