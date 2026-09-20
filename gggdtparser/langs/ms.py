# -*- coding:utf-8 -*-

"""
马来语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_MS_UNITS = {
    "saat": "秒", "minit": "分钟", "jam": "小时",
    "hari": "天", "minggu": "周", "bulan": "月", "tahun": "年",
}

SUB_TRANSLATE = [
    (r"\bJanuari\b", "1月"),
    (r"\bFebruari\b", "2月"),
    (r"\bMac\b", "3月"),
    (r"\bApril\b", "4月"),
    (r"\bMei\b", "5月"),
    (r"\bJun\b", "6月"),
    (r"\bJulai\b", "7月"),
    (r"\bOgos\b", "8月"),
    (r"\bSeptember\b", "9月"),
    (r"\bOktober\b", "10月"),
    (r"\bNovember\b", "11月"),
    (r"\bDisember\b", "12月"),
    (r"\bkelmarin\b", "前天"),
    (r"\blusa\b", "后天"),
    (r"\bhari\s+ini\b", "今天"),
    (r"\bsemalam\b", "昨天"),
    (r"\besok\b", "明天"),
    (r"dalam\s+(?P<num>\d+)\s*(?P<unit>saat|minit|jam|hari|minggu|bulan|tahun)",
     lambda m: "%s%s后" % (
         m.group("num"), _MS_UNITS[m.group("unit")])),
    (r"(?P<num>\d+)\s*(?P<unit>saat|minit|jam|hari|minggu|bulan|tahun)\s+lalu",
     lambda m: "%s%s前" % (
         m.group("num"), _MS_UNITS[m.group("unit")])),
    (r"\b(?:sekarang|baru\s+sahaja)\b", "刚刚"),
    (r"\bminggu\s+depan\b", "下周"),
    (r"\bminggu\s+lepas\b", "上周"),
    (r"\bbulan\s+depan\b", "下个月"),
    (r"\bbulan\s+lepas\b", "上个月"),
    (r"\btahun\s+depan\b", "明年"),
    (r"\btahun\s+lepas\b", "去年"),
]
