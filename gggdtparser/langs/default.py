# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/5/16


"""
默认
"""

ACCURATE_REGEX_LIST = [
# 精准策略
    r"(?P<Y>\d{4})\s*[\-\|/\.年]\s*(?P<m>\d{2})\s*[\-\|/\.月]\s*(?P<d>\d{2})\s*[日]?\s*[T，]?\s*(?P<apm>am|pm)?\s*(?P<H>\d{2})\s*[:时h]\s*(?P<M>\d{2})\s*[:分]\s*(?P<S>\d{2})\s*[秒]?",
    r"(?P<Y>\d{4})\s*[\-\|/\.年]\s*(?P<m>\d{2})\s*[\-\|/\.月]\s*(?P<d>\d{2})\s*[日]?\s*[T，]?\s*(?P<apm>am|pm)?\s*(?P<H>\d{2})\s*[:时h]\s*(?P<M>\d{2})\s*[分]?",
    r"(?P<Y>\d{4})\s*[\-\|/\.年]\s*(?P<m>\d{2})\s*[\-\|/\.月]\s*(?P<d>\d{2})\s*[日]?\s*[T，]?\s*(?P<apm>am|pm)?\s*(?P<H>\d{2})\s*[时]?",
    r"(?P<Y>\d{4})\s*[\-\|/\.年]\s*(?P<m>\d{2})\s*[\-\|/\.月]\s*(?P<d>\d{2})\s*[日]?",
    r"(?P<Y>\d{4})\s*[\-\|/\.年]\s*(?P<m>\d{1,2})\s*[\-\|/\.月]\s*(?P<d>\d{1,2})\s*[日]?\s*[T，]?\s*(?P<apm>am|pm)?\s*(?P<H>\d{1,2})\s*[:时h]\s*(?P<M>\d{1,2})\s*[:分]\s*(?P<S>\d{1,2})\s*[秒]?",
    r"(?P<Y>\d{4})\s*[\-\|/\.年]\s*(?P<m>\d{1,2})\s*[\-\|/\.月]\s*(?P<d>\d{1,2})\s*[日]?\s*[T，]?\s*(?P<apm>am|pm)?\s*(?P<H>\d{1,2})\s*[:时h]\s*(?P<M>\d{1,2})\s*[分]?",
    r"(?P<Y>\d{4})\s*[\-\|/\.年]\s*(?P<m>\d{1,2})\s*[\-\|/\.月]\s*(?P<d>\d{1,2})\s*[日]?\s*[T，]?\s*(?P<apm>am|pm)?\s*(?P<H>\d{1,2})\s*[时]?",
    r"(?P<Y>\d{4})\s*[\-\|/\.年]\s*(?P<m>\d{1,2})\s*[\-\|/\.月]\s*(?P<d>\d{1,2})\s*[日]?",
    r"^(?P<ts>\d{13})$",
    r"^(?P<ts>\d{10})$",

    # before
    r"(?P<bd>\d+)\s*天\s*(前|ago)",
    r"(?P<bM>\d+)\s*分钟\s*(前|ago)",
    r"(?P<bH>\d+)\s*小时\s*(前|ago)",
    r"(?P<bm>\d+)\s*(个)?月\s*(前|ago)",
    r"(?P<bY>\d+)\s*年\s*(前|ago)",
    r"(?P<bS>\d+)\s*秒\s*(前|ago)",
    r"(?P<ba>\d+)\s*周\s*(前|ago)",
    r"(?P<ba>\d+)\s*星期\s*(前|ago)",
    # in
    r"(?P<wd>\d+)\s*天内",
    r"(?P<wM>\d+)\s*分钟内",
    r"(?P<wH>\d+)\s*小时内",
    r"(?P<wm>\d+)\s*(个)?月内",
    r"(?P<wY>\d+)\s*年内",
    r"(?P<wS>\d+)\s*秒内",
    r"(?P<wa>\d+)\s*周内",
    r"(?P<wa>\d+)\s*星期内",
    # 特殊语义
    r"(?P<sd>今天)\s*(?P<H>\d+):(?P<M>\d+):(?P<S>\d+)",
    r"(?P<sd>今天)\s*(?P<H>\d+):(?P<M>\d+)",
    r"(?P<sd>今天)\s*(?P<H>\d+)",
    r"(?P<sd>今天)",
    r"(?P<sd>昨天)\s*(?P<H>\d+):(?P<M>\d+):(?P<S>\d+)",
    r"(?P<sd>昨天)\s*(?P<H>\d+):(?P<M>\d+)",
    r"(?P<sd>昨天)\s*(?P<H>\d+)",
    r"(?P<sd>昨天)",
    r"(?P<sd>前天)\s*(?P<H>\d+):(?P<M>\d+):(?P<S>\d+)",
    r"(?P<sd>前天)\s*(?P<H>\d+):(?P<M>\d+)",
    r"(?P<sd>前天)\s*(?P<H>\d+)",
    r"(?P<sd>前天)",
    r"(?P<so>刚刚)",
]

