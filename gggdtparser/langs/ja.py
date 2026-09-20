# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/5/16

"""
日语
"""


def _ja_clock_time(match):
    part = match.group("part")
    hour = int(match.group("H"))
    if match.group("half"):
        minute = 30
    else:
        minute = int(match.group("M") or 0)
    if "一昨日" in part:
        day = "前天"
    elif "明後日" in part or "明日" in part or "明朝" in part:
        day = "明天"
    elif "昨日" in part or "昨夜" in part:
        day = "昨天"
    else:
        day = "今天"
    if any(p in part for p in ("午後", "夕方", "夜")) \
            or part in ("今夜", "今晩", "昨夜"):
        hour = 12 if hour == 12 else (hour + 12 if hour < 12 else hour)
    else:
        hour = 0 if hour == 12 else hour
    return "%s %02d:%02d" % (day, hour, minute)


_JA_WEEKDAY_MAP = {
    "月": "一", "火": "二", "水": "三", "木": "四",
    "金": "五", "土": "六", "日": "日",
}


def _ja_noon(match):
    day = match.group("day")
    return {
        "今日": "今天", "明日": "明天", "昨日": "昨天",
        "一昨日": "前天", "明後日": "后天",
    }[day] + " 12:00"


def _ja_period_clock_time(match):
    hour = int(match.group("H"))
    if match.group("half"):
        minute = 30
    else:
        minute = int(match.group("M") or 0)
    if match.group("period") in ("午後", "夕方", "夜"):
        hour = 12 if hour == 12 else (hour + 12 if hour < 12 else hour)
    else:
        hour = 0 if hour == 12 else hour
    return "%02d:%02d" % (hour, minute)


ACCURATE_REGEX_LIST = [
]

