# -*- coding:utf-8 -*-

"""
马来语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_MS_UNITS = {
    "saat": "秒", "minit": "分钟", "jam": "小时",
    "hari": "天", "minggu": "周", "bulan": "月", "tahun": "年",
}

SUB_TRANSLATE = [
    (r"(?i)\b(?:pada\s+)?(isnin|selasa|rabu|khamis|jumaat|sabtu|ahad)\s+depan\b",
     lambda m: "下%s" % {
         "isnin": "周一", "selasa": "周二", "rabu": "周三",
         "khamis": "周四", "jumaat": "周五", "sabtu": "周六",
         "ahad": "周日"}[m.group(1).lower()]),
    (r"(?i)\b(?:pada\s+)?(isnin|selasa|rabu|khamis|jumaat|sabtu|ahad)\s+(?:lepas|yang\s+lalu)\b",
     lambda m: "上%s" % {
         "isnin": "周一", "selasa": "周二", "rabu": "周三",
         "khamis": "周四", "jumaat": "周五", "sabtu": "周六",
         "ahad": "周日"}[m.group(1).lower()]),
    (r"(?i)\b(?:pada\s+)?(isnin|selasa|rabu|khamis|jumaat|sabtu|ahad)\s+ini\b",
     lambda m: "这%s" % {
         "isnin": "周一", "selasa": "周二", "rabu": "周三",
         "khamis": "周四", "jumaat": "周五", "sabtu": "周六",
         "ahad": "周日"}[m.group(1).lower()]),
    (r"(?i)\bisnin\b", "周一"),
    (r"(?i)\bselasa\b", "周二"),
    (r"(?i)\brabu\b", "周三"),
    (r"(?i)\bkhamis\b", "周四"),
    (r"(?i)\bjumaat\b", "周五"),
    (r"(?i)\bsabtu\b", "周六"),
    (r"(?i)\bahad\b", "周日"),
    (r"(?i)\bpagi\s+ini\b", "今天 08:00 am"),
    (r"(?i)\btengah\s+hari\b", "12:00 pm"),
    (r"(?i)\bpetang\s+ini\b", "今天 15:00 pm"),
    (r"(?i)\bmalam\s+ini\b", "今天 20:00 pm"),
    (r"(?i)\besok\s+pagi\b", "明天 08:00 am"),
    (r"(?i)\besok\s+petang\b", "明天 15:00 pm"),
    (r"(?i)\besok\s+malam\b", "明天 20:00 pm"),
    (r"(?i)\bmalam\s+semalam\b|\bsemalam\s+malam\b", "昨天 20:00 pm"),
    (r"(?i)\btengah\s+malam\b", "12:00 am"),
    (r"\bJanuari\b", "1月"),
    (r"\bFebruari\b", "2月"),
    (r"\bMac\b", "3月"),
    (r"\bApril\b", "4月"),
    (r"\bMei\b", "5月"),
    (r"\bJun\b", "6月"),
    (r"\bJulai\b", "7月"),
    (r"\bOgos\b", "8月"),
    (r"\bSeptember\b", "9月"),
    (r"\bOktober\b", "10月"),
    (r"\bNovember\b", "11月"),
    (r"\bDisember\b", "12月"),
    (r"\bkelmarin\b", "前天"),
    (r"\blusa\b", "后天"),
    (r"\bhari\s+ini\b", "今天"),
    (r"\bsemalam\b", "昨天"),
    (r"\besok\b", "明天"),
    (r"dalam\s+(?P<num>\d+)\s*(?P<unit>saat|minit|jam|hari|minggu|bulan|tahun)",
     lambda m: "%s%s后" % (
         m.group("num"), _MS_UNITS[m.group("unit")])),
    (r"(?P<num>\d+)\s*(?P<unit>saat|minit|jam|hari|minggu|bulan|tahun)\s+lalu",
     lambda m: "%s%s前" % (
         m.group("num"), _MS_UNITS[m.group("unit")])),
    (r"\b(?:sekarang|baru\s+sahaja)\b", "刚刚"),
    (r"\bminggu\s+depan\b", "下周"),
    (r"\bminggu\s+lepas\b", "上周"),
    (r"\bbulan\s+depan\b", "下个月"),
    (r"\bbulan\s+lepas\b", "上个月"),
    (r"\btahun\s+depan\b", "明年"),
    (r"\btahun\s+lepas\b", "去年"),
]
