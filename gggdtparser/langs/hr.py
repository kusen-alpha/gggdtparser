# -*- coding:utf-8 -*-

"""
克罗地亚语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_HR_UNITS = {
    "sekund": "秒", "sekunda": "秒", "sekunde": "秒",
    "minut": "分钟", "minuta": "分钟", "minute": "分钟",
    "sat": "小时", "sata": "小时", "sati": "小时",
    "dan": "天", "dana": "天",
    "tjedan": "周", "tjedna": "周", "tjedni": "周", "tjedana": "周",
    "mjesec": "月", "mjeseca": "月", "mjeseci": "月",
    "godina": "年", "godine": "年",
}
_HR_UNIT_RE = (
    r"sekund[ae]?|minut[ae]?|sat(?:i|a)?|dan(?:a)?|"
    r"tjedn[ai]|tjedana|mjesec(?:a|i)?|godin[ae]"
)


def _hr_later(match):
    return "%s%s后" % (match.group(1), _HR_UNITS[match.group(2)])


def _hr_earlier(match):
    return "%s%s前" % (match.group(1), _HR_UNITS[match.group(2)])


_HR_WEEKDAYS = {
    "ponedjeljak": "周一",
    "utorak": "周二",
    "srijeda": "周三",
    "četvrtak": "周四",
    "petak": "周五",
    "subota": "周六",
    "nedjelja": "周日",
}


SUB_TRANSLATE = [
    (r"(?i)\b(?:sljedeć[ia]|iduć[ia]|nadolazeć[ia])\s+(ponedjeljak|utorak|srijeda|četvrtak|petak|subota|nedjelja)\b",
     lambda m: "下%s" % _HR_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(?:prošl[ia]|prethodn[ia])\s+(ponedjeljak|utorak|srijeda|četvrtak|petak|subota|nedjelja)\b",
     lambda m: "上%s" % _HR_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(?:ovaj|ova)\s+(ponedjeljak|utorak|srijeda|četvrtak|petak|subota|nedjelja)\b",
     lambda m: "这%s" % _HR_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(ponedjeljak|utorak|srijeda|četvrtak|petak|subota|nedjelja)\b",
     lambda m: "周%s" % {
         "ponedjeljak": "一", "utorak": "二", "srijeda": "三",
         "četvrtak": "四", "petak": "五", "subota": "六",
         "nedjelja": "日"}[m.group(1).lower()]),
    (r"(?i)\b(?:pon\.|uto\.|sri\.|čet\.|pet\.|sub\.|ned\.)(?!\w)",
     lambda m: "周%s" % {
         "pon.": "一", "uto.": "二", "sri.": "三", "čet.": "四",
         "pet.": "五", "sub.": "六", "ned.": "日"}[m.group(0).lower()]),
    (r"(?iu)\b(?:siječanj|siječnja)\b", "1月"),
    (r"(?iu)\b(?:veljača|veljače)\b", "2月"),
    (r"(?iu)\b(?:ožujak|ožujka)\b", "3月"),
    (r"(?iu)\b(?:travanj|travnja)\b", "4月"),
    (r"(?iu)\b(?:svibanj|svibnja)\b", "5月"),
    (r"(?iu)\b(?:lipanj|lipnja)\b", "6月"),
    (r"(?iu)\b(?:srpanj|srpnja)\b", "7月"),
    (r"(?iu)\b(?:kolovoz|kolovoza)\b", "8月"),
    (r"(?iu)\b(?:rujan|rujna)\b", "9月"),
    (r"(?iu)\b(?:listopad|listopada)\b", "10月"),
    (r"(?iu)\b(?:studeni|studenoga)\b", "11月"),
    (r"(?iu)\b(?:prosinac|prosinca)\b", "12月"),
    (r"\bprekjučer\b", "前天"),
    (r"\bprekosutra\b", "后天"),
    (r"(?i)\bdanas\s+(?:ujutro|ujutra|u\s+jutro)\b", "今天 08:00 am"),
    (r"(?i)\bdanas\s+popodne\b", "今天 15:00 pm"),
    (r"(?i)\bdanas\s+(?:navečer|u\s+večer)\b", "今天 20:00 pm"),
    (r"(?i)\bsutra\s+(?:ujutro|ujutra|u\s+jutro)\b", "明天 08:00 am"),
    (r"(?i)\bsutra\s+popodne\b", "明天 15:00 pm"),
    (r"(?i)\bsutra\s+(?:navečer|u\s+večer)\b", "明天 20:00 pm"),
    (r"(?i)\bjučer\s+(?:navečer|u\s+večer)\b", "昨天 20:00 pm"),
    (r"(?i)\b(?:u\s+podne|podne)\b", "12:00 pm"),
    (r"(?i)\bponoć\b", "12:00 am"),
    (r"(?i)\b(?:jutros|večeras)\b",
     lambda m: "今天 08:00 am" if m.group(0).lower() == "jutros" else "今天 20:00 pm"),
    (r"\bdanas\b", "今天"),
    (r"\bjučer\b", "昨天"),
    (r"\bsutra\b", "明天"),
    (r"za\s+(?P<a>\d+)\s*(?P<b>%s)" % _HR_UNIT_RE, _hr_later),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+kasnije" % _HR_UNIT_RE, _hr_later),
    (r"prije\s+(?P<a>\d+)\s*(?P<b>%s)" % _HR_UNIT_RE, _hr_earlier),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+ranije" % _HR_UNIT_RE, _hr_earlier),
    (r"\b(?:upravo\s+sada|sada)\b", "刚刚"),
    (r"\bsljedeći\s+tjedan\b", "下周"),
    (r"\bprošli\s+tjedan\b", "上周"),
    (r"\bsljedeći\s+mjesec\b", "下个月"),
    (r"\bprošli\s+mjesec\b", "上个月"),
    (r"\bsljedeća\s+godina\b", "明年"),
    (r"\bprošla\s+godina\b", "去年"),
]
