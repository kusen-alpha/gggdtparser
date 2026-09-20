# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/5/8


"""
英语
"""

ACCURATE_REGEX_LIST = [
    # Thu February 02 02:02:02 2022
    r"(?P<m>\d{1,2})\s*[\-\|/\.月]?\s*(?P<d>\d{1,2})\s*[\-\|/\.日]?\s*(?P<H>\d{1,2})\s*[:时h]\s*(?P<M>\d{1,2})\s*[:分]\s*(?P<S>\d{1,2})\s*[秒]?\s*(?P<Y>\d{4})\s*[\-\|/\.年]?",
    # 04:28, 13 Feb 2023
    r"(?P<H>\d{1,2})[:](?P<M>\d{1,2})\s*[,]?\s*(?P<d>\d{1,2})\s*(?P<m>\d{1,2})\s*[月]\s*(?P<Y>\d{4})",
    # Mar 23 02:28:00 2023
    r"(?P<m>\d{1,2})\s*[月]\s*(?P<d>\d{1,2})\s*(?P<H>\d{1,2})[:](?P<M>\d{1,2})[:](?P<S>\d{1,2})\s*(?P<Y>\d{4})",
    # Feb 02, 2022 08:35 pm
    r"(?P<m>\d{1,2})\s*[月]?\s*(?P<d>\d{1,2})\s*,\s*(?P<Y>\d{4})\s*[-]?\s*(?P<H>\d{1,2})[:](?P<M>\d{1,2})\s*(?P<apm>am|pm)",
    # Feb 02, 2022 08:35
    r"(?P<m>\d{1,2})\s*[月]?\s*(?P<d>\d{1,2})\s*,\s*(?P<Y>\d{4})\s*(?P<H>\d{1,2})[:](?P<M>\d{1,2})",

    # 5:36 PM EST, Sat March 11, 2023
    r"(?P<H>\d{1,2})[:](?P<M>\d{1,2})\s*(?P<apm>am|pm)\s*[,]?\s*(?P<m>\d{1,2})\s*[月]?\s*(?P<d>\d{1,2})\s*,\s*(?P<Y>\d{4})",
    # Feb 02, 2022
    r"(?P<m>\d{1,2})\s*[月]?\s*(?P<d>\d{1,2})\s*,\s*(?P<Y>\d{4})",

    # 10 25, 2021| Jan 01, 2000
    r"(?P<d>\d{1,2})[\.]?\s*(?P<m>\d{1,2})\s*[月]\s*(?P<Y>\d{4})\s*[|]?\s*(?P<H>\d{1,2})[:](?P<M>\d{1,2})\s*(?P<apm>am|pm)",
    # Wed 29 Mar 2023 at 3:04pm
    r"(?P<d>\d{1,2})[\.]?\s*(?P<m>\d{1,2})\s*[月]\s*(?P<Y>\d{4})\s*(?P<H>\d{1,2})[:h](?P<M>\d{1,2})",
    # Wed 29 Mar 2023 at 3:04

    # May 15 2023 21:08:42
    r"(?P<m>\d{1,2})\s*(?:[月]\s*|\s+)(?P<d>\d{1,2})\s*(?P<Y>\d{4})\s*(?P<H>\d{1,2}):(?P<M>\d{1,2}):(?P<S>\d{1,2})",
    # May 08 2023, 6.00pm
    r"(?P<m>\d{1,2})\s*(?:[月]\s*|\s+)(?P<d>\d{1,2})\s*(?P<Y>\d{4}),\s*(?P<H>\d{1,2})\.(?P<M>\d{1,2})\s*(?P<apm>am|pm)",
    # May 08 2023
    r"(?P<m>\d{1,2})\s*(?:[月]\s*|\s+)(?P<d>\d{1,2})\s*(?P<Y>\d{4})",
    # RFC822: Wed, 02 Feb 2022 14:30:20 +0530
    r"(?P<d>\d{1,2})\s+(?P<m>\d{1,2})\s*[月]\s*(?P<Y>\d{4})\s+(?P<H>\d{1,2}):(?P<M>\d{1,2}):(?P<S>\d{1,2})(?:\s*[+-]?\d{4}|\s*GMT)?",
    # 25 10 2021
    r"(?P<d>\d{1,2})\s+(?P<m>\d{1,2})\s*(?P<Y>\d{4})",
    # December 23, 2022 / 15:20 -> 翻译后: 12月 23, 2022 / 15:20
    r"(?P<m>\d{1,2})\s*月\s+(?P<d>\d{1,2})(?!\d)\s*[,]?\s*(?P<Y>\d{4})\s*/?\s*(?P<H>\d{1,2}):(?P<M>\d{1,2})",
    # 23 December, 2022 / 15:20
    r"(?P<d>\d{1,2})(?!\d)\s*(?P<m>\d{1,2})\s*[月]?\s*,?\s*(?P<Y>\d{4})\s*/?\s*(?P<H>\d{1,2}):(?P<M>\d{1,2})",
    r"(?P<m>\d{1,2})\s*[月]?\s+(?P<Y>\d{4})",  # 10 2021
    r"(?P<bS>\d+)\s*seconds?\s*(ago)?",
    r"(?P<bM>\d+)\s*m\s*ago",
    r"(?P<bM>\d+)\s*minutes?\s*(ago)?",
    r"(?P<bH>\d+)\s*h\s*ago",
    r"(?P<bH>\d+)\s*小时\s*",
    r"(?P<bH>\d+)\s*hours?\s*(ago)?",
    r"(?P<bd>\d+)\s*days?\s*(ago)?\*?(at)?\s*(?P<H>\d{2})?\s*[:]?\s*(?P<M>\d{2})?\s*[分]?\s*(?P<apm>am|pm)?",
    r"(?P<bm>\d+)\s*months?\s*(ago)?",
    r"(?P<ba>\d+)\s*weeks?\s*(ago)?",
    r"(?P<bY>\d+)\s*years?\s*(ago)?",
]

