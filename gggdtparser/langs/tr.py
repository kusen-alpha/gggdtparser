# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/5/16

"""
土耳其语
"""

ACCURATE_REGEX_LIST = [
]

SUB_TRANSLATE = [
    (r"Ocak", "1月"),
    (r"\bŞubat\b|Şub\.?", "2月"),
    (r"Mart", "3月"),
    (r"Nisan", "4月"),
    (r"Mayıs", "5月"),
    (r"Haziran", "6月"),
    (r"Temmuz", "7月"),
    (r"Ağustos", "8月"),
    (r"Eylül", "9月"),
    (r"Ekim", "10月"),
    (r"Kasım", "11月"),
    (r"Aralık", "12月"),
    (r"öğleden sonra\s*(?P<H>\d{1,2}):(?P<M>\d{2})",
     lambda m: "%d:%s" % (int(m.group("H")) % 12 + 12, m.group("M"))),
    (r"öğleden önce\s*(?P<H>\d{1,2}):(?P<M>\d{2})",
     lambda m: "%d:%s" % (int(m.group("H")) % 12, m.group("M"))),
    (r"evvelsi\s*(?:gün|天)", "前天"),
    (r"öbür\s*(?:gün|天)", "后天"),
    (r"dün", "昨天"),
    (r"bugün", "今天"),
    (r"yarın", "明天"),
    (r"şimdi", "刚刚"),
    (r"(?:gelecek|önümüzdeki)\s+hafta\b", "下周"),
    (r"geçen\s+hafta\b", "上周"),
    (r"gelecek\s+ay\b", "下个月"),
    (r"geçen\s+ay\b", "上个月"),
    (r"(?:gelecek|önümüzdeki)\s+(?:yıl|sene)\b", "明年"),
    (r"geçen\s+(?:yıl|sene)\b", "去年"),
    (r"saat", "小时"),
    (r"önce", "前"),
    (r"gün", "天"),
    (r"dakika", "分钟"),
    (r"(?P<num>\d+)\s*(?:saat|小时)\s+sonra", lambda m: "%s小时后" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*(?:dakika|分钟)\s+sonra", lambda m: "%s分钟后" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*(?:gün|天)\s+sonra", lambda m: "%s天后" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*hafta\s+sonra", lambda m: "%s周后" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*(?:ay|月)\s+sonra", lambda m: "%s月后" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*(?:yıl|sene)\s+sonra", lambda m: "%s年后" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*(?:saat|小时)\s+(?:önce|前)", lambda m: "%s小时前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*(?:dakika|分钟)\s+(?:önce|前)", lambda m: "%s分钟前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*(?:gün|天)\s+(?:önce|前)", lambda m: "%s天前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*hafta\s+(?:önce|前)", lambda m: "%s周前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*(?:ay|月)\s+(?:önce|前)", lambda m: "%s月前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*(?:yıl|sene)\s+(?:önce|前)", lambda m: "%s年前" % int(m.group("num"))),
]

FUZZY_REGEX_LIST = [
]
