#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/3/24


STRING_DATE_TIME_REGEX_LIST = [
    # 精准策略
    r"(?P<ts>\d{10})",
    r"(?P<Y>\d{4})\s*[\-\|/\.年]\s*(?P<m>\d{1,2})\s*[\-\|/\.月]\s*(?P<d>\d{1,2})\s*[日]?\s*T?\s*(?P<H>\d{1,2})\s*[:时]\s*(?P<M>\d{1,2})\s*[:分]\s*(?P<S>\d{1,2})\s*[秒]?",
    r"(?P<Y>\d{4})\s*[\-\|/\.年]\s*(?P<m>\d{1,2})\s*[\-\|/\.月]\s*(?P<d>\d{1,2})\s*[日]?\s+T?\s*(?P<H>\d{1,2})\s*[:时]\s*(?P<M>\d{1,2})\s*[分]?",
    r"(?P<Y>\d{4})\s*[\-\|/\.年]\s*(?P<m>\d{1,2})\s*[\-\|/\.月]\s*(?P<d>\d{1,2})\s*[日]?\s+(?P<H>\d{1,2})\s*[时]?",
    r"(?P<Y>\d{4})\s*[\-\|/\.年]\s*(?P<m>\d{1,2})\s*[\-\|/\.月]\s*(?P<d>\d{1,2})\s*[日]?",
    r"(?P<Y>\d{4})\s*[\-\|/\.年]\s*(?P<m>\d{1,2})",  # 2012.9
    r"(?P<m>\d{1,2})\s*[\-\|/\.月]?\s*(?P<d>\d{1,2})\s*[\-\|/\.日]?\*?(?P<Y>\d{4})\s*[\-\|/\.年]?",  # 11/1/2018

    # 模糊策略
    r"(?P<bd>\d+)\s*天前",
    r"(?P<bM>\d+)\s*分钟前",
    r"(?P<bH>\d+)\s*小时前",
    r"(?P<bm>\d+)\s*(个)?月前",
    r"(?P<bY>\d+)\s*年前",
    r"(?P<bS>\d+)\s*秒前",
    r"(?P<ba>\d+)\s*周前",
    r"(?P<ba>\d+)\s*星期前",

    r"(?P<wd>\d+)\s*天内",
    r"(?P<wM>\d+)\s*分钟内",
    r"(?P<wH>\d+)\s*小时内",
    r"(?P<wm>\d+)\s*(个)?月内",
    r"(?P<wY>\d+)\s*年内",
    r"(?P<wS>\d+)\s*秒内",
    r"(?P<wa>\d+)\s*周内",
    r"(?P<wa>\d+)\s*星期内",

    r"(?P<sd>今天)\s*(?P<H>\d+):(?P<M>\d+)",
    r"(?P<sd>今天)",
    r"(?P<sd>昨天)\s*(?P<H>\d+):(?P<M>\d+)",
    r"(?P<sd>昨天)",
    r"(?P<sd>前天)\s*(?P<H>\d+):(?P<M>\d+)",
    r"(?P<sd>前天)",
    r"(?P<so>刚刚)",
    # 特殊策略
    # r"(?P<m>\d{1,2})\s*月?\s*\.\s*(?P<d>\d{1,2})\s*日?\s*/(?P<Y>\d{4})\s*年?",
    # r"(?P<d>\d{1,2})\s*\.\s*(?P<m>\d{1,2})\s*日?\s*/(?P<Y>\d{4})\s*年?"
]

STRING_DATE_TIME_REGEX_LIST_FUZZY = [  # 模糊时间
    r"(?P<m>\d{1,2})\s*[\-\|/\.月]\s*(?P<d>\d{1,2})\s*[\-\|/\.日]\s*(?P<Y>\d{2,4})",  # 06-02-20
    r"(?P<m>\d{1,2})\s*[\-\|/\.月]\s*(?P<d>\d{1,2})\s*[日]?",  # 11月20日 01-01
    r"(?P<Y>\d{4})\s*(?P<m>\d{1,2})\s*(?P<d>\d{1,2})",  # 20000101
]

