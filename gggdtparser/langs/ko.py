# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2026/9/18

"""
韩语
"""

ACCURATE_REGEX_LIST = []

SUB_TRANSLATE = [
    (r"년|年", "年"),
    (r"월|月", "月"),
    (r"일|日", "日"),
    (r"시간 전", "小时前"),
    (r"분 전", "分钟前"),
    (r"초 전", "秒前"),
    (r"시", "时"),
    (r"분", "分"),
    (r"초", "秒"),
    (r"오늘", "今天"),
    (r"어제", "昨天"),
    (r"오후", "pm"),
    (r"오전", "am"),
]

FUZZY_REGEX_LIST = []
