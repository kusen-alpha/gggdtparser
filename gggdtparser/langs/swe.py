# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/5/16


"""
瑞典语
"""

ACCURATE_REGEX_LIST = [
    r"(?P<bS>\d+)\s*segundos?\s*",
    r"(?P<bM>\d+)\s*minutos?\s*",
    r"(?P<bH>\d+)\s*horas?\s*",
    r"(?P<bd>\d+)\s*dias?\s*",
    r"(?P<bm>\d+)\s*meses?\s*",
    r"(?P<ba>\d+)\s*semanas?\s*",
    r"(?P<bY>\d+)\s*anos?\s*",
]

SUB_TRANSLATE = [
    (r"janeiro", "1月"),
    (r"fevereiro", "2月"),
    (r"março", "3月"),
    (r"abril", "4月"),
    (r"maio", "5月"),
    (r"junho", "6月"),
    (r"julho", "7月"),
    (r"agosto", "8月"),
    (r"setembro", "9月"),
    (r"outubro", "10月"),
    (r"novembro", "11月"),
    (r"dezembro", "12月"),
]
FUZZY_REGEX_LIST = []