# -*- coding:utf-8 -*-

"""
立陶宛语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_LT_UNITS = {
    "sekundė": "秒", "sekundes": "秒", "sekundžių": "秒",
    "minutė": "分钟", "minutes": "分钟", "minučių": "分钟",
    "valanda": "小时", "valandas": "小时", "valandų": "小时",
    "diena": "天", "dienas": "天", "dienų": "天",
    "savaitė": "周", "savaites": "周", "savaičių": "周",
    "mėnuo": "月", "mėnesį": "月", "mėnesių": "月",
    "mėnesius": "月", "mėnesio": "月",
    "metai": "年", "metus": "年", "metų": "年", "metais": "年",
}
_LT_UNIT_RE = (
    r"sekund[ėe]s?|sekundžių|minut[ėe]s?|minučių|"
    r"valand[ao]s?|valandų|dien[ao]s?|dienų|"
    r"savait[ėe]s?|savaičių|mėnes(?:į|ių|ius|io)|met(?:us|ais|ų|ai|ą)"
)


def _lt_later(match):
    return "%s%s后" % (match.group(1), _LT_UNITS[match.group(2)])


def _lt_earlier(match):
    return "%s%s前" % (match.group(1), _LT_UNITS[match.group(2)])


_LT_WEEKDAYS = {
    "pirmadienis": "周一", "pirmadienį": "周一",
    "antradienis": "周二", "antradienį": "周二",
    "trečiadienis": "周三", "trečiadienį": "周三",
    "ketvirtadienis": "周四", "ketvirtadienį": "周四",
    "penktadienis": "周五", "penktadienį": "周五",
    "šeštadienis": "周六", "šeštadienį": "周六",
    "sekmadienis": "周日", "sekmadienį": "周日",
}


SUB_TRANSLATE = [
    (r"(?i)\b(?:kitą|ateinantį|artėjantį)\s+(pirmadienis|pirmadienį|antradienis|antradienį|trečiadienis|trečiadienį|ketvirtadienis|ketvirtadienį|penktadienis|penktadienį|šeštadienis|šeštadienį|sekmadienis|sekmadienį)\b",
     lambda m: "下%s" % _LT_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(?:praėjusį|praeitą)\s+(pirmadienis|pirmadienį|antradienis|antradienį|trečiadienis|trečiadienį|ketvirtadienis|ketvirtadienį|penktadienis|penktadienį|šeštadienis|šeštadienį|sekmadienis|sekmadienį)\b",
     lambda m: "上%s" % _LT_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(?:šį|šis)\s+(pirmadienis|pirmadienį|antradienis|antradienį|trečiadienis|trečiadienį|ketvirtadienis|ketvirtadienį|penktadienis|penktadienį|šeštadienis|šeštadienį|sekmadienis|sekmadienį)\b",
     lambda m: "这%s" % _LT_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(pirmadien(?:is|į)|antradien(?:is|į)|trečiadien(?:is|į)|ketvirtadien(?:is|į)|penktadien(?:is|į)|šeštadien(?:is|į)|sekmadien(?:is|į))\b",
     lambda m: "周%s" % {
         "pirmadienis": "一", "pirmadienį": "一", "antradienis": "二",
         "antradienį": "二", "trečiadienis": "三", "trečiadienį": "三",
         "ketvirtadienis": "四", "ketvirtadienį": "四",
         "penktadienis": "五", "penktadienį": "五", "šeštadienis": "六",
         "šeštadienį": "六", "sekmadienis": "日", "sekmadienį": "日"}[
            m.group(1).lower()]),
    (r"(?iu)\b(?:sausis|sausio)\b", "1月"),
    (r"(?iu)\b(?:vasaris|vasario)\b", "2月"),
    (r"(?iu)\b(?:kovas|kovo)\b", "3月"),
    (r"(?iu)\b(?:balandis|balandžio)\b", "4月"),
    (r"(?iu)\b(?:gegužė|gegužės)\b", "5月"),
    (r"(?iu)\b(?:birželis|birželio)\b", "6月"),
    (r"(?iu)\b(?:liepa|liepos)\b", "7月"),
    (r"(?iu)\b(?:rugpjūtis|rugpjūčio)\b", "8月"),
    (r"(?iu)\b(?:rugsėjis|rugsėjo)\b", "9月"),
    (r"(?iu)\b(?:spalis|spalio)\b", "10月"),
    (r"(?iu)\b(?:lapkritis|lapkričio)\b", "11月"),
    (r"(?iu)\b(?:gruodis|gruodžio)\b", "12月"),
    (r"(?i)\b(?P<Y>\d{4})\s+m\.\s+(?P<m>\d{1,2})月\s+(?P<d>\d{1,2})(?:\s*d\.)?(?!\w)",
     lambda m: "%s年%s月%s日" % (m.group("Y"), m.group("m"), m.group("d"))),
    (r"\bužvakar\b", "前天"),
    (r"\bporyt\b", "后天"),
    (r"(?i)\b(?:šį\s+rytą|šiandien\s+ryt(?:ą|e))\b", "今天 08:00 am"),
    (r"(?i)\b(?:šį\s+vakarą|šiandien\s+vakar(?:ą|e))\b", "今天 20:00 pm"),
    (r"(?i)\b(?:rytoj\s+ryt(?:ą|e)|rytą\s+rytoj)\b", "明天 08:00 am"),
    (r"(?i)\b(?:rytoj\s+vakar(?:ą|e))\b", "明天 20:00 pm"),
    (r"(?i)\b(?:vakar\s+vakar(?:ą|e))\b", "昨天 20:00 pm"),
    (r"(?i)\b(?:vidurdienį|per\s+pietus)\b", "12:00 pm"),
    (r"(?i)\bvidurnaktį\b", "12:00 am"),
    (r"\bšiandien\b", "今天"),
    (r"\bvakar\b", "昨天"),
    (r"\brytoj\b", "明天"),
    (r"po\s+(?P<a>\d+)\s*(?P<b>%s)" % _LT_UNIT_RE, _lt_later),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+vėliau" % _LT_UNIT_RE, _lt_later),
    (r"prieš\s+(?P<a>\d+)\s*(?P<b>%s)" % _LT_UNIT_RE, _lt_earlier),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+anksčiau" % _LT_UNIT_RE, _lt_earlier),
    (r"\b(?:dabar|šiuo\s+metu)\b", "刚刚"),
    (r"\bkitą\s+savaitę\b", "下周"),
    (r"\bpraėjusią\s+savaitę\b", "上周"),
    (r"\bkitą\s+mėnesį\b", "下个月"),
    (r"\bpraėjusį\s+mėnesį\b", "上个月"),
    (r"\bkitais\s+metais\b", "明年"),
    (r"\bpraėjusiais\s+metais\b", "去年"),
]
