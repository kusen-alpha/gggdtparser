# -*- coding:utf-8 -*-

"""
阿尔巴尼亚语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_SQ_UNITS = {
    "sekondë": "秒", "sekonda": "秒", "sekondash": "秒",
    "minutë": "分钟", "minuta": "分钟", "minutash": "分钟",
    "orë": "小时", "orësh": "小时",
    "ditë": "天", "ditësh": "天",
    "javë": "周", "javësh": "周",
    "muaj": "月", "muajsh": "月",
    "vit": "年", "vite": "年", "vjet": "年",
}
_SQ_UNIT_RE = (
    r"sekond[ëa]|sekondash|minut[ëa]|minutash|orë(?:sh)?|"
    r"dit[ëe]|ditësh|jav[ëe]|javësh|muaj(?:sh)?|vit(?:e)?|vjet"
)

_SQ_WEEKDAYS = {
    "e hënë": "周一",
    "të hënën": "周一",
    "e martë": "周二",
    "të martën": "周二",
    "e mërkurë": "周三",
    "të mërkurën": "周三",
    "e enjte": "周四",
    "të enjten": "周四",
    "e premte": "周五",
    "të premten": "周五",
    "e shtunë": "周六",
    "të shtunën": "周六",
    "e diel": "周日",
    "të dielën": "周日",
}
_SQ_WEEKDAYS_RE = "|".join(sorted(_SQ_WEEKDAYS, key=len, reverse=True))
_SQ_WEEKDAYS_THIS_RE = (
    r"të\s+hënë|të\s+martë|të\s+mërkurë|të\s+enjte|"
    r"të\s+premte|të\s+shtunë|të\s+dielë"
)


def _sq_later(match):
    return "%s%s后" % (match.group(1), _SQ_UNITS[match.group(2)])


def _sq_earlier(match):
    return "%s%s前" % (match.group(1), _SQ_UNITS[match.group(2)])


SUB_TRANSLATE = [
    (r"(?i)\b(%s)\s+e\s+ardhshme\b" % _SQ_WEEKDAYS_RE,
     lambda m: "下%s" % _SQ_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(%s)\s+e\s+kaluar\b" % _SQ_WEEKDAYS_RE,
     lambda m: "上%s" % _SQ_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\bkëtë\s+(%s)\b" % _SQ_WEEKDAYS_THIS_RE,
     lambda m: "这%s" % {
         "të hënë": "周一", "të martë": "周二", "të mërkurë": "周三",
         "të enjte": "周四", "të premte": "周五", "të shtunë": "周六",
         "të dielë": "周日"}[m.group(1).lower()]),
    (r"(?i)\bsot\s+në\s+mëngjes\b", "今天 08:00 am"),
    (r"(?i)\bsot\s+në\s+mesditë\b", "今天 12:00 pm"),
    (r"(?i)\bsot\s+pasdite\b", "今天 15:00 pm"),
    (r"(?i)\bsot\s+në\s+mbrëmje\b", "今天 20:00 pm"),
    (r"(?i)\bsonte\b", "今天 22:00 pm"),
    (r"(?i)\bnesër\s+në\s+mëngjes\b", "明天 08:00 am"),
    (r"(?i)\bdje\s+në\s+mbrëmje\b", "昨天 20:00 pm"),
    (r"(?i)\bmesnatë\b", "12:00 am"),
    (r"(?i)\bmesditë\b", "12:00 pm"),
    (r"\bjanar\b", "1月"),
    (r"\bshkurt\b", "2月"),
    (r"\bmars\b", "3月"),
    (r"\bprill\b", "4月"),
    (r"\bmaj\b", "5月"),
    (r"\bqershor\b", "6月"),
    (r"\bkorrik\b", "7月"),
    (r"\bgusht\b", "8月"),
    (r"\bshtator\b", "9月"),
    (r"\btetor\b", "10月"),
    (r"\bnëntor\b", "11月"),
    (r"\bdhjetor\b", "12月"),
    (r"\bpardje\b", "前天"),
    (r"\bpasnesër\b", "后天"),
    (r"\bsot\b", "今天"),
    (r"\bdje\b", "昨天"),
    (r"\bnesër\b", "明天"),
    (r"pas\s+(?P<a>\d+)\s*(?P<b>%s)" % _SQ_UNIT_RE, _sq_later),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+(?:më\s+vonë)" % _SQ_UNIT_RE, _sq_later),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+më\s+parë" % _SQ_UNIT_RE, _sq_earlier),
    (r"\b(?:tani|tani\s+menjëherë)\b", "刚刚"),
    (r"\bjava\s+e\s+ardhshme\b|\bjavën\s+e\s+ardhshme\b", "下周"),
    (r"\bjava\s+e\s+kaluar\b|\bjavën\s+e\s+kaluar\b", "上周"),
    (r"\bmuajin\s+e\s+ardhshëm\b", "下个月"),
    (r"\bmuajin\s+e\s+kaluar\b", "上个月"),
    (r"\bviti\s+e\s+ardhshëm\b|\bvitin\s+e\s+ardhshëm\b", "明年"),
    (r"\bviti\s+e\s+kaluar\b|\bvitin\s+e\s+kaluar\b", "去年"),
]

for _weekday in sorted(_SQ_WEEKDAYS, key=len, reverse=True):
    SUB_TRANSLATE.append((r"(?i)\b%s\b" % _weekday,
                          _SQ_WEEKDAYS[_weekday]))
