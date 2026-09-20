# -*- coding:utf-8 -*-

"""
意大利语
"""

ACCURATE_REGEX_LIST = []

_IT_MONTH_ABBRS = {
    "gen": 1, "feb": 2, "mar": 3, "apr": 4, "mag": 5, "giu": 6,
    "lug": 7, "ago": 8, "set": 9, "ott": 10, "nov": 11, "dic": 12,
}
_IT_WEEKDAY_ABBRS = {
    "lun": "一", "mer": "三", "gio": "四",
    "ven": "五", "sab": "六", "dom": "日",
}


SUB_TRANSLATE = [
    (r"(?i)\b(?:lun|mar|mer|gio|ven|sab|dom)\.?\s+"
     r"(?P<d>\d{1,2})\s+"
     r"(?P<mo>gen|feb|mar|apr|mag|giu|lug|ago|set|ott|nov|dic)\.?\s+"
     r"(?P<Y>\d{4})",
     lambda m: "%s年%s月%s日" % (
         m.group("Y"), _IT_MONTH_ABBRS[m.group("mo").lower().rstrip(".")],
         m.group("d"))),
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
    (r"(?i)\b(?:lun|mer|gio|ven|sab|dom)\.?(?!\w)",
     lambda m: "周%s" % _IT_WEEKDAY_ABBRS[
         m.group(0).lower().rstrip(".")]),
    (r"(?i)\bstamattina\b|\bstamani\b", "今天 08:00 am"),
    (r"(?i)\b(?:quest[oa]\s+sera|stasera)\b", "今天 20:00 pm"),
    (r"(?i)\b(?:quest[oa]\s+notte|stanotte)\b", "今天 23:00 pm"),
    (r"(?i)\bieri\s+sera\b", "昨天 20:00 pm"),
    (r"(?i)\bdomani\s+mattina\b", "明天 08:00 am"),
    (r"(?i)\bdomani\s+sera\b", "明天 20:00 pm"),
    (r"(?i)\ba\s+mezzogiorno\b", "12:00 pm"),
    (r"(?i)\ba\s+mezzanotte\b", "12:00 am"),
    (r"(?i)\bgennaio\b|\bgen\.?(?!\w)", "1月"),
    (r"(?i)\bfebbraio\b|\bfeb\.?(?!\w)", "2月"),
    (r"(?i)\bmarzo\b|\bmar\.?(?!\w)", "3月"),
    (r"(?i)\baprile\b|\bapr\.?(?!\w)", "4月"),
    (r"(?i)\bmaggio\b|\bmag\.?(?!\w)", "5月"),
    (r"(?i)\bgiugno\b|\bgiu\.?(?!\w)", "6月"),
    (r"(?i)\bluglio\b|\blug\.?(?!\w)", "7月"),
    (r"(?i)\bagosto\b|\bago\.?(?!\w)", "8月"),
    (r"(?i)\bsettembre\b|\bset\.?(?!\w)", "9月"),
    (r"(?i)\bottobre\b|\bott\.?(?!\w)", "10月"),
    (r"(?i)\bnovembre\b|\bnov\.?(?!\w)", "11月"),
    (r"(?i)\bdicembre\b|\bdic\.?(?!\w)", "12月"),
    (r"(?i)\b(?:gen|feb|mar|apr|mag|giu|lug|ago|set|ott|nov|dic)\.?(?!\w)",
     lambda m: "%s月" % _IT_MONTH_ABBRS[
         m.group(0).lower().rstrip(".")]),
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
