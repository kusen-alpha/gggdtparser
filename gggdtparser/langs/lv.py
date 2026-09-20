# -*- coding:utf-8 -*-

"""
拉脱维亚语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_LV_UNITS = {
    "sekunde": "秒", "sekundes": "秒", "sekundēm": "秒",
    "minūte": "分钟", "minūtes": "分钟", "minūtēm": "分钟",
    "stunda": "小时", "stundas": "小时", "stundām": "小时",
    "diena": "天", "dienas": "天", "dienām": "天",
    "nedēļa": "周", "nedēļas": "周", "nedēļām": "周",
    "mēnesis": "月", "mēnesi": "月", "mēneši": "月", "mēnešiem": "月",
    "gads": "年", "gadi": "年", "gadus": "年", "gadiem": "年",
}
_LV_UNIT_RE = (
    r"sekundes|sekundēm|minūtes|minūtēm|stundas|stundām|"
    r"dienas|dienām|nedēļas|nedēļām|mēneši|mēnešiem|gadi|gadiem"
)

_LV_WEEKDAYS = {
    "pirmdiena": "周一", "pirmdienā": "周一",
    "otrdiena": "周二", "otrdienā": "周二",
    "trešdiena": "周三", "trešdienā": "周三",
    "ceturtdiena": "周四", "ceturtdienā": "周四",
    "piektdiena": "周五", "piektdienā": "周五",
    "sestdiena": "周六", "sestdienā": "周六",
    "svētdiena": "周日", "svētdienā": "周日",
}


def _lv_later(match):
    return "%s%s后" % (match.group(1), _LV_UNITS[match.group(2)])


def _lv_earlier(match):
    return "%s%s前" % (match.group(1), _LV_UNITS[match.group(2)])


SUB_TRANSLATE = [
    (r"(?i)\b(?:nākamā|nākamajā|nākošā|nākošajā)\s+(pirmdiena|pirmdienā|otrdiena|otrdienā|trešdiena|trešdienā|ceturtdiena|ceturtdienā|piektdiena|piektdienā|sestdiena|sestdienā|svētdiena|svētdienā)\b",
     lambda m: "下%s" % _LV_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(?:pagājušā|pagājušajā|iepriekšējā|iepriekšējajā)\s+(pirmdiena|pirmdienā|otrdiena|otrdienā|trešdiena|trešdienā|ceturtdiena|ceturtdienā|piektdiena|piektdienā|sestdiena|sestdienā|svētdiena|svētdienā)\b",
     lambda m: "上%s" % _LV_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(?:šī|šajā)\s+(pirmdiena|pirmdienā|otrdiena|otrdienā|trešdiena|trešdienā|ceturtdiena|ceturtdienā|piektdiena|piektdienā|sestdiena|sestdienā|svētdiena|svētdienā)\b",
     lambda m: "这%s" % _LV_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(pirmdien[āa]|otrdien[āa]|trešdien[āa]|ceturtdien[āa]|piektdien[āa]|sestdien[āa]|svētdien[āa])\b",
     lambda m: "周%s" % {
         "pirmdiena": "一", "pirmdienā": "一", "otrdiena": "二",
         "otrdienā": "二", "trešdiena": "三", "trešdienā": "三",
         "ceturtdiena": "四", "ceturtdienā": "四", "piektdiena": "五",
         "piektdienā": "五", "sestdiena": "六", "sestdienā": "六",
         "svētdiena": "日", "svētdienā": "日"}[m.group(1).lower()]),
    (r"(?iu)\b(?:janvāris|janvāra|janvārī)\b", "1月"),
    (r"(?iu)\b(?:februāris|februāra|februārī)\b", "2月"),
    (r"(?iu)\b(?:marts|marta|martā)\b", "3月"),
    (r"(?iu)\b(?:aprīlis|aprīļa|aprīlī)\b", "4月"),
    (r"(?iu)\b(?:maijs|maija|majā|maijā)\b", "5月"),
    (r"(?iu)\b(?:jūnijs|jūnija|jūnijā)\b", "6月"),
    (r"(?iu)\b(?:jūlijs|jūlija|jūlijā)\b", "7月"),
    (r"(?iu)\b(?:augusts|augusta|augustā)\b", "8月"),
    (r"(?iu)\b(?:septembris|septembra|septembrī)\b", "9月"),
    (r"(?iu)\b(?:oktobris|oktobra|oktobrī)\b", "10月"),
    (r"(?iu)\b(?:novembris|novembra|novembrī)\b", "11月"),
    (r"(?iu)\b(?:decembris|decembra|decembrī)\b", "12月"),
    (r"(?i)\b(?P<Y>\d{4})\.?\s+gada\s+(?P<d>\d{1,2})\.?\s+(?P<m>\d{1,2})月(?!\w)",
     lambda m: "%s年%s月%s日" % (m.group("Y"), m.group("m"), m.group("d"))),
    (r"\baizvakar\b", "前天"),
    (r"\bparīt\b", "后天"),
    (r"(?i)\bšorīt\b", "今天 08:00 am"),
    (r"(?i)\bšodien\s+pēcpusdienā\b", "今天 15:00 pm"),
    (r"(?i)\bšovakar\b", "今天 20:00 pm"),
    (r"(?i)\brīt\s+no\s+rīta\b", "明天 08:00 am"),
    (r"(?i)\brīt\s+vakarā\b", "明天 20:00 pm"),
    (r"(?i)\bvakar\s+vakarā\b", "昨天 20:00 pm"),
    (r"(?i)\bpusdienlaikā\b", "12:00 pm"),
    (r"(?i)\bpusnaktī\b", "12:00 am"),
    (r"\bšodien\b", "今天"),
    (r"\bvakar\b", "昨天"),
    (r"\brīt\b", "明天"),
    (r"pēc\s+(?P<a>\d+)\s*(?P<b>%s)" % _LV_UNIT_RE, _lv_later),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+vēlāk" % _LV_UNIT_RE, _lv_later),
    (r"pirms\s+(?P<a>\d+)\s*(?P<b>%s)" % _LV_UNIT_RE, _lv_earlier),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+agrāk" % _LV_UNIT_RE, _lv_earlier),
    (r"\b(?:tagad|šobrīd)\b", "刚刚"),
    (r"\bnākamnedēļ\b", "下周"),
    (r"\bpagājušajā\s+nedēļā\b", "上周"),
    (r"\bnākamajā\s+mēnesī\b", "下个月"),
    (r"\bpagājušajā\s+mēnesī\b", "上个月"),
    (r"\bnākamgad\b", "明年"),
    (r"\bpagājušajā\s+gadā\b", "去年"),
]
