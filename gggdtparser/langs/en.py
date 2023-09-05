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
    r"(?P<m>\d{1,2})\s*[月]?\s*(?P<d>\d{1,2})\s*(?P<Y>\d{4})\s*(?P<H>\d{1,2}):(?P<M>\d{1,2}):(?P<S>\d{1,2})",
    # May 08 2023, 6.00pm
    r"(?P<m>\d{1,2})\s*[月]?\s*(?P<d>\d{1,2})\s*(?P<Y>\d{4}),\s*(?P<H>\d{1,2})\.(?P<M>\d{1,2})\s*(?P<apm>am|pm)",
    # May 08 2023
    r"(?P<m>\d{1,2})\s*[月]?\s*(?P<d>\d{1,2})\s*(?P<Y>\d{4})",
    # 25 10 2021
    r"(?P<d>\d{1,2})\s*(?P<m>\d{1,2})\s*(?P<Y>\d{4})",
    r"(?P<m>\d{1,2})\s*(?P<Y>\d{4})",  # 10 2021
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
    (r"January|JANUARY|Jan\.|Jan", "1月"),
    (r"February|FEBRUARY|Feb\.", "2月"),
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
    (r'[yY]esterday\s*(at)?', '昨天'),
]
FUZZY_REGEX_LIST = []