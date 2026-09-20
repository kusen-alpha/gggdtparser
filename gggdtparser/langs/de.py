# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/5/16


"""
德语
"""

ACCURATE_REGEX_LIST = [
    # 02.02.2022, 02.02 Uhr
    r"(?P<d>\d{1,2})\s*[\-\|/\.]\s*(?P<m>\d{1,2})\s*[\-\|/\.]\s*(?P<Y>\d{2,4})\s*[,]?\s*(?P<H>\d{1,2})[\.:]\s*(?P<M>\d{1,2})\s*(?:Uhr|uhr|am|pm)?",
    # 02.02.2022
    r"(?P<d>\d{1,2})\s*[\-\|/\.]\s*(?P<m>\d{1,2})\s*[\-\|/\.]\s*(?P<Y>\d{2,4})",
]

SUB_TRANSLATE = [
    (r"Januar|Jan", "1月"),
    (r"Februar|Feb\.", "2月"),
    (r"März|Mär", "3月"),
    (r"April|Apr", "4月"),
    (r"Abriil|Abr", "4月"),
    (r"Mai|mai", "5月"),
    (r"Juni|Jun", "6月"),
    (r"Juli|Jnl", "7月"),
    (r"August|Aug", "8月"),
    (r"September|Sep\.", "9月"),
    (r"Oktober|Okt", "10月"),
    (r"November|Nov", "11月"),
    (r"Dezember|Dez", "12月"),
    (r"Uhr", "am"),
    (r"une heure", "1 heure"),
    (r"il y a heure", "il y a 1 heure"),
    (r"vorgestern", "前天"),
    (r"gestern", "昨天"),
    (r"heute", "今天"),
    (r"morgen", "明天"),
    (r"übermorgen|uebermorgen", "后天"),
    (r"gerade eben|jetzt gerade", "刚刚"),
    (r"in\s+(?P<num>\d+)\s*(?P<unit>Sekunde|Sekunden|Minute|Minuten|Stunde|Stunden|Tag|Tage|Tagen|Woche|Wochen|Monat|Monate|Monaten|Jahr|Jahre|Jahren)(?:\s+später)?",
     lambda m: "%s%s后" % (
         m.group("num"),
         {"Sekunde": "秒", "Sekunden": "秒", "Minute": "分钟",
          "Minuten": "分钟", "Stunde": "小时", "Stunden": "小时",
          "Tag": "天", "Tage": "天", "Tagen": "天",
          "Woche": "周", "Wochen": "周", "Monat": "月",
          "Monaten": "月", "Monate": "月", "Jahr": "年",
          "Jahre": "年", "Jahren": "年"}[m.group("unit")])),
    (r"(?P<num>\d+)\s*(?P<unit>Sekunde|Sekunden|Minute|Minuten|Stunde|Stunden|Tag|Tage|Tagen|Woche|Wochen|Monat|Monate|Monaten|Jahr|Jahre|Jahren)\s+später",
     lambda m: "%s%s后" % (
         m.group("num"),
         {"Sekunde": "秒", "Sekunden": "秒", "Minute": "分钟",
          "Minuten": "分钟", "Stunde": "小时", "Stunden": "小时",
          "Tag": "天", "Tage": "天", "Tagen": "天",
          "Woche": "周", "Wochen": "周", "Monat": "月",
          "Monaten": "月", "Monate": "月", "Jahr": "年",
          "Jahre": "年", "Jahren": "年"}[m.group("unit")])),
    (r"vor\s+(?P<num>\d+)\s*(?P<unit>Sekunde|Sekunden|Minute|Minuten|Stunde|Stunden|Tag|Tage|Tagen|Woche|Wochen|Monat|Monate|Monaten|Jahr|Jahre|Jahren)",
     lambda m: "%s%s前" % (
         m.group("num"),
         {"Sekunde": "秒", "Sekunden": "秒", "Minute": "分钟",
          "Minuten": "分钟", "Stunde": "小时", "Stunden": "小时",
          "Tag": "天", "Tage": "天", "Tagen": "天",
          "Woche": "周", "Wochen": "周", "Monat": "月",
          "Monaten": "月", "Monate": "月", "Jahr": "年",
          "Jahre": "年", "Jahren": "年"}[m.group("unit")])),
    (r"(?P<num>\d+)\s*(?P<unit>Sekunde|Sekunden|Minute|Minuten|Stunde|Stunden|Tag|Tage|Tagen|Woche|Wochen|Monat|Monate|Monaten|Jahr|Jahre|Jahren)\s+(?:her|früher)",
     lambda m: "%s%s前" % (
         m.group("num"),
         {"Sekunde": "秒", "Sekunden": "秒", "Minute": "分钟",
          "Minuten": "分钟", "Stunde": "小时", "Stunden": "小时",
          "Tag": "天", "Tage": "天", "Tagen": "天",
          "Woche": "周", "Wochen": "周", "Monat": "月",
          "Monaten": "月", "Monate": "月", "Jahr": "年",
          "Jahre": "年", "Jahren": "年"}[m.group("unit")])),
    (r"(?:nächste|kommende)\s+Woche\b", "下周"),
    (r"(?:letzte|vergangene)\s+Woche\b", "上周"),
    (r"(?:nächste[nrs]?|kommende[nrs]?)\s+Monat\b", "下个月"),
    (r"(?:letzte[nrs]?|vergangene[nrs]?)\s+Monat\b", "上个月"),
    (r"(?:nächstes|kommendes)\s+Jahr\b", "明年"),
    (r"(?:letztes|vergangenes)\s+Jahr\b", "去年"),
]
FUZZY_REGEX_LIST = []
