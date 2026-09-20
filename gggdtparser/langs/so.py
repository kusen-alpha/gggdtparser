# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/5/16


"""
索马里语
"""

ACCURATE_REGEX_LIST = [
    r"(?P<bH>\d+)\s*Saacadood?\s*",
]

SUB_TRANSLATE = [
    (r'Janaayo', '1月'),
    (r'Febraayo', '2月'),
    (r'Maarso', '3月'),
    (r'Abriil', '4月'),
    (r'Maajo', '5月'),
    (r'Juun', '6月'),
    (r'Luuliyo', '7月'),
    (r'Agoosto', '8月'),
    (r'Sebitembar', '9月'),
    (r'Oktoobar', '10月'),
    (r'Nofeembar', '11月'),
    (r'Diseembar', '12月'),
    (r'shalay', '昨天'),
    (r'maanta', '今天'),
    (r'berri', '明天'),
    (r'hadda|isla hadda', '刚刚'),
    (r'(?P<num>\d+)\s*(?P<unit>daqiiqo|saacad|saacadood|maalin|maalmood|toddobaad|bil|bilood|sano)\s+ka\s+dib',
     lambda m: "%s%s后" % (
         m.group("num"),
         {"daqiiqo": "分钟", "saacad": "小时", "saacadood": "小时",
          "maalin": "天", "maalmood": "天", "toddobaad": "周",
          "bil": "月", "bilood": "月", "sano": "年"}[m.group("unit")])),
    (r'(?P<num>\d+)\s*(?P<unit>daqiiqo|saacad|saacadood|maalin|maalmood|toddobaad|bil|bilood|sano)\s+ka\s+hor',
     lambda m: "%s%s前" % (
         m.group("num"),
         {"daqiiqo": "分钟", "saacad": "小时", "saacadood": "小时",
          "maalin": "天", "maalmood": "天",
          "toddobaad": "周", "bil": "月", "bilood": "月",
          "sano": "年"}[m.group("unit")])),
    (r'toddobaadka\s+soo\s+socda', '下周'),
    (r'toddobaadkii\s+hore', '上周'),
    (r'bisha\s+soo\s+socota', '下个月'),
    (r'bishii\s+hore', '上个月'),
    (r'sanadka\s+soo\s+socda', '明年'),
    (r'sanadkii\s+hore', '去年'),
]
FUZZY_REGEX_LIST = []
