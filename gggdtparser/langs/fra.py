# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/5/16


"""
法语
"""

ACCURATE_REGEX_LIST = [
    # 31/03/23 à 12h03
    r"(?P<d>\d{1,2})\s*[\-\|/\.日]\s*(?P<m>\d{1,2})\s*[\-\|/\.月]\s*(?P<Y>\d{2,4})\s*[,]?\s*(?P<H>\d{1,2})\s*[:时h\.]\s*(?P<M>\d{1,2})\s*[:分]?",

    # before
    r"(il y a)?\s*(?P<bH>\d+)\s*heures?\s*(ago)?",
]

SUB_TRANSLATE = [
    (r"(?i)\b(?:(lundi|mardi|mercredi|jeudi|vendredi|samedi|dimanche))\s+(?:prochain|prochaine)\b",
     lambda m: "下%s" % {
         "lundi": "周一", "mardi": "周二", "mercredi": "周三",
         "jeudi": "周四", "vendredi": "周五", "samedi": "周六",
         "dimanche": "周日"}[m.group(1).lower()]),
    (r"(?i)\b(?:(lundi|mardi|mercredi|jeudi|vendredi|samedi|dimanche))\s+(?:dernier|dernière|derniere)\b",
     lambda m: "上%s" % {
         "lundi": "周一", "mardi": "周二", "mercredi": "周三",
         "jeudi": "周四", "vendredi": "周五", "samedi": "周六",
         "dimanche": "周日"}[m.group(1).lower()]),
    (r"(?i)\bcet?\s+(?:(lundi|mardi|mercredi|jeudi|vendredi|samedi|dimanche))\b",
     lambda m: "这%s" % {
         "lundi": "周一", "mardi": "周二", "mercredi": "周三",
         "jeudi": "周四", "vendredi": "周五", "samedi": "周六",
         "dimanche": "周日"}[m.group(1).lower()]),
    (r"(?i)\b(lundi|mardi|mercredi|jeudi|vendredi|samedi|dimanche)\b",
     lambda m: "周%s" % {
         "lundi": "一", "mardi": "二", "mercredi": "三",
         "jeudi": "四", "vendredi": "五", "samedi": "六",
         "dimanche": "日"}[m.group(1).lower()]),
    (r"(?i)\b(?:lun\.|mar\.|mer\.|jeu\.|ven\.|sam\.|dim\.)(?!\w)",
     lambda m: "周%s" % {
         "lun.": "一", "mar.": "二", "mer.": "三", "jeu.": "四",
         "ven.": "五", "sam.": "六", "dim.": "日"}[m.group(0).lower()]),
    (r"(?i)\bce\s+matin\b", "今天 08:00 am"),
    (r"(?i)\bce\s+midi\b", "今天 12:00 pm"),
    (r"(?i)\bcet\s+après-midi\b|\bcet\s+apres-midi\b", "今天 15:00 pm"),
    (r"(?i)\bce\s+soir\b", "今天 22:00 pm"),
    (r"(?i)\bcette\s+nuit\b", "今天 23:00 pm"),
    (r"(?i)\bhier\s+matin\b", "昨天 08:00 am"),
    (r"(?i)\bhier\s+soir\b", "昨天 20:00 pm"),
    (r"(?i)\bdemain\s+matin\b", "明天 08:00 am"),
    (r"(?i)\bdemain\s+midi\b", "明天 12:00 pm"),
    (r"(?i)\bdemain\s+soir\b", "明天 20:00 pm"),
    (r"(?i)\bà\s+midi\b", "12:00 pm"),
    (r"(?i)\bà\s+minuit\b", "12:00 am"),
    (r"(?i)\bjanvier\b|\bjanv\.?(?!\w)", "1月"),
    (r"(?i)\bf[ée]vrier\b|\bf[ée]v(?:r)?\.?(?!\w)", "2月"),
    (r"(?i)\bmars\.?(?!\w)", "3月"),
    (r"(?i)\bavril\b|\bavr\.?(?!\w)", "4月"),
    (r"(?i)\bmai\.?(?!\w)", "5月"),
    (r"(?i)\bjuin\.?(?!\w)", "6月"),
    (r"(?i)\bjuillet\b|\bjuil\.?(?!\w)", "7月"),
    (r"(?i)\bao[uû]t\.?(?!\w)|\baout\.?(?!\w)", "8月"),
    (r"(?i)\bseptembre\b|\bsept\.?(?!\w)", "9月"),
    (r"(?i)\boctobre\b|\boct\.?(?!\w)", "10月"),
    (r"(?i)\bnovembre\b|\bnov\.?(?!\w)", "11月"),
    (r"(?i)\bd[ée]cembre\b|\bd[ée]c\.?(?!\w)|\bdec\.?(?!\w)", "12月"),
    (r"aujourd’hui à", ""),
    (r"à l’instant", "刚刚"),
    (r"hier à", "昨天"),
    (r"à", ""),
    (r"après-demain|après demain", "后天"),
    (r"avant-hier|avant hier", "前天"),
    (r"aujourd’hui|aujourd'hui", "今天"),
    (r"demain", "明天"),
    (r"hier", "昨天"),
    (r"maintenant\b", "刚刚"),
    (r"dans\s+(?P<num>\d+)\s*(?P<unit>secondes?|minutes?|heures?|jours?|semaines?|mois|ans?)(?:\s+plus\s+tard)?",
     lambda m: "%s%s后" % (
         m.group("num"),
         {"seconde": "秒", "secondes": "秒", "minute": "分钟",
          "minutes": "分钟", "heure": "小时", "heures": "小时",
          "jour": "天", "jours": "天", "semaine": "周", "semaines": "周",
          "mois": "月", "an": "年", "ans": "年"}[m.group("unit").lower()])),
    (r"d'ici\s+(?P<num>\d+)\s*(?P<unit>secondes?|minutes?|heures?|jours?|semaines?|mois|ans?)",
     lambda m: "%s%s后" % (
         m.group("num"),
         {"seconde": "秒", "secondes": "秒", "minute": "分钟",
          "minutes": "分钟", "heure": "小时", "heures": "小时",
          "jour": "天", "jours": "天", "semaine": "周", "semaines": "周",
          "mois": "月", "an": "年", "ans": "年"}[m.group("unit").lower()])),
    (r"il\s+y\s+a\s+(?P<num>\d+)\s*(?P<unit>secondes?|minutes?|heures?|jours?|semaines?|mois|ans?)",
     lambda m: "%s%s前" % (
         m.group("num"),
         {"seconde": "秒", "secondes": "秒", "minute": "分钟",
          "minutes": "分钟", "heure": "小时", "heures": "小时",
          "jour": "天", "jours": "天", "semaine": "周", "semaines": "周",
          "mois": "月", "an": "年", "ans": "年"}[m.group("unit").lower()])),
    (r"(?P<num>\d+)\s*(?P<unit>secondes?|minutes?|heures?|jours?|semaines?|mois|ans?)\s+(?:plus\s+t[ôo]t|auparavant)",
     lambda m: "%s%s前" % (
         m.group("num"),
         {"seconde": "秒", "secondes": "秒", "minute": "分钟",
          "minutes": "分钟", "heure": "小时", "heures": "小时",
          "jour": "天", "jours": "天", "semaine": "周", "semaines": "周",
          "mois": "月", "an": "年", "ans": "年"}[m.group("unit").lower()])),
    (r"(?:la\s+)?semaine\s+prochaine\b", "下周"),
    (r"(?:la\s+)?semaine\s+(?:derni[èe]re|pr[ée]c[ée]dente)\b", "上周"),
    (r"(?:le\s+)?mois\s+prochain\b", "下个月"),
    (r"(?:le\s+)?mois\s+(?:dernier|pr[ée]c[ée]dent)\b", "上个月"),
    (r"(?:l['’])?ann[ée]e\s+prochaine\b", "明年"),
    (r"(?:l['’])?ann[ée]e\s+(?:derni[èe]re|pr[ée]c[ée]dente)\b", "去年"),
]
FUZZY_REGEX_LIST = []
