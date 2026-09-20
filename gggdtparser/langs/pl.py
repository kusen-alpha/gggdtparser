# -*- coding:utf-8 -*-

"""
波兰语
"""

ACCURATE_REGEX_LIST = []

SUB_TRANSLATE = [
    (r"stycznia|styczeń|stycze?nia", "1月"),
    (r"lutego|luty|lut", "2月"),
    (r"marca|marzec|mar", "3月"),
    (r"kwietnia|kwiecień", "4月"),
    (r"maja|maj", "5月"),
    (r"czerwca|czerwiec", "6月"),
    (r"lipca|lipiec", "7月"),
    (r"sierpnia|sierpień", "8月"),
    (r"września|wrzesień", "9月"),
    (r"października|październik", "10月"),
    (r"listopada|listopad", "11月"),
    (r"grudnia|grudzień", "12月"),
    (r"poniedziałek|poniedział", ""),
    (r"wtorek|wtork", ""),
    (r"środa|środ|środe", ""),
    (r"czwartek|czwartk", ""),
    (r"piątek|piąt|piatek", ""),
    (r"sobota|sobot", ""),
    (r"niedziela|niedziel", ""),
    (r"(?P<num>\d+)\s*godzin[aiy]?\s*temu", lambda m: "%s小时前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*minut[aoy]?\s*temu", lambda m: "%s分钟前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*dni?\s*temu", lambda m: "%s天前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*tygodni\s*temu", lambda m: "%s周前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*miesięc[yi]?\s*temu", lambda m: "%s月前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*lat\s*temu", lambda m: "%s年前" % int(m.group("num"))),
    (r"przed chwilą|właśnie", "刚刚"),
    (r"przedwczoraj", "前天"),
    (r"pojutrze", "后天"),
    (r"dzisiaj|dziś", "今天"),
    (r"wczoraj", "昨天"),
    (r"jutro", "明天"),
    (r"za\s+(?P<num>\d+)\s*(?P<unit>sekund[ęy]?|minut[ęy]?|godzin[ęy]?|dni?|tygodni[ae]?|miesi[ąe]c[ei]?|lat[ao]?)",
     lambda m: "%s%s后" % (
         m.group("num"),
         {"sekundę": "秒", "sekundy": "秒", "sekund": "秒",
          "minutę": "分钟", "minuty": "分钟", "minut": "分钟",
          "godzinę": "小时", "godziny": "小时", "godzin": "小时",
          "dzień": "天", "dni": "天", "dniem": "天",
          "tydzień": "周", "tygodnie": "周", "tygodnia": "周",
          "miesiąc": "月", "miesiące": "月", "miesiąca": "月",
          "rok": "年", "lata": "年", "lat": "年", "latem": "年"}[
             m.group("unit").lower()])),
    (r"(?P<num>\d+)\s*(?P<unit>minut[ęy]?|godzin[ęy]?|dni?|tygodni[ae]?|miesi[ąe]c[ei]?|lat[ao]?)\s+p[oó]źniej",
     lambda m: "%s%s后" % (
         m.group("num"),
         {"minutę": "分钟", "minuty": "分钟", "minut": "分钟",
          "godzinę": "小时", "godziny": "小时", "godzin": "小时",
          "dzień": "天", "dni": "天", "dniem": "天",
          "tydzień": "周", "tygodnie": "周", "tygodnia": "周",
          "miesiąc": "月", "miesiące": "月", "miesiąca": "月",
          "rok": "年", "lata": "年", "lat": "年", "latem": "年"}[
             m.group("unit").lower()])),
    (r"(?P<num>\d+)\s*(?:tygodni[ae]?|miesi[ąe]c[ei]?|lat[ao]?)\s*temu",
     lambda m: "%s%s前" % (
         m.group("num"),
         {"tydzień": "周", "tygodnie": "周", "tygodnia": "周",
          "miesiąc": "月", "miesiące": "月", "miesiąca": "月",
          "rok": "年", "lata": "年", "lat": "年", "latem": "年"}[
             m.group("unit").lower()])),
    (r"w\s+przyszłym\s+tygodniu\b|przyszły\s+tydzień\b", "下周"),
    (r"w\s+zeszłym\s+tygodniu\b|zeszły\s+tydzień\b", "上周"),
    (r"w\s+przyszłym\s+miesiącu\b|przyszły\s+miesiąc\b", "下个月"),
    (r"w\s+zeszłym\s+miesiącu\b|zeszły\s+miesiąc\b", "上个月"),
    (r"w\s+przyszłym\s+roku\b|przyszły\s+rok\b", "明年"),
    (r"w\s+zeszłym\s+roku\b|zeszły\s+rok\b", "去年"),
]

FUZZY_REGEX_LIST = []