FUZZY_REGEX_LIST = [
    # 2010 7月19日
    r"(?P<Y>\d{4})\s*[\-\|/\.年,]?\s*(?P<m>\d{1,2})\s*[\-\|/\.月]\s*(?P<d>\d{1,2})\s*[日]?",
    # 10 апреля 2023, 18:57
    r"(?P<d>\d{1,2})[\.]?\s*(?P<m>\d{1,2})\s*[月]\s*(?P<Y>\d{4})\s*[,]?\s*(?P<H>\d{2})\s*[:时h]\s*(?P<M>\d{2})\s*[分]?",
    # 14 March 2023
    r"(?P<d>\d{1,2})[\.]?\s*(?P<m>\d{1,2})\s*[月]\s*(?P<Y>\d{4})",
    # August 2006
    r"(?P<m>\d{1,2})\s*[月]?\s*(?P<Y>\d{4})",
    # 2023/0329
    r"(?P<Y>\d{4})\s*[\-\|/\.年]\s*(?P<m>\d{2})(?P<d>\d{2})",
    # 2012.9
    r"(?P<Y>\d{4})\s*[\-\|/\.年]\s*(?P<m>\d{1,2})",
    r"(?P<m>\d{1,2})\s*[\-\|/\.月]?\s*(?P<d>\d{1,2})\s*[\-\|/\.日]?\s*?(?P<Y>\d{4})\s*[\-\|/\.年]?",
    # 11/1/2018
    r"(?P<m>\d{1,2})\s*[\-\|/\.月]?\s*(?P<d>\d{1,2})\s*[\-\|/\.日]?\s*(?P<H>\d{1,2})\s*[:时h]\s*(?P<M>\d{1,2})\s*[:分]\s*(?P<S>\d{1,2})\s*[秒]?",

    # 02月02日 02:02:02
    r"(?P<m>\d{1,2})\s*[\-\|/\.月]?\s*(?P<d>\d{1,2})\s*[\-\|/\.日]?\s*(?P<H>\d{1,2})\s*[:时h]\s*(?P<M>\d{1,2})\s*[:分]?",
    # 02月02日 02:02
    r"(?P<m>\d{2})\s*[\-\|/\.月]?\s*(?P<d>\d{2})\s*[\-\|/\.日]?\s*(?P<H>\d{2})\s*[:时h]?",
    # 02月02日 02
    # 02:02:02
    r"(?P<H>\d{1,2})\s*[:时h]\s*(?P<M>\d{1,2})\s*[:分]\s*(?P<S>\d{1,2})\s*[秒]?",
    # 02:02
    r"(?P<H>\d{1,2})\s*[:时h]\s*(?P<M>\d{1,2})\s*[:分]?\s*(?P<apm>am|pm)?",
    r"(?P<m>\d{1,2})\s*[\-\|/\.月]\s*(?P<d>\d{1,2})\s*[\-\|/\.日]\s*(?P<Y>\d{2,4})",
    # 06-02-20
    r"(?P<d>\d{1,2})\s*[\-\|/\.日]\s*(?P<m>\d{1,2})\s*[\-\|/\.月]\s*(?P<Y>\d{2,4})",
    # 31.01.2019
    r"(?P<m>\d{1,2})\s*[\-\|/\.月]\s*(?P<d>\d{1,2})\s*[日]?",  # 11月20日 01-01
    r"(?P<Y>\d{4})\s*(?P<m>\d{1,2})\s*(?P<d>\d{1,2})",  # 20000101
    # Feb 5
    r"(?P<m>\d{1,2})\s*[月]\s*(?P<d>\d{1,2})",
    # 2022年
    r"(?P<Y>\d{4})\s*年",
    # 02月
    r"(?P<m>\d{1,2})\s*[月]",
    # 2022
    r"^(?P<Y>\d{4})$",

    r"(?P<bH>\d+)\s*hr\s*",
    r"(?P<bH>\d+)\s*h\s*",
    r"(?P<bd>\d+)\s*d\s*",
    r"(?P<ba>\d+)\s*w\s*",
    r"(?P<bm>\d+)\s*m\s*",
    r"(?P<bY>\d+)\s*y\s*",

    r"分钟\s*(?P<bM>\d+)",
]

SUB_TRANSLATE = [
    (r"Feb", "2月"),
    (r'at', ''),
]