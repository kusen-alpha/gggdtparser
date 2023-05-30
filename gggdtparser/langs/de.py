# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/5/16


"""
德语
"""

ACCURATE_REGEX_LIST = [
]

SUB_TRANSLATE = [
    (r"Januar|Jan", "1月"),
    (r"Februar|Feb\.", "2月"),
    (r"März|Mär", "3月"),
    (r"April|Apr", "4月"),
    (r"Abriil|Abr", "4月"),
    (r"Mai|mai", "5月"),
    (r"Juni|Jun", "6月"),
    (r"Juli|Jnl", "7月"),
    (r"August|Aug", "8月"),
    (r"September|Sep\.", "9月"),
    (r"Oktober|Okt", "10月"),
    (r"November|Nov", "11月"),
    (r"Dezember|Dez", "12月"),
    (r"Uhr", "am"),
    (r"une heure", "1 heure"),
    (r"il y a heure", "il y a 1 heure"),
]
FUZZY_REGEX_LIST = []