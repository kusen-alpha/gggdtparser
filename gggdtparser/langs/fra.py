# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/5/16


"""
法语
"""

ACCURATE_REGEX_LIST = [
    # 31/03/23 à 12h03
    r"(?P<d>\d{1,2})\s*[\-\|/\.日]\s*(?P<m>\d{1,2})\s*[\-\|/\.月]\s*(?P<Y>\d{2,4})\s*[,]?\s*(?P<H>\d{1,2})\s*[:时h\.]\s*(?P<M>\d{1,2})\s*[:分]?",

    # before
    r"(il y a)?\s*(?P<bH>\d+)\s*heures?\s*(ago)?",
]

SUB_TRANSLATE = [
    (r"janvier|jan\.", "1月"),
    (r"février|fev\.", "2月"),
    (r"mars\.|mars", "3月"),
    (r"avril|avr\.", "4月"),
    (r"mai\.|mai", "5月"),
    (r"juin\.|juin", "6月"),
    (r"juillet\.|juil\.|juillet", "7月"),
    (r"aout\.|août", "8月"),
    (r"septembre|sept\.", "9月"),
    (r"octobre|oct\.", "10月"),
    (r"novembre|nov\.", "11月"),
    (r"décembre|dec\.", "12月"),
    (r"aujourd’hui à", ""),
    (r"à l’instant", "刚刚"),
    (r"hier à", "昨天"),
    (r"à", ""),
]
FUZZY_REGEX_LIST = []