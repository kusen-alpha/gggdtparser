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
    (r"(?i)\b(?:nächste|kommende)\s+Woche\s+(Montag|Dienstag|Mittwoch|Donnerstag|Freitag|Samstag|Sonntag)\b",
     lambda m: "下%s" % {
         "montag": "周一", "dienstag": "周二", "mittwoch": "周三",
         "donnerstag": "周四", "freitag": "周五", "samstag": "周六",
         "sonntag": "周日"}[m.group(1).lower()]),
    (r"(?i)\b(?:letzte|vergangene)\s+Woche\s+(Montag|Dienstag|Mittwoch|Donnerstag|Freitag|Samstag|Sonntag)\b",
     lambda m: "上%s" % {
         "montag": "周一", "dienstag": "周二", "mittwoch": "周三",
         "donnerstag": "周四", "freitag": "周五", "samstag": "周六",
         "sonntag": "周日"}[m.group(1).lower()]),
    (r"(?i)\b(?:(Montag|Dienstag|Mittwoch|Donnerstag|Freitag|Samstag|Sonntag))\s+(?:nächste[nrs]?|kommende[nrs]?)\b",
     lambda m: "下%s" % {
         "montag": "周一", "dienstag": "周二", "mittwoch": "周三",
         "donnerstag": "周四", "freitag": "周五", "samstag": "周六",
         "sonntag": "周日"}[m.group(1).lower()]),
    (r"(?i)\b(?:(?:nächste[nrs]?|kommende[nrs]?))\s+(?:(Montag|Dienstag|Mittwoch|Donnerstag|Freitag|Samstag|Sonntag))\b",
     lambda m: "下%s" % {
         "montag": "周一", "dienstag": "周二", "mittwoch": "周三",
         "donnerstag": "周四", "freitag": "周五", "samstag": "周六",
         "sonntag": "周日"}[m.group(1).lower()]),
    (r"(?i)\b(?:(Montag|Dienstag|Mittwoch|Donnerstag|Freitag|Samstag|Sonntag))\s+(?:letzte[nrs]?|vergangene[nrs]?)\b",
     lambda m: "上%s" % {
         "montag": "周一", "dienstag": "周二", "mittwoch": "周三",
         "donnerstag": "周四", "freitag": "周五", "samstag": "周六",
         "sonntag": "周日"}[m.group(1).lower()]),
    (r"(?i)\b(?:(?:letzte[nrs]?|vergangene[nrs]?))\s+(?:(Montag|Dienstag|Mittwoch|Donnerstag|Freitag|Samstag|Sonntag))\b",
     lambda m: "上%s" % {
         "montag": "周一", "dienstag": "周二", "mittwoch": "周三",
         "donnerstag": "周四", "freitag": "周五", "samstag": "周六",
         "sonntag": "周日"}[m.group(1).lower()]),
    (r"(?i)\bdies(?:en|e|em|er)?\s+(?:(Montag|Dienstag|Mittwoch|Donnerstag|Freitag|Samstag|Sonntag))\b",
     lambda m: "这%s" % {
         "montag": "周一", "dienstag": "周二", "mittwoch": "周三",
         "donnerstag": "周四", "freitag": "周五", "samstag": "周六",
         "sonntag": "周日"}[m.group(1).lower()]),
    (r"(?i)\b(Montag|Dienstag|Mittwoch|Donnerstag|Freitag|Samstag|Sonntag)\b",
     lambda m: "周%s" % {
         "montag": "一", "dienstag": "二", "mittwoch": "三",
         "donnerstag": "四", "freitag": "五", "samstag": "六",
         "sonntag": "日"}[m.group(1).lower()]),
    (r"(?i)\b(?:Mo|Di|Mi|Do|Fr|Sa|So)\.?(?!\w)",
     lambda m: "周%s" % {
         "mo": "一", "di": "二", "mi": "三", "do": "四",
         "fr": "五", "sa": "六", "so": "日"}[m.group(0).lower().rstrip(".")]),
    (r"(?i)\bheute\s+Morgen\b", "今天 08:00 am"),
    (r"(?i)\bheute\s+Abend\b", "今天 20:00 pm"),
    (r"(?i)\bheute\s+Mittag\b", "今天 12:00 pm"),
    (r"(?i)\bheute\s+Nacht\b", "今天 23:00 pm"),
    (r"(?i)\bgestern\s+Abend\b", "昨天 20:00 pm"),
    (r"(?i)\bgestern\s+Morgen\b", "昨天 08:00 am"),
    (r"(?i)\bmorgen\s+früh\b", "明天 08:00 am"),
    (r"(?i)\bmorgen\s+Mittag\b", "明天 12:00 pm"),
    (r"(?i)\bmorgen\s+Abend\b", "明天 20:00 pm"),
    (r"(?i)\bübermorgen\s+Morgen\b", "后天 08:00 am"),
    (r"(?i)\bzu\s+Mittag\b", "12:00 pm"),
    (r"(?i)\bum\s+Mitternacht\b", "12:00 am"),
    (r"(?i)\b(?:Januar|Jan\.?)(?!\w)", "1月"),
    (r"(?i)\b(?:Februar|Feb\.?)(?!\w)", "2月"),
    (r"(?i)\b(?:März|Mär\.?)(?!\w)", "3月"),
    (r"(?i)\b(?:April|Apr\.?)(?!\w)", "4月"),
    (r"(?i)\bMai\.?(?!\w)", "5月"),
    (r"(?i)\b(?:Juni|Jun\.?)(?!\w)", "6月"),
    (r"(?i)\b(?:Juli|Jul\.?)(?!\w)", "7月"),
    (r"(?i)\b(?:August|Aug\.?)(?!\w)", "8月"),
    (r"(?i)\b(?:September|Sept?\.?)(?!\w)", "9月"),
    (r"(?i)\b(?:Oktober|Okt\.?)(?!\w)", "10月"),
    (r"(?i)\b(?:November|Nov\.?)(?!\w)", "11月"),
    (r"(?i)\b(?:Dezember|Dez\.?)(?!\w)", "12月"),
    (r"(?i)\bum\s+(?P<H>\d{1,2})\s*Uhr\b",
     lambda m: "%d:00" % int(m.group("H"))),
    (r"(?i)(?<![\d:.])(?P<H>\d{1,2})\s*Uhr\b",
     lambda m: "%d:00" % int(m.group("H"))),
    (r"Uhr", "am"),
    (r"une heure", "1 heure"),
    (r"il y a heure", "il y a 1 heure"),
    (r"vorgestern", "前天"),
    (r"gestern", "昨天"),
    (r"heute", "今天"),
    (r"morgen", "明天"),
    (r"übermorgen|uebermorgen", "后天"),
    (r"gerade eben|jetzt gerade", "刚刚"),
    (r"(?i)\bin\s+einer\s+halben\s+Stunde\b", "30分钟后"),
    (r"(?i)\bvor\s+einer\s+halben\s+Stunde\b", "30分钟前"),
    (r"(?i)\bin\s+einer\s+(?P<unit>Minute|Stunde|Woche)\b",
     lambda m: "1%s后" % {
         "minute": "分钟", "stunde": "小时", "woche": "周"}[
             m.group("unit").lower()]),
    (r"(?i)\bin\s+einem\s+(?P<unit>Tag|Monat|Jahr)\b",
     lambda m: "1%s后" % {
         "tag": "天", "monat": "月", "jahr": "年"}[
             m.group("unit").lower()]),
    (r"(?i)\bvor\s+einer\s+(?P<unit>Minute|Stunde|Woche)\b",
     lambda m: "1%s前" % {
         "minute": "分钟", "stunde": "小时", "woche": "周"}[
             m.group("unit").lower()]),
    (r"(?i)\bvor\s+einem\s+(?P<unit>Tag|Monat|Jahr)\b",
     lambda m: "1%s前" % {
         "tag": "天", "monat": "月", "jahr": "年"}[
             m.group("unit").lower()]),
    (r"(?i)\beine\s+Stunde\s+später\b", "1小时后"),
    (r"(?i)\beine\s+Stunde\s+(?:her|früher)\b", "1小时前"),
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
