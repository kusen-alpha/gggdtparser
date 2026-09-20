# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/5/16


"""
繁体/中国台湾等
"""

ACCURATE_REGEX_LIST = [
    r"民国\s*(?P<mgY>\d+)[\-\|/\.年]\s*(?P<m>\d+)[\-\|/\.月]\s*(?P<d>\d+)[日]?",
    r"民国\s*(?P<mgY>\d+)[\-\|/\.年]\s*(?P<m>\d+)[\-\|/\.月]?",
    r"民国(?P<mgY>\d+)[年]?",
    r"(?P<mgY>\d{3})\s*[\-\|/\.年]\s*(?P<m>\d{1,2})\s*[\-\|/\.月]\s*(?P<d>\d{1,2})\s*[日]?",
    r"(?P<bH>\d+)\s*时间前",
]

SUB_TRANSLATE = [
    (r'時', '时'),
    (r'間', '间'),
    (r'國', '国'),
    (r'鐘', '钟'),
    (r'個', '个'),
    (r'後', '后'),
    (r'週', '周'),
    (r'今天', '今天'),
    (r'昨天', '昨天'),
    (r'明天', '明天'),
    (r'前天', '前天'),
    (r'后天', '后天'),
    (r'剛剛|剛', '刚刚'),
    (r'(?P<num>\d+)\s*(?:秒鐘?|秒)\s*后', lambda m: "%s秒后" % int(m.group("num"))),
    (r'(?P<num>\d+)\s*分鐘?\s*后', lambda m: "%s分钟后" % int(m.group("num"))),
    (r'(?P<num>\d+)\s*(?:小時|点钟|點鐘)\s*后', lambda m: "%s小时后" % int(m.group("num"))),
    (r'(?P<num>\d+)\s*日\s*后', lambda m: "%s天后" % int(m.group("num"))),
    (r'(?P<num>\d+)\s*星期\s*后', lambda m: "%s周后" % int(m.group("num"))),
    (r'(?P<num>\d+)\s*個?月\s*后', lambda m: "%s月后" % int(m.group("num"))),
    (r'(?P<num>\d+)\s*年\s*后', lambda m: "%s年后" % int(m.group("num"))),
    (r'(?P<num>\d+)\s*秒\s*前', lambda m: "%s秒前" % int(m.group("num"))),
    (r'(?P<num>\d+)\s*分\s*前', lambda m: "%s分钟前" % int(m.group("num"))),
    (r'(?P<num>\d+)\s*(?:小時|点钟|點鐘)\s*前', lambda m: "%s小时前" % int(m.group("num"))),
    (r'(?P<num>\d+)\s*日\s*前', lambda m: "%s天前" % int(m.group("num"))),
    (r'(?P<num>\d+)\s*星期\s*前', lambda m: "%s周前" % int(m.group("num"))),
    (r'(?P<num>\d+)\s*個?月\s*前', lambda m: "%s月前" % int(m.group("num"))),
    (r'(?P<num>\d+)\s*年\s*前', lambda m: "%s年前" % int(m.group("num"))),
    (r'下週|下周', '下周'),
    (r'上週|上周', '上周'),
    (r'下個月|下月', '下个月'),
    (r'上個月|上月', '上个月'),
    (r'明年', '明年'),
    (r'去年', '去年'),
]
FUZZY_REGEX_LIST = []
