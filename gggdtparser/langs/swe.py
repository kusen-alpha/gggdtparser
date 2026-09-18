# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/5/16


"""
葡萄牙语
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
    (r"(de)?\s*janeiro\s*(de)?", "1月"),
    (r"Fev\.?", "2月"),
    (r"(de)?\s*fevereiro\s*(de)?", "2月"),
    (r"(de)?\s*março\s*(de)?", "3月"),
    (r"(de)?\s*abril\s*(de)?", "4月"),
    (r"(de)?\s*maio\s*(de)?", "5月"),
    (r"(de)?\s*junho\s*(de)?", "6月"),
    (r"(de)?\s*julho\s*(de)?", "7月"),
    (r"(de)?\s*agosto\s*(de)?", "8月"),
    (r"(de)?\s*setembro\s*(de)?", "9月"),
    (r"(de)?\s*outubro\s*(de)?", "10月"),
    (r"(de)?\s*novembro\s*(de)?", "11月"),
    (r"(de)?\s*dezembro\s*(de)?", "12月"),
]
FUZZY_REGEX_LIST = []
