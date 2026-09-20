# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/5/16

"""
斯瓦希里语
"""

ACCURATE_REGEX_LIST = [
]

SUB_TRANSLATE = [
    (r'Januari', '1月'),
    (r'Februari', '2月'),
    (r'Machi', '3月'),
    (r'Aprili', '4月'),
    (r'Mei', '5月'),
    (r'Juni', '6月'),
    (r'Julai', '7月'),
    (r'Agosti', '8月'),
    (r'Septemba', '9月'),
    (r'Oktoba', '10月'),
    (r'Novemba', '11月'),
    (r'Desemba', '12月'),
    (r'juzi', '前天'),
    (r'kesho\s+kutwa', '后天'),
    (r'jana', '昨天'),
    (r'leo', '今天'),
    (r'kesho', '明天'),
    (r'sasa|hivi\s+punde', '刚刚'),
    (r'baada\s+ya\s+(?P<num>\d+)\s*(?P<unit>sekunde|dakika|saa|siku|wiki|mwezi|mwaka)',
     lambda m: "%s%s后" % (
         m.group("num"),
         {"sekunde": "秒", "dakika": "分钟", "saa": "小时",
          "siku": "天", "wiki": "周", "mwezi": "月",
          "mwaka": "年"}[m.group("unit")])),
    (r'baada\s+ya\s+(?P<unit>sekunde|dakika|saa|siku|wiki|mwezi|mwaka)\s+(?P<num>\d+)',
     lambda m: "%s%s后" % (
         m.group("num"),
         {"sekunde": "秒", "dakika": "分钟", "saa": "小时",
          "siku": "天", "wiki": "周", "mwezi": "月",
          "mwaka": "年"}[m.group("unit")])),
    (r'(?P<num>\d+)\s*(?P<unit>sekunde|dakika|saa|siku|wiki|mwezi|mwaka)\s+baadaye',
     lambda m: "%s%s后" % (
         m.group("num"),
         {"sekunde": "秒", "dakika": "分钟", "saa": "小时",
          "siku": "天", "wiki": "周", "mwezi": "月",
          "mwaka": "年"}[m.group("unit")])),
    (r'wiki\s+ijayo', '下周'),
    (r'wiki\s+iliyopita', '上周'),
    (r'mwezi\s+ujao', '下个月'),
    (r'mwezi\s+uliopita', '上个月'),
    (r'mwaka\s+ujao', '明年'),
    (r'mwaka\s+uliopita', '去年'),
]

FUZZY_REGEX_LIST = [
    r"Saa\s*(?P<bH>\d+)\s*zilizopita\s*",
    r"Saa\s*(?P<bH>\d+)\s*iliyopita\s*",
    r"Dakika\s*(?P<bM>\d+)\s*zilizopita\s*",
]