SUB_TRANSLATE = [
    (r"(?P<num>\d{1,2})(?:st|nd|rd|th)\b", lambda m: m.group("num")),
    (r"\bof\b", ""),
    (r"January|JANUARY|Jan\.|Jan", "1月"),
    (r"February|FEBRUARY|Feb\.?|FEB", "2月"),
    (r"March|MARCH|Mar\.|Mar|Mai", "3月"),
    (r"April|APRIL|Apr\.|Apr", "4月"),
    (r"May\.|May|MAY", "5月"),
    (r"June|JUNE|Jun\.|Jun", "6月"),
    (r"July|JULY|Jul\.|Jul", "7月"),
    (r"August|AUGUST|Aug\.|Aug", "8月"),
    (r"September|SEPTEMBER|Sept\.|Sept|Sep\.|Sep", "9月"),
    (r"October|OCTOBER|Oct\.|Oct", "10月"),
    (r"November|NOVEMBER|Nov\.|Nov", "11月"),
    (r"December|DECEMBER|Dec\.|Dec", "12月"),
    (r'Spring|SPRING', '2月'),
    (r'Summer|SUMMER', '5月'),
    (r'Autumn|AUTUMN', '8月'),
    (r'Winter|WINTER', '11月'),
    (r'EST|CST|MST|PST|AKST|HST', ''),
    (r"(?i)\b(?P<dir>next|last|this)\s+(?P<name>monday|mon\.?|tuesday|tues\.?|thursday|thurs\.?|thur\.?|wednesday|wed\.?|friday|fri\.?|saturday|sat\.?|sunday|sun\.?)\b",
     lambda m: "%s周%s" % (
         {"next": "下", "last": "上"}.get(m.group("dir").lower(), "这"),
         {
             "monday": "一", "mon": "一", "mon.": "一",
             "tuesday": "二", "tues": "二", "tues.": "二",
             "wednesday": "三", "wed": "三", "wed.": "三",
             "thursday": "四", "thurs": "四", "thurs.": "四",
             "thur": "四", "thur.": "四",
             "friday": "五", "fri": "五", "fri.": "五",
             "saturday": "六", "sat": "六", "sat.": "六",
             "sunday": "日", "sun": "日", "sun.": "日",
         }.get(m.group("name").lower(), ""))),
    (r'Monday|Mon\.?', ''),
    (r'Tuesday|Tues\.?', ''),
    (r'Wednesday|Wed\.?', ''),
    (r'Thursday|Thurs\.?|Thur\.?', ''),
    (r'Friday|Fri\.?', ''),
    (r'Saturday|Sat\.?', ''),
    (r'Sunday|Sun\.?', ''),
    (r'AT', ''),
    (r'AM', 'am'),
    (r'PM', 'pm'),
    (r"(?i)\b(?P<apm>a|p)\.m\.", lambda m: "am" if m.group("apm").lower() == "a" else "pm"),
    (r"(?i)\bnoon\b", "12:00 pm"),
    (r"(?i)\bmidnight\b", "12:00 am"),
    (r"(?i)\bthis\s+morning\b", "今天 08:00 am"),
    (r"(?i)\bthis\s+afternoon\b", "今天 15:00 pm"),
    (r"(?i)\bthis\s+evening\b|\btonight\b", "今天 20:00 pm"),
    (r"(?i)\bthis\s+night\b|\blast\s+night\b", "昨天 22:00 pm"),
    (r"(?i)\btomorrow\s+morning\b", "明天 08:00 am"),
    (r"(?i)\btomorrow\s+afternoon\b", "明天 15:00 pm"),
    (r"(?i)\btomorrow\s+evening\b", "明天 20:00 pm"),
    (r"(?i)\btomorrow\s+night\b", "明天 22:00 pm"),
    (r"(?i)\byesterday\s+morning\b", "昨天 08:00 am"),
    (r"(?i)\b(?:at\s+)?noon\b", "12:00 pm"),
    (r"(?i)\bjust now\b|\bright now\b", "刚刚"),
    (r"(?i)\btoday\b", "今天"),
    (r"(?i)\bthe day after tomorrow\b", "后天"),
    (r"(?i)\bday before yesterday\b", "前天"),
    (r"(?i)\btomorrow\b", "明天"),
    (r"(?i)\bhalf past\s*(?P<H>\d{1,2})\b", lambda m: "%d:30" % int(m.group("H"))),
    (r"(?i)\bquarter past\s*(?P<H>\d{1,2})\b", lambda m: "%d:15" % int(m.group("H"))),
    (r"(?i)\bquarter to\s*(?P<H>\d{1,2})\b",
     lambda m: "%d:45" % (int(m.group("H")) - 1 or 12)),
    (r"(?i)\bin\s+(?P<num>\d+)\s+hours?", lambda m: "%s小时后" % m.group("num")),
    (r"(?i)\bin\s+(?P<num>\d+)\s+minutes?", lambda m: "%s分钟后" % m.group("num")),
    (r"(?i)\bin\s+(?P<num>\d+)\s+days?", lambda m: "%s天后" % m.group("num")),
    (r"(?i)\bin\s+(?P<num>\d+)\s+weeks?", lambda m: "%s周后" % m.group("num")),
    (r"(?i)\bin\s+(?P<num>\d+)\s+months?", lambda m: "%s月后" % m.group("num")),
    (r"(?i)\bin\s+(?P<num>\d+)\s+years?", lambda m: "%s年后" % m.group("num")),
    (r"(?i)\b(?P<num>\d+)\s+hours?\s+later", lambda m: "%s小时后" % m.group("num")),
    (r"(?i)\b(?P<num>\d+)\s+minutes?\s+later", lambda m: "%s分钟后" % m.group("num")),
    (r"(?i)\b(?P<num>\d+)\s+days?\s+later", lambda m: "%s天后" % m.group("num")),
    (r"(?i)\b(?P<num>\d+)\s+weeks?\s+later", lambda m: "%s周后" % m.group("num")),
    (r"(?i)\b(?P<num>\d+)\s+months?\s+later", lambda m: "%s月后" % m.group("num")),
    (r"(?i)\b(?P<num>\d+)\s+years?\s+later", lambda m: "%s年后" % m.group("num")),
    (r"(?i)\bnext\s+week\b", "下周"),
    (r"(?i)\blast\s+week\b", "上周"),
    (r"(?i)\bnext\s+month\b", "下个月"),
    (r"(?i)\blast\s+month\b", "上个月"),
    (r"(?i)\bnext\s+year\b", "明年"),
    (r"(?i)\blast\s+year\b", "去年"),
    (r"(?i)\bin\s+an?\s+(?P<unit>second|minute|hour|day|week|month|year)\b",
     lambda m: "1%s后" % {
         "second": "秒", "minute": "分钟", "hour": "小时",
         "day": "天", "week": "周", "month": "月", "year": "年"
     }[m.group("unit").lower()]),
    (r"(?i)(?:an?|a)\s+(?P<unit>second|minute|hour|day|week|month|year)\s+ago\b",
     lambda m: "1%s前" % {
         "second": "秒", "minute": "分钟", "hour": "小时",
         "day": "天", "week": "周", "month": "月", "year": "年"
     }[m.group("unit").lower()]),
    (r"(?i)\bin\s+half\s+an\s+hour\b", "30分钟后"),
    (r"(?i)\bhalf\s+an\s+hour\s+ago\b", "30分钟前"),
    (r'[yY]esterday\s*(at)?', '昨天'),
]
FUZZY_REGEX_LIST = []
