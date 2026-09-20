# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2026/9/18

"""
韩语
"""


_KO_DAY_MAP = {
    "오늘": "今天", "내일": "明天", "어제": "昨天",
    "그저께": "前天", "모레": "后天",
}
_KO_WEEKDAY_MAP = {
    "월": "一", "화": "二", "수": "三", "목": "四",
    "금": "五", "토": "六", "일": "日",
}
_KO_NATIVE_DAY_COUNT = {
    "하루": 1, "이틀": 2, "사흘": 3, "나흘": 4,
    "닷새": 5, "엿새": 6, "이레": 7, "여드레": 8,
    "아흐레": 9, "열흘": 10,
}


def _ko_clock_time(match):
    hour = int(match.group("H"))
    if match.group("half"):
        minute = 30
    else:
        minute = int(match.group("M") or 0)
    if match.group("period") in ("오후", "저녁", "밤"):
        hour = 12 if hour == 12 else (hour + 12 if hour < 12 else hour)
    else:
        hour = 0 if hour == 12 else hour
    return "%s %02d:%02d" % (
        _KO_DAY_MAP[match.group("day")], hour, minute)


def _ko_weekday_clock(match):
    hour = int(match.group("H"))
    if match.group("half"):
        minute = 30
    else:
        minute = int(match.group("M") or 0)
    if match.group("period") in ("오후", "저녁", "밤"):
        hour = 12 if hour == 12 else (hour + 12 if hour < 12 else hour)
    else:
        hour = 0 if hour == 12 else hour
    prefix = match.group("prefix").replace(" ", "")
    direction = {"다음주": "下", "지난주": "上", "이번주": "这", "오는": "下"}[prefix]
    return "%s周%s %02d:%02d" % (
        direction, _KO_WEEKDAY_MAP[match.group(2)], hour, minute)


ACCURATE_REGEX_LIST = []

SUB_TRANSLATE = [
    (r"(?P<day>오늘|내일|어제|그저께|모레)\s*(?P<period>오전|오후|아침|저녁|밤|낮)\s*(?P<H>\d{1,2})\s*시\s*(?:(?P<M>\d{1,2})\s*분?|(?P<half>반))?",
     _ko_clock_time),
    (r"(?P<prefix>다음\s+주|지난\s+주|이번\s+주|오는)\s*([월화수목금토일])(?:요일)?\s*(?P<period>오전|오후|아침|저녁|밤|낮)\s*(?P<H>\d{1,2})\s*시\s*(?:(?P<M>\d{1,2})\s*분?|(?P<half>반))?",
     _ko_weekday_clock),
    (r"(하루|이틀|사흘|나흘|닷새|엿새|이레|여드레|아흐레|열흘)\s*후",
     lambda m: "%s天后" % _KO_NATIVE_DAY_COUNT[m.group(1)]),
    (r"(하루|이틀|사흘|나흘|닷새|엿새|이레|여드레|아흐레|열흘)\s*전",
     lambda m: "%s天前" % _KO_NATIVE_DAY_COUNT[m.group(1)]),
    (r"(?<![A-Za-z0-9])단기\s*(?P<num>\d{1,4})\s*년",
     lambda m: "%s年" % (int(m.group("num")) - 2333)),
    (r"오는\s+([월화수목금토일])(?:요일)?", lambda m: "下%s" % {
        "월": "周一", "화": "周二", "수": "周三", "목": "周四",
        "금": "周五", "토": "周六", "일": "周日"}[m.group(1)]),
    (r"다음\s+주\s+([월화수목금토일])(?:요일)?", lambda m: "下%s" % {
        "월": "周一", "화": "周二", "수": "周三", "목": "周四",
        "금": "周五", "토": "周六", "일": "周日"}[m.group(1)]),
    (r"지난\s+주\s+([월화수목금토일])(?:요일)?", lambda m: "上%s" % {
        "월": "周一", "화": "周二", "수": "周三", "목": "周四",
        "금": "周五", "토": "周六", "일": "周日"}[m.group(1)]),
    (r"이번\s+주\s+([월화수목금토일])(?:요일)?", lambda m: "这%s" % {
        "월": "周一", "화": "周二", "수": "周三", "목": "周四",
        "금": "周五", "토": "周六", "일": "周日"}[m.group(1)]),
    (r"([월화수목금토일])요일", lambda m: "周%s" % {
        "월": "一", "화": "二", "수": "三", "목": "四",
        "금": "五", "토": "六", "일": "日"}[m.group(1)]),
    (r"오늘\s+아침", "今天 08:00 am"),
    (r"오늘\s+저녁|오늘\s+밤", "今天 20:00 pm"),
    (r"내일\s+아침", "明天 08:00 am"),
    (r"내일\s+저녁|내일\s+밤", "明天 20:00 pm"),
    (r"어제\s+저녁|어제\s+밤", "昨天 20:00 pm"),
    (r"정오", "12:00 pm"),
    (r"자정", "12:00 am"),
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