SUB_TRANSLATE = [
    (r"再来週の([月火水木金土日])曜日", lambda m: "下下周%s" % _JA_WEEKDAY_MAP[m.group(1)]),
    (r"(?:先々週|先先週)の([月火水木金土日])曜日", lambda m: "上上周%s" % _JA_WEEKDAY_MAP[m.group(1)]),
    (r"再来週|再々週", "下下周"),
    (r"先々週|先先週", "上上周"),
    (r"来週の(?:[月火水木金土日])曜日", lambda m: "下%s" % {
        "月": "周一", "火": "周二", "水": "周三", "木": "周四",
        "金": "周五", "土": "周六", "日": "周日"}[m.group(0)[3]]),
    (r"次の(?:[月火水木金土日])曜日", lambda m: "下%s" % {
        "月": "周一", "火": "周二", "水": "周三", "木": "周四",
        "金": "周五", "土": "周六", "日": "周日"}[m.group(0)[2]]),
    (r"先週の(?:[月火水木金土日])曜日", lambda m: "上%s" % {
        "月": "周一", "火": "周二", "水": "周三", "木": "周四",
        "金": "周五", "土": "周六", "日": "周日"}[m.group(0)[3]]),
    (r"今週の(?:[月火水木金土日])曜日", lambda m: "这%s" % {
        "月": "周一", "火": "周二", "水": "周三", "木": "周四",
         "金": "周五", "土": "周六", "日": "周日"}[m.group(0)[3]]),
    (r"(?:[月火水木金土日])曜日?",
     lambda m: "周%s" % {
         "月": "一", "火": "二", "水": "三", "木": "四",
         "金": "五", "土": "六", "日": "日"}[m.group(0)[0]]),
    (r"(?P<part>(?:今日|明日|昨日|一昨日|明後日)の(?:午前|午後|朝|夕方|夜)|今朝|明朝|今夜|今晩|昨夜)\s*(?P<H>\d{1,2})\s*時\s*(?:(?P<M>\d{1,2})\s*分?|(?P<half>半))?",
     _ja_clock_time),
    (r"の\s*(?P<period>午前|午後|朝|夕方|夜)\s*(?P<H>\d{1,2})\s*時\s*(?:(?P<M>\d{1,2})\s*分?|(?P<half>半))?",
     _ja_period_clock_time),
    (r"(?P<day>今日|明日|昨日|一昨日|明後日)の正午", _ja_noon),
    (r"今朝", "今天 08:00 am"),
    (r"今日の朝", "今天 08:00 am"),
    (r"今日の午後", "今天 15:00 pm"),
    (r"今夜|今晩", "今天 22:00 pm"),
    (r"明日の朝|明朝", "明天 08:00 am"),
    (r"明日の夜", "明天 20:00 pm"),
    (r"昨日の夜|昨夜", "昨天 22:00 pm"),
    (r"正午", "12:00 pm"),
    (r"深夜|真夜中", "12:00 am"),
    (r'\(月\)|\(火\)|\(水\)|\(木\)|\(金\)|\(土\)|\(日\)', ''),
    (r'か', '个'),
    (r"(?<![A-Za-z0-9])R\s*(?P<num>\d{1,2})\s*年\s*(?P<m>\d{1,2})\s*月\s*(?P<d>\d{1,2})日?",
     lambda m: "%s年%s月%s日" % (
         2018 + int(m.group("num")),
         m.group("m").lstrip("0") or "1",
         m.group("d").lstrip("0") or "1")),
    (r"(?<![A-Za-z0-9])R\s*(?P<num>\d{1,2})(?:[\-\/\.]\s*(?P<m>\d{1,2})[\-\/\.]\s*(?P<d>\d{1,2}))?(?!\d)",
     lambda m: (
         "%s年" % (2018 + int(m.group("num")))
         if not m.group("m") else
         "%s年%s月%s日" % (
             2018 + int(m.group("num")),
             m.group("m").lstrip("0") or "1",
             m.group("d").lstrip("0") or "1"))),
    (r"令和\s*(\d+)年", lambda m: "%s年" % (2018 + int(m.group(1)))),
    (r"平成\s*(\d+)年", lambda m: "%s年" % (1988 + int(m.group(1)))),
    (r"昭和\s*(\d+)年", lambda m: "%s年" % (1925 + int(m.group(1)))),
    (r"大正\s*(\d+)年", lambda m: "%s年" % (1911 + int(m.group(1)))),
    (r"明治\s*(\d+)年", lambda m: "%s年" % (1867 + int(m.group(1)))),
    (r"午前\s*(?P<H>\d{1,2})\s*時半",
     lambda m: "%d:%02d am" % (int(m.group("H")) % 12, 30)),
    (r"午後\s*(?P<H>\d{1,2})\s*時半",
     lambda m: "%d:%02d pm" % (int(m.group("H")) % 12 + 12, 30)),
    (r"(?P<num>\d+)\s*(?:秒|秒間)\s*後", lambda m: "%s秒后" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*分\s*後", lambda m: "%s分钟后" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*時間\s*後", lambda m: "%s小时后" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*日\s*後", lambda m: "%s天后" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*(?:週間|週)\s*後", lambda m: "%s周后" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*(?:ヶ月|か月|个?月)\s*後", lambda m: "%s月后" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*年\s*後", lambda m: "%s年后" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*秒\s*前", lambda m: "%s秒前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*分\s*前", lambda m: "%s分钟前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*時間\s*前", lambda m: "%s小时前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*日\s*前", lambda m: "%s天前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*(?:週間|週)\s*前", lambda m: "%s周前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*(?:ヶ月|か月|个?月)\s*前", lambda m: "%s月前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*年\s*前", lambda m: "%s年前" % int(m.group("num"))),
    (r"(?P<H>\d{1,2})\s*時半", lambda m: "%d:30" % int(m.group("H"))),
    (r"(?P<H>\d{1,2})\s*時\s*(?P<M>\d{1,2})\s*分?",
     lambda m: "%d:%02d" % (int(m.group("H")), int(m.group("M")))),
    (r"(?P<H>\d{1,2})\s*時", lambda m: "%d:00" % int(m.group("H"))),
    (r"午前", " am"),
    (r"午後", " pm"),
    (r"\s*(?P<apm>am|pm)(?P<time>\d{1,2}:\d{2}(?::\d{2})?)",
     lambda m: "%s %s" % (m.group("time"), m.group("apm"))),
    (r"一昨日|おととい|おとつい", "前天"),
    (r"明後日|あさって", "后天"),
    (r"今日|きょう", "今天"),
    (r"昨日|きのう", "昨天"),
    (r"明日|あした|あす", "明天"),
    (r"たった今|いま", "刚刚"),
    (r"来週", "下周"),
    (r"先週", "上周"),
    (r"来月", "下个月"),
    (r"先月", "上个月"),
    (r"来年", "明年"),
    (r"去年", "去年"),
]

FUZZY_REGEX_LIST = [
]
