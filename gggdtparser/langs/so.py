# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/5/16


"""
索马里语
"""

_SO_WEEKDAYS = {
    'Isniin': '周一',
    'Talaado': '周二',
    'Arbaco': '周三',
    'Khamiis': '周四',
    'Jimce': '周五',
    'Sabti': '周六',
    'Axad': '周日',
}
_SO_WEEKDAYS_RE = "|".join(sorted(_SO_WEEKDAYS, key=len, reverse=True))

_SO_WEEKDAYS_NEXT = {
    'Isniinta': '周一', 'Talaadada': '周二', 'Arbacada': '周三',
    'Khamiista': '周四', 'Jimcaha': '周五', 'Sabtida': '周六',
    'Axadda': '周日',
}
_SO_WEEKDAYS_NEXT_RE = "|".join(
    sorted(_SO_WEEKDAYS_NEXT, key=len, reverse=True))

_SO_WEEKDAYS_PAST = {
    'Isniintii': '周一', 'Talaadadii': '周二', 'Arbacidii': '周三',
    'Khamiistii': '周四', 'Jimcihii': '周五', 'Sabtidii': '周六',
    'Axaddii': '周日',
}
_SO_WEEKDAYS_PAST_RE = "|".join(
    sorted(_SO_WEEKDAYS_PAST, key=len, reverse=True))

ACCURATE_REGEX_LIST = [
    r"(?P<bH>\d+)\s*Saacadood?\s*",
]

SUB_TRANSLATE = [
    (r'(%s)\s+soo\s+socota' % _SO_WEEKDAYS_NEXT_RE,
     lambda m: "下%s" % _SO_WEEKDAYS_NEXT[m.group(1)]),
    (r'(%s)\s+hore' % _SO_WEEKDAYS_PAST_RE,
     lambda m: "上%s" % _SO_WEEKDAYS_PAST[m.group(1)]),
    (r'Isniintan', '这周一'),
    (r'\bsubaxaan\b', '今天 08:00 am'),
    (r'\bcaawa\b', '今天 20:00 pm'),
    (r'\bgalabta\b', '今天 15:00 pm'),
    (r'maanta\s+subax', '今天 08:00 am'),
    (r'maanta\s+duhurka', '今天 12:00 pm'),
    (r'maanta\s+galab', '今天 15:00 pm'),
    (r'maanta\s+fiid', '今天 20:00 pm'),
    (r'maanta\s+habeen', '今天 22:00 pm'),
    (r'berri\s+subax', '明天 08:00 am'),
    (r'shalay\s+habeen', '昨天 22:00 pm'),
    (r'saqda\s+dhexe', '12:00 am'),
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

for _weekday in sorted(_SO_WEEKDAYS, key=len, reverse=True):
    SUB_TRANSLATE.append((_weekday, _SO_WEEKDAYS[_weekday]))

FUZZY_REGEX_LIST = []
