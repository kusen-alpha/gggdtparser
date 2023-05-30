# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/5/16


"""
越南语
"""

ACCURATE_REGEX_LIST = [
    "(?P<d>\d{1,2})\s*[\-\|/\.月]\s*(?P<m>\d{1,2})\s*[\-\|/\.年]\s*(?P<Y>\d{2,4})"
    # 29 tháng 3 năm 2023
]

SUB_TRANSLATE = [
    (r"phút", "分钟"),
    (r"trước", "前"),
    (r"giờ", "小时"),
    (r"tháng", "月"),
    (r"năm", "年"),
]
FUZZY_REGEX_LIST = []