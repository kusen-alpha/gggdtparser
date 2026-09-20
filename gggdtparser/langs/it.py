# -*- coding:utf-8 -*-

"""
意大利语
"""

ACCURATE_REGEX_LIST = []

SUB_TRANSLATE = [
    (r"(?i)\b(?:(luned[ìi]|marted[ìi]|mercoled[ìi]|gioved[ìi]|venerd[ìi]|sabato|domenica))\s+prossim[oa]\b",
     lambda m: "下%s" % {
         "lunedì": "周一", "lunedi": "周一", "martedì": "周二",
         "martedi": "周二", "mercoledì": "周三", "mercoledi": "周三",
         "giovedì": "周四", "giovedi": "周四", "venerdì": "周五",
         "venerdi": "周五", "sabato": "周六", "domenica": "周日"}[
            m.group(1).lower()]),
    (r"(?i)\bprossim[oa]\s+(?:(luned[ìi]|marted[ìi]|mercoled[ìi]|gioved[ìi]|venerd[ìi]|sabato|domenica))\b",
     lambda m: "下%s" % {
         "lunedì": "周一", "lunedi": "周一", "martedì": "周二",
         "martedi": "周二", "mercoledì": "周三", "mercoledi": "周三",
         "giovedì": "周四", "giovedi": "周四", "venerdì": "周五",
         "venerdi": "周五", "sabato": "周六", "domenica": "周日"}[
            m.group(1).lower()]),
    (r"(?i)\b(?:(luned[ìi]|marted[ìi]|mercoled[ìi]|gioved[ìi]|venerd[ìi]|sabato|domenica))\s+(?:scors[oa]|precedente)\b",
     lambda m: "上%s" % {
         "lunedì": "周一", "lunedi": "周一", "martedì": "周二",
         "martedi": "周二", "mercoledì": "周三", "mercoledi": "周三",
         "giovedì": "周四", "giovedi": "周四", "venerdì": "周五",
         "venerdi": "周五", "sabato": "周六", "domenica": "周日"}[
            m.group(1).lower()]),
    (r"(?i)\bquest[oa]\s+(?:(luned[ìi]|marted[ìi]|mercoled[ìi]|gioved[ìi]|venerd[ìi]|sabato|domenica))\b",
     lambda m: "这%s" % {
         "lunedì": "周一", "lunedi": "周一", "martedì": "周二",
         "martedi": "周二", "mercoledì": "周三", "mercoledi": "周三",
         "giovedì": "周四", "giovedi": "周四", "venerdì": "周五",
         "venerdi": "周五", "sabato": "周六", "domenica": "周日"}[
            m.group(1).lower()]),
    (r"(?i)\b(luned[ìi]|marted[ìi]|mercoled[ìi]|gioved[ìi]|venerd[ìi]|sabato|domenica)\b",
     lambda m: "周%s" % {
         "lunedì": "一", "lunedi": "一", "martedì": "二", "martedi": "二",
         "mercoledì": "三", "mercoledi": "三", "giovedì": "四",
         "giovedi": "四", "venerdì": "五", "venerdi": "五",
         "sabato": "六", "domenica": "日"}[m.group(1).lower()]),
    (r"(?i)\bstamattina\b|\bstamani\b", "今天 08:00 am"),
    (r"(?i)\b(?:quest[oa]\s+sera|stasera)\b", "今天 20:00 pm"),
    (r"(?i)\b(?:quest[oa]\s+notte|stanotte)\b", "今天 23:00 pm"),
    (r"(?i)\bieri\s+sera\b", "昨天 20:00 pm"),
    (r"(?i)\bdomani\s+mattina\b", "明天 08:00 am"),
    (r"(?i)\bdomani\s+sera\b", "明天 20:00 pm"),
    (r"(?i)\ba\s+mezzogiorno\b", "12:00 pm"),
    (r"(?i)\ba\s+mezzanotte\b", "12:00 am"),
    (r"\bgennaio\b|\bgen\.\b", "1月"),
    (r"\bfebbraio\b|\bfeb\.\b", "2月"),
    (r"\bmarzo\b|\bmar\.\b", "3月"),
    (r"\baprile\b|\bapr\.\b", "4月"),
    (r"\bmaggio\b|\bmag\.\b", "5月"),
    (r"\bgiugno\b|\bgiu\.\b", "6月"),
    (r"\bluglio\b|\blug\.\b", "7月"),
    (r"\bagosto\b|\bago\.\b", "8月"),
    (r"\bsettembre\b|\bset\.\b", "9月"),
    (r"\bottobre\b|\bott\.\b", "10月"),
    (r"\bnovembre\b|\bnov\.\b", "11月"),
    (r"\bdicembre\b|\bdic\.\b", "12月"),
    (r"lunedì|lunedi|luned", ""),
    (r"martedì|martedi|marted", ""),
    (r"mercoledì|mercoledi|mercoled", ""),
    (r"giovedì|giovedi|gioved", ""),
    (r"venerdì|venerdi|venerd", ""),
    (r"sabato|sabat", ""),
    (r"domenica|domenic", ""),
    (r"(?P<num>\d+)\s*ore?\s*fa", lambda m: "%s小时前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*minut[ie]?\s*fa", lambda m: "%s分钟前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*giorn[io]\s*fa", lambda m: "%s天前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*settiman[ae]\s*fa", lambda m: "%s周前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*m[ei]si?\s*fa", lambda m: "%s月前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*anni?\s*fa", lambda m: "%s年前" % int(m.group("num"))),
    (r"adesso|ora", "刚刚"),
    (r"l'altro\s+ieri|ieri\s+l'altro", "前天"),
    (r"dopodomani", "后天"),
    (r"oggi", "今天"),
    (r"ieri", "昨天"),
    (r"domani", "明天"),
    (r"(?:tra|fra)\s+(?P<num>\d+)\s*(?P<unit>second[oi]?|minut[oi]?|ore?|giorn[oi]?|settiman[ae]?|mesi?|ann[oi]?)",
     lambda m: "%s%s后" % (
         m.group("num"),
         {"secondo": "秒", "secondi": "秒", "minuto": "分钟",
          "minuti": "分钟", "ora": "小时", "ore": "小时",
          "giorno": "天", "giorni": "天", "settimana": "周",
          "settimane": "周", "mese": "月", "mesi": "月",
          "anno": "年", "anni": "年"}[m.group("unit").lower()])),
    (r"(?P<num>\d+)\s*(?P<unit>second[oi]?|minut[oi]?|ore?|giorn[oi]?|settiman[ae]?|mesi?|ann[oi]?)\s+(?:dopo|più\s+tardi)",
     lambda m: "%s%s后" % (
         m.group("num"),
         {"secondo": "秒", "secondi": "秒", "minuto": "分钟",
          "minuti": "分钟", "ora": "小时", "ore": "小时",
          "giorno": "天", "giorni": "天", "settimana": "周",
          "settimane": "周", "mese": "月", "mesi": "月",
          "anno": "年", "anni": "年"}[m.group("unit").lower()])),
    (r"(?:la\s+)?prossim[oa]\s+settimana\b", "下周"),
    (r"(?:la\s+)?settimana\s+(?:scorsa|precedente)\b", "上周"),
    (r"(?:il\s+)?prossimo\s+mes[ea]\b", "下个月"),
    (r"(?:il\s+)?mes[ea]\s+(?:scorso|precedente)\b", "上个月"),
    (r"(?:l['’])?anno\s+prossimo\b", "明年"),
    (r"(?:l['’])?anno\s+(?:scorso|precedente)\b", "去年"),
]

FUZZY_REGEX_LIST = []
