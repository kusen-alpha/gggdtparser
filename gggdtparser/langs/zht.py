# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/5/16


"""
繁体/中国台湾等
"""

ACCURATE_REGEX_LIST = [
    r"民国\s*(?P<mgY>\d+)[\-\|/\.年]\s*(?P<m>\d+)[\-\|/\.月]\s*(?P<d>\d+)[日]?",
    r"民国\s*(?P<mgY>\d+)[\-\|/\.年]\s*(?P<m>\d+)[\-\|/\.月]?",
    r"民国(?P<mgY>\d+)[年]?",
    r"(?P<mgY>\d{3})\s*[\-\|/\.年]\s*(?P<m>\d{1,2})\s*[\-\|/\.月]\s*(?P<d>\d{1,2})\s*[日]?",
    r"(?P<bH>\d+)\s*时间前",
]

SUB_TRANSLATE = [
    (r'時', '时'),
    (r'間', '间'),
    (r'國', '国'),
    (r'鐘', '钟'),
    (r'個', '个'),
]
FUZZY_REGEX_LIST = []