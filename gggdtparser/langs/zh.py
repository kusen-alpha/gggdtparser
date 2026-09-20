# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/5/16

"""
中文
"""


def _cn_period_hour(match):
    part = match.group("part")
    hour = int(match.group("H"))
    if match.group("half"):
        minute = 30
    else:
        minute = int(match.group("M") or 0)
    if "明" in part:
        day = "明天"
    elif "昨" in part:
        day = "昨天"
    elif "前" in part:
        day = "前天"
    elif "后" in part:
        day = "后天"
    elif any(k in part for k in ("今天", "今晚", "今夜", "今早")):
        day = "今天"
    else:
        day = None
    if any(p in part for p in ("晚上", "夜里", "夜间", "深夜")) \
            or part in ("今晚", "今夜", "明晚", "昨晚"):
        hour = 0 if hour == 12 else (hour + 12 if hour < 12 else hour)
    elif any(p in part for p in ("下午", "傍晚")):
        hour = 12 if hour == 12 else (hour + 12 if hour < 12 else hour)
    elif "中午" in part:
        pass
    elif "午夜" in part or "半夜" in part:
        hour = 0 if hour == 12 else hour
    else:
        hour = 0 if hour == 12 else hour
    if day is None:
        return " %02d:%02d" % (hour, minute)
    return "%s %02d:%02d" % (day, hour, minute)


ACCURATE_REGEX_LIST = [

]

SUB_TRANSLATE = [
    (r"(?P<part>(?:今天|明天|昨天|前天|后天)(?:凌晨|清晨|早上|早晨|上午|中午|下午|傍晚|晚上|夜里|夜间|深夜)?|今晚|今夜|明晚|昨晚|今早)\s*(?P<H>\d{1,2})\s*[点时]\s*(?:(?P<M>\d{1,2})\s*分?|(?P<half>半))?",
     _cn_period_hour),
    (r"(?P<part>凌晨|清晨|早上|早晨|上午|中午|下午|傍晚|晚上|夜里|夜间|深夜|午夜|半夜)\s*(?P<H>\d{1,2})\s*[点时]\s*(?:(?P<M>\d{1,2})\s*分?|(?P<half>半))?",
     _cn_period_hour),
    (r'星期([一二三四五六日天])', lambda m: "周%s" % m.group(1)),
    (r'周([一二三四五六日天])', lambda m: "周%s" % m.group(1)),
    (r'禮拜([一二三四五六日天])', lambda m: "周%s" % m.group(1)),
    (r'礼拜([一二三四五六日天])', lambda m: "周%s" % m.group(1)),
    (r"今晚|今天晚上", "今天 22:00 pm"),
    (r"今天早上|今早", "今天 08:00 am"),
    (r"今天中午", "今天 12:00 pm"),
    (r"今天下午", "今天 15:00 pm"),
    (r"明天早上|明早", "明天 08:00 am"),
    (r"明天上午", "明天 09:00 am"),
    (r"明天中午", "明天 12:00 pm"),
    (r"明天下午", "明天 15:00 pm"),
    (r"明天晚上|明晚", "明天 20:00 pm"),
    (r"昨天晚上|昨晚", "昨天 22:00 pm"),
    (r"昨天早上", "昨天 08:00 am"),
    (r"前天晚上", "前天 22:00 pm"),
    (r"后天早上", "后天 08:00 am"),
    (r"半小时后|半个小时后|再过半小时", "30分钟后"),
    (r"半小时前|半个小时前|半小时之前", "30分钟前"),
    (r"一刻钟后|一刻钟以后", "15分钟后"),
    (r"一刻钟前|一刻钟以前", "15分钟前"),
    (r"壹", "1"),
    (r"貳|贰|两|兩", "2"),
    (r"參|叁|参", "3"),
    (r"肆", "4"),
    (r"伍", "5"),
    (r"陸|陆", "6"),
    (r"柒", "7"),
    (r"捌", "8"),
    (r"玖", "9"),
    (r"拾", "10"),
    (r"〇|○", "0"),
    (r"點", "点"),
    (r"十一", "11"),
    (r"十二", "12"),
    (r"十三", "13"),
    (r"十四", "14"),
    (r"十五", "15"),
    (r"十六", "16"),
    (r"十七", "17"),
    (r"十八", "18"),
    (r"十九", "19"),
    (r"二十一", "21"),
    (r"二十二", "22"),
    (r"二十三", "23"),
    (r"二十四", "24"),
    (r"二十", "20"),
    (r"十", "10"),
    (r"一", "1"),
    (r"二", "2"),
    (r"三", "3"),
    (r"四", "4"),
    (r"五", "5"),
    (r"六", "6"),
    (r"七", "7"),
    (r"八", "8"),
    (r"九", "9"),
    (r"零", "0"),
    (r"(?P<H>\d{1,2})\s*点半", lambda m: "%d:30" % int(m.group("H"))),
    (r"(?P<H>\d{1,2})\s*点\s*(?:(?P<M>\d{1,2})\s*分?)?",
     lambda m: "%d:%02d" % (int(m.group("H")), int(m.group("M") or 0))),
    (r"\s*(?P<apm>am|pm)(?P<time>\d{1,2}:\d{2}(?::\d{2})?)",
     lambda m: "%s %s" % (m.group("time"), m.group("apm"))),
    (r"凌晨|清晨|早上|早晨", " am"),
    (r"中午", " pm"),
    (r"下午|傍晚|晚上|夜里|夜间|深夜", " pm"),
    (r"午夜|半夜", "12:00 am"),
    (r"上午", " am"),
    (r"下午", " pm"),
]
FUZZY_REGEX_LIST = []
