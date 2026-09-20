# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2026/9/18

"""
韩语
"""

ACCURATE_REGEX_LIST = []

SUB_TRANSLATE = [
    (r"그저께", "前天"),
    (r"모레", "后天"),
    (r"오늘", "今天"),
    (r"어제", "昨天"),
    (r"내일", "明天"),
    (r"내년", "明年"),
    (r"작년", "去年"),
    (r"지금|방금", "刚刚"),
    (r"(?P<num>\d+)\s*초\s*후", lambda m: "%s秒后" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*분\s*후", lambda m: "%s分钟后" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*시간\s*후", lambda m: "%s小时后" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*일\s*후", lambda m: "%s天后" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*주\s*후", lambda m: "%s周后" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*개월\s*후", lambda m: "%s月后" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*년\s*후", lambda m: "%s年后" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*초\s*전", lambda m: "%s秒前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*분\s*전", lambda m: "%s分钟前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*시간\s*전", lambda m: "%s小时前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*일\s*전", lambda m: "%s天前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*주\s*전", lambda m: "%s周前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*개월\s*전", lambda m: "%s月前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*년\s*전", lambda m: "%s年前" % int(m.group("num"))),
    (r"다음\s+주\b|다음주\b", "下周"),
    (r"지난\s+주\b|지난주\b", "上周"),
    (r"다음\s+달\b|다음달\b", "下个月"),
    (r"지난\s+달\b|지난달\b", "上个月"),
    (r"오후", "pm"),
    (r"오전", "am"),
    (r"년|年", "年"),
    (r"월|月", "月"),
    (r"일|日", "日"),
    (r"시", "时"),
    (r"분", "分"),
    (r"초", "秒"),
]

FUZZY_REGEX_LIST = []
