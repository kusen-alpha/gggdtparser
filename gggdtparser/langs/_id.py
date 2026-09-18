# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/5/16


"""
印尼语
"""

ACCURATE_REGEX_LIST = [

]

SUB_TRANSLATE = [
    (r"\bJanuari\b", "1月"),
    (r"\bFebruari\b", "2月"),
    (r"Maret", "3月"),
    (r"April", "4月"),
    (r"Mei", "5月"),
    (r"Juni", "6月"),
    (r"Juli", "7月"),
    (r"Agustus", "8月"),
    (r"September", "9月"),
    (r"Oktober", "10月"),
    (r"November", "11月"),
    (r"Desember", "12月"),
    (r"Senin", ""),
    (r"Selasa", ""),
    (r"Rabu", ""),
    (r"Kamis", ""),
    (r"Jumat", ""),
    (r"Sabtu", ""),
    (r"Minggu", ""),
    (r"(?P<d>\d{1,2})\s+(?P<m>\d{1,2})\s*月\s+(?P<Y>\d{4})\s+(?P<H>\d{1,2})\.(?P<M>\d{2})",
     lambda m: "%s %s月 %s %s:%s" % (
         m.group("d"), m.group("m"), m.group("Y"),
         m.group("H"), m.group("M"))),
    (r"(?P<num>\d+)\s*jam\s+yang\s+lalu",
     lambda m: "%s小时前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*menit\s+yang\s+lalu",
     lambda m: "%s分钟前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*hari\s+yang\s+lalu",
     lambda m: "%s天前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*minggu\s+yang\s+lalu",
     lambda m: "%s周前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*bulan\s+yang\s+lalu",
     lambda m: "%s月前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*tahun\s+yang\s+lalu",
     lambda m: "%s年前" % int(m.group("num"))),
    (r"baru saja", "刚刚"),
    (r"hari ini", "今天"),
    (r"kemarin", "昨天"),
]
FUZZY_REGEX_LIST = [
    r"(?P<bH>\d+)\s*jam\s*yang\s*lalu",
    r"(?P<bM>\d+)\s*menit\s*yang\s*lalu",
    r"(?P<bd>\d+)\s*hari\s*yang\s*lalu",
    r"(?P<ba>\d+)\s*minggu\s*yang\s*lalu",
    r"(?P<bm>\d+)\s*bulan\s*yang\s*lalu",
    r"(?P<bY>\d+)\s*tahun\s*yang\s*lalu",
]