EN_STRING_DATE_TIME_REGEX_LIST = [
    r"(?P<H>\d{1,2})[:](?P<M>\d{1,2})\s*[,]?\s*(?P<d>\d{1,2})\s*(?P<m>\d{1,2})\s*[月]\s*(?P<Y>\d{4})",  # 04:28, 13 Feb 2023
    r"(?P<m>\d{1,2})\s*[月]\s*(?P<d>\d{1,2})\s*(?P<H>\d{1,2})[:](?P<M>\d{1,2})[:](?P<S>\d{1,2})\s*(?P<Y>\d{4})",  # Mar 23 02:28:00 2023
    r"(?P<m>\d{1,2})\s*[月]?\s*(?P<d>\d{1,2})\s*,\s*(?P<Y>\d{4})",  # 10 25, 2021| Jan 01, 2000
    r"(?P<d>\d{1,2})\s*(?P<m>\d{1,2})\s*(?P<Y>\d{4})",  # 25 10 2021
    r"(?P<m>\d{1,2})\s*(?P<Y>\d{4})",  # 10 2021

    #
    r"(?P<bH>\d+)\s*days ago",
    r"(?P<bm>\d+)\s*month ago",
    r"(?P<ba>\d+)\s*weeks ago",
    r"(?P<bY>\d+)\s*years ago",
]

ZH_TW_STRING_DATE_TIME_REGEX_LIST = [
    r"民国(?P<mgY>\d+)[年]?",
]

DEFAULT_META_XPATH_LIST = [  # 部分特别规范的新闻网站，可以直接从 HTML 的 meta 数据中获得发布时间
    '//meta[starts-with(@property, "rnews:datePublished")]/@content',
    '//meta[starts-with(@property, "article:published_time")]/@content',
    '//meta[starts-with(@property, "og:article:published_time")]/@content',
    '//meta[starts-with(@property, "og:published_time")]/@content',
    '//meta[starts-with(@property, "og:release_date")]/@content',
    '//meta[starts-with(@itemprop, "datePublished")]/@content',
    '//meta[starts-with(@itemprop, "dateUpdate")]/@content',
    '//meta[starts-with(@name, "OriginalPublicationDate")]/@content',
    '//meta[starts-with(@name, "article_date_original")]/@content',
    '//meta[starts-with(@name, "og:time")]/@content',
    '//meta[starts-with(@name, "apub:time")]/@content',
    '//meta[starts-with(@name, "publication_date")]/@content',
    '//meta[starts-with(@name, "sailthru.date")]/@content',
    '//meta[starts-with(@name, "PublishDate")]/@content',
    '//meta[starts-with(@name, "publishdate")]/@content',
    '//meta[starts-with(@name, "PubDate")]/@content',
    '//meta[starts-with(@name, "pubtime")]/@content',
    '//meta[starts-with(@name, "_pubtime")]/@content',
    '//meta[starts-with(@name, "weibo: article:create_at")]/@content',
    '//meta[starts-with(@pubdate, "pubdate")]/@content',
    '//meta[@property="article:published_time"]/@content',
]

# 英文转阿拉伯
EN2ARAB = [
    (r"January|Jan\.|Jan", "1月"),
    (r"February|Feb\.|Feb", "2月"),
    (r"March|Mar\.|Mar", "3月"),
    (r"April|Apr\.|Apr", "4月"),
    (r"May\.|May", "5月"),
    (r"June|Jun\.|Jun", "6月"),
    (r"July|Jul\.|Jul", "7月"),
    (r"August|Aug\.|Aug", "8月"),
    (r"September|Sept\.|Sept|Sep\.|Sep", "9月"),
    (r"October|Oct\.|Oct", "10月"),
    (r"November|Nov\.|Nov", "11月"),
    (r"December|Dec\.|Dec", "12月"),
    (r'Spring', '2月'),
    (r'Summer', '5月'),
    (r'Autumn', '8月'),
    (r'Winter', '11月')
]

# 中文转阿拉伯
ZH_CN2ARAB = [
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
]

# 繁体转简体
ZH_TW2ZH_CN = {
    (r'時', '时'),
    (r'國', '国'),
}

DATE_TIME_FORMATS = [
    # '%Y/%m/%d'
]
