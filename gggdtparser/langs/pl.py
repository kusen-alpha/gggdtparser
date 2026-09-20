# -*- coding:utf-8 -*-

"""
波兰语
"""

ACCURATE_REGEX_LIST = []

SUB_TRANSLATE = [
    (r"(?:w\s+)?(?:przyszły|przyszłą|przyszła|następny|następną|następna)\s+(?:poniedziałek|wtorek|środę|środa|czwartek|piątek|sobotę|sobota|niedzielę|niedziela)\b",
     lambda m: "下%s" % {
         "poniedziałek": "周一", "wtorek": "周二", "środę": "周三",
         "środa": "周三", "czwartek": "周四", "piątek": "周五",
         "sobotę": "周六", "sobota": "周六", "niedzielę": "周日",
         "niedziela": "周日"}[m.group(0).split()[-1].lower()]),
    (r"(?:w\s+)?(?:zeszły|zeszłą|zeszła|miniony|minioną|miniona|ubiegły|ubiegłą|ubiegła)\s+(?:poniedziałek|wtorek|środę|środa|czwartek|piątek|sobotę|sobota|niedzielę|niedziela)\b",
     lambda m: "上%s" % {
         "poniedziałek": "周一", "wtorek": "周二", "środę": "周三",
         "środa": "周三", "czwartek": "周四", "piątek": "周五",
         "sobotę": "周六", "sobota": "周六", "niedzielę": "周日",
         "niedziela": "周日"}[m.group(0).split()[-1].lower()]),
    (r"(?:w\s+)?(?:ten|tę|ta)\s+(?:poniedziałek|wtorek|środę|środa|czwartek|piątek|sobotę|sobota|niedzielę|niedziela)\b",
     lambda m: "这%s" % {
         "poniedziałek": "周一", "wtorek": "周二", "środę": "周三",
         "środa": "周三", "czwartek": "周四", "piątek": "周五",
         "sobotę": "周六", "sobota": "周六", "niedzielę": "周日",
         "niedziela": "周日"}[m.group(0).split()[-1].lower()]),
    (r"(?i)\bponiedziałek\b", "周一"),
    (r"(?i)\bwtorek\b", "周二"),
    (r"(?i)\bśroda\b", "周三"),
    (r"(?i)\bczwartek\b", "周四"),
    (r"(?i)\bpiątek\b", "周五"),
    (r"(?i)\bsobota\b", "周六"),
    (r"(?i)\bniedziela\b", "周日"),
    (r"(?i)\b(?:pon\.?|wt\.?|śr\.?|czw\.?|pt\.?|sob\.?|niedz\.?)(?!\w)",
     lambda m: "周%s" % {
         "pon": "一", "wt": "二", "śr": "三", "czw": "四",
         "pt": "五", "sob": "六", "niedz": "日"}[
            m.group(0).lower().rstrip(".")]),
    (r"dzisiaj\s+rano|dziś\s+rano", "今天 08:00 am"),
    (r"dzisiaj\s+po\s+południu|dziś\s+po\s+południu", "今天 15:00 pm"),
    (r"dzisiaj\s+wieczorem|dziś\s+wieczorem", "今天 20:00 pm"),
    (r"w\s+nocy", "今天 23:00 pm"),
    (r"jutro\s+rano", "明天 08:00 am"),
    (r"jutro\s+wieczorem", "明天 20:00 pm"),
    (r"wczoraj\s+wieczorem\b", "昨天 20:00 pm"),
    (r"w\s+południe\b", "12:00 pm"),
    (r"o\s+północy\b", "12:00 am"),
    (r"(?i)\b(?:styczeń|stycznia|stycze?nia|sty)\b", "1月"),
    (r"(?i)\b(?:luty|lutego|lut)\b", "2月"),
    (r"(?i)\b(?:marzec|marca|mar)\b", "3月"),
    (r"(?i)\b(?:kwiecień|kwietnia|kwi)\b", "4月"),
    (r"(?i)\b(?:maj|maja)\b", "5月"),
    (r"(?i)\b(?:czerwiec|czerwca|cze)\b", "6月"),
    (r"(?i)\b(?:lipiec|lipca|lip)\b", "7月"),
    (r"(?i)\b(?:sierpień|sierpnia|sie)\b", "8月"),
    (r"(?i)\b(?:wrzesień|września|wrz)\b", "9月"),
    (r"(?i)\b(?:październik|października|paź)\b", "10月"),
    (r"(?i)\b(?:listopad|listopada|lis)\b", "11月"),
    (r"(?i)\b(?:grudzień|grudnia|gru)\b", "12月"),
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
