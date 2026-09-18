# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/5/16

"""
土耳其语
"""

ACCURATE_REGEX_LIST = [
]

SUB_TRANSLATE = [
    (r"Ocak", "1月"),
    (r"\bŞubat\b|Şub\.?", "2月"),
    (r"Mart", "3月"),
    (r"Nisan", "4月"),
    (r"Mayıs", "5月"),
    (r"Haziran", "6月"),
    (r"Temmuz", "7月"),
    (r"Ağustos", "8月"),
    (r"Eylül", "9月"),
    (r"Ekim", "10月"),
    (r"Kasım", "11月"),
    (r"Aralık", "12月"),
    (r"saat", "小时"),
    (r"önce", "前"),
    (r"gün", "天"),
    (r"dakika", "分钟"),
    (r"öğleden sonra\s*(?P<H>\d{1,2}):(?P<M>\d{2})",
     lambda m: "%d:%s" % (int(m.group("H")) % 12 + 12, m.group("M"))),
    (r"öğleden önce\s*(?P<H>\d{1,2}):(?P<M>\d{2})",
     lambda m: "%d:%s" % (int(m.group("H")) % 12, m.group("M"))),
]

FUZZY_REGEX_LIST = [
]
