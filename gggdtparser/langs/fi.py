# -*- coding:utf-8 -*-

"""
芬兰语
"""

ACCURATE_REGEX_LIST = []

SUB_TRANSLATE = [
    (r"ensi\s+(maanantai|tiistai|keskiviikko|torstai|perjantai|lauantai|sunnuntai)\b",
     lambda m: "下%s" % {
         "maanantai": "周一", "tiistai": "周二", "keskiviikko": "周三",
         "torstai": "周四", "perjantai": "周五", "lauantai": "周六",
         "sunnuntai": "周日"}[m.group(1).lower()]),
    (r"viime\s+(maanantai|tiistai|keskiviikko|torstai|perjantai|lauantai|sunnuntai)\b",
     lambda m: "上%s" % {
         "maanantai": "周一", "tiistai": "周二", "keskiviikko": "周三",
         "torstai": "周四", "perjantai": "周五", "lauantai": "周六",
         "sunnuntai": "周日"}[m.group(1).lower()]),
    (r"tänä\s+(maanantaina|tiistaina|keskiviikkona|torstaina|perjantaina|lauantaina|sunnuntaina)\b",
     lambda m: "这%s" % {
         "maanantaina": "周一", "tiistaina": "周二", "keskiviikkona": "周三",
         "torstaina": "周四", "perjantaina": "周五", "lauantaina": "周六",
         "sunnuntaina": "周日"}[m.group(1).lower()]),
    (r"maanantai", "周一"),
    (r"tiistai", "周二"),
    (r"keskiviikko", "周三"),
    (r"torstai", "周四"),
    (r"perjantai", "周五"),
    (r"lauantai", "周六"),
    (r"sunnuntai", "周日"),
    (r"tänä\s+aamuna", "今天 08:00 am"),
    (r"tänä\s+iltapäivänä", "今天 15:00 pm"),
    (r"tänä\s+iltana", "今天 20:00 pm"),
    (r"huomisaamuna|huomenna\s+aamulla", "明天 08:00 am"),
    (r"huomenna\s+illalla", "明天 20:00 pm"),
    (r"eilen\s+illalla", "昨天 20:00 pm"),
    (r"keskellä\s+päivää", "12:00 pm"),
    (r"keskiyöllä", "12:00 am"),
    (r"tammikuuta|tammikuu", "1月"),
    (r"helmikuuta|helmikuu", "2月"),
    (r"maaliskuuta|maaliskuu", "3月"),
    (r"huhtikuuta|huhtikuu", "4月"),
    (r"toukokuuta|toukokuu", "5月"),
    (r"kesäkuuta|kesäkuu", "6月"),
    (r"heinäkuuta|heinäkuu", "7月"),
    (r"elokuuta|elokuu", "8月"),
    (r"syyskuuta|syyskuu", "9月"),
    (r"lokakuuta|lokakuu", "10月"),
    (r"marraskuuta|marraskuu", "11月"),
    (r"joulukuuta|joulukuu", "12月"),
    (r"maanantai", ""),
    (r"tiistai", ""),
    (r"keskiviikko", ""),
    (r"torstai", ""),
    (r"perjantai", ""),
    (r"lauantai", ""),
    (r"sunnuntai", ""),
    (r"(?P<num>\d+)\s*tuntia?\s*sitten", lambda m: "%s小时前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*minuuttia?\s*sitten", lambda m: "%s分钟前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*päivää\s*sitten", lambda m: "%s天前" % int(m.group("num"))),
    (r"juuri nyt", "刚刚"),
    (r"toissapäivänä", "前天"),
    (r"ylihuomenna", "后天"),
    (r"tänään", "今天"),
    (r"eilen", "昨天"),
    (r"huomenna", "明天"),
    (r"(?P<num>\d+)\s*(?P<unit>sekunnin|minuutin|tunnin|päivän|viikon|kuukauden|vuoden)\s+(?:kuluttua|päästä)",
     lambda m: "%s%s后" % (
         m.group("num"),
         {"sekunnin": "秒", "minuutin": "分钟", "tunnin": "小时",
          "päivän": "天", "viikon": "周", "kuukauden": "月",
          "vuoden": "年"}[m.group("unit")])),
    (r"ensi\s+viikolla\b", "下周"),
    (r"viime\s+viikolla\b", "上周"),
    (r"ensi\s+kuussa\b", "下个月"),
    (r"viime\s+kuussa\b", "上个月"),
    (r"ensi\s+vuonna\b", "明年"),
    (r"viime\s+vuonna\b", "去年"),
]

FUZZY_REGEX_LIST = []
