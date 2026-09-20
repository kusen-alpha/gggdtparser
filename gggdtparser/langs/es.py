# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/5/16


"""
西班牙语
"""

ACCURATE_REGEX_LIST = [
]

_ES_MONTH_ABBRS = {
    "ene": 1, "feb": 2, "mar": 3, "abr": 4, "may": 5, "jun": 6,
    "jul": 7, "ago": 8, "sep": 9, "set": 9, "oct": 10, "nov": 11,
    "dic": 12,
}
_ES_WEEKDAY_ABBRS = {
    "lun": "一", "mié": "三", "mie": "三", "jue": "四",
    "vie": "五", "sáb": "六", "sab": "六", "dom": "日",
}


SUB_TRANSLATE = [
    (r"(?i)\b(?:lun|mar|mi[ée]|jue|vie|s[áa]b|dom)\.?\s+"
     r"(?P<d>\d{1,2})\s+(?:de\s+)?"
     r"(?P<mo>ene|feb|mar|abr|may|jun|jul|ago|sep|set|oct|nov|dic)\.?\s+"
     r"(?:de\s+)?(?P<Y>\d{4})",
     lambda m: "%s年%s月%s日" % (
         m.group("Y"), _ES_MONTH_ABBRS[m.group("mo").lower().rstrip(".")],
         m.group("d"))),
    (r"(?i)\b(?:el\s+)?(?:pr[óo]ximo|pr[óo]xima)\s+(?:(lunes|martes|mi[ée]rcoles|jueves|viernes|s[áa]bado|domingo))\b",
     lambda m: "下%s" % {
         "lunes": "周一", "martes": "周二", "miércoles": "周三",
         "miercoles": "周三", "jueves": "周四", "viernes": "周五",
         "sábado": "周六", "sabado": "周六", "domingo": "周日"}[
            m.group(1).lower()]),
    (r"(?i)\b(?:(lunes|martes|mi[ée]rcoles|jueves|viernes|s[áa]bado|domingo))\s+(?:pr[óo]ximo|pr[óo]xima)\b",
     lambda m: "下%s" % {
         "lunes": "周一", "martes": "周二", "miércoles": "周三",
         "miercoles": "周三", "jueves": "周四", "viernes": "周五",
         "sábado": "周六", "sabado": "周六", "domingo": "周日"}[
            m.group(1).lower()]),
    (r"(?i)\b(?:(lunes|martes|mi[ée]rcoles|jueves|viernes|s[áa]bado|domingo))\s+(?:pasado|pasada|anterior)\b",
     lambda m: "上%s" % {
         "lunes": "周一", "martes": "周二", "miércoles": "周三",
         "miercoles": "周三", "jueves": "周四", "viernes": "周五",
         "sábado": "周六", "sabado": "周六", "domingo": "周日"}[
            m.group(1).lower()]),
    (r"(?i)\b(?:el\s+)?(?:(lunes|martes|mi[ée]rcoles|jueves|viernes|s[áa]bado|domingo))\s+(?:que\s+viene)\b",
     lambda m: "下%s" % {
         "lunes": "周一", "martes": "周二", "miércoles": "周三",
         "miercoles": "周三", "jueves": "周四", "viernes": "周五",
         "sábado": "周六", "sabado": "周六", "domingo": "周日"}[
            m.group(1).lower()]),
    (r"(?i)\beste\s+(?:(lunes|martes|mi[ée]rcoles|jueves|viernes|s[áa]bado|domingo))\b",
     lambda m: "这%s" % {
         "lunes": "周一", "martes": "周二", "miércoles": "周三",
         "miercoles": "周三", "jueves": "周四", "viernes": "周五",
         "sábado": "周六", "sabado": "周六", "domingo": "周日"}[
            m.group(1).lower()]),
    (r"(?i)\b(lunes|martes|mi[ée]rcoles|jueves|viernes|s[áa]bado|domingo)\b",
     lambda m: "周%s" % {
         "lunes": "一", "martes": "二", "miércoles": "三",
         "miercoles": "三", "jueves": "四", "viernes": "五",
         "sábado": "六", "sabado": "六", "domingo": "日"}[
            m.group(1).lower()]),
    (r"(?i)\b(?:lun|mi[ée]|jue|vie|s[áa]b|dom)\.?(?!\w)",
     lambda m: "周%s" % _ES_WEEKDAY_ABBRS[
         m.group(0).lower().rstrip(".")]),
    (r"(?i)\best[ae]\s+mañana\b", "今天 08:00 am"),
    (r"(?i)\best[ae]\s+tarde\b", "今天 15:00 pm"),
    (r"(?i)\best[ae]\s+noche\b", "今天 22:00 pm"),
    (r"(?i)\banoche\b", "昨天 22:00 pm"),
    (r"(?i)\bmañana\s+por\s+la\s+mañana\b", "明天 08:00 am"),
    (r"(?i)\bmañana\s+por\s+la\s+tarde\b", "明天 15:00 pm"),
    (r"(?i)\bmañana\s+por\s+la\s+noche\b", "明天 20:00 pm"),
    (r"(?i)\ba\s+mediodía\b|\ba\s+mediodia\b", "12:00 pm"),
    (r"(?i)\ba\s+medianoche\b", "12:00 am"),
    (r"(?i)(de)?\s*enero\s*(de)?", "1月"),
    (r"(?i)(de)?\s*febrero\s*(de)?", "2月"),
    (r"(?i)(de)?\s*marzo\s*(de)?", "3月"),
    (r"(?i)(de)?\s*abril\s*(de)?", "4月"),
    (r"(?i)(de)?\s*mayo\s*(de)?", "5月"),
    (r"(?i)(de)?\s*junio\s*(de)?", "6月"),
    (r"(?i)(de)?\s*julio\s*(de)?", "7月"),
    (r"(?i)(de)?\s*agosto\s*(de)?", "8月"),
    (r"(?i)(de)?\s*septiembre\s*(de)?", "9月"),
    (r"(?i)(de)?\s*octubre\s*(de)?", "10月"),
    (r"(?i)(de)?\s*noviembre\s*(de)?", "11月"),
    (r"(?i)(de)?\s*diciembre\s*(de)?", "12月"),
    (r"(?i)\b(?:ene|feb|mar|abr|may|jun|jul|ago|sep|set|oct|nov|dic)\.?(?!\w)",
     lambda m: "%s月" % _ES_MONTH_ABBRS[
         m.group(0).lower().rstrip(".")]),
    (r"(?i)\banteayer\b|\bantier\b", "前天"),
    (r"(?i)\bpasado\s+mañana\b", "后天"),
    (r"(?i)\bayer\b", "昨天"),
    (r"(?i)\bhoy\b", "今天"),
    (r"(?i)\bmañana\b", "明天"),
    (r"(?i)\bahora\s+mismo\b|\bjusto\s+ahora\b", "刚刚"),
    (r"(?i)(?:en|dentro\s+de)\s*(?P<num>\d+)\s*(?P<unit>segundos?|minutos?|horas?|días?|semanas?|meses?|años?)(?:\s+despu[ée]s)?",
     lambda m: "%s%s后" % (
         m.group("num"),
         {"segundo": "秒", "segundos": "秒", "minuto": "分钟",
          "minutos": "分钟", "hora": "小时", "horas": "小时",
          "día": "天", "días": "天", "semana": "周", "semanas": "周",
          "mes": "月", "meses": "月", "año": "年", "años": "年"}[
             m.group("unit").lower()])),
    (r"(?i)(?P<num>\d+)\s*(?P<unit>segundos?|minutos?|horas?|días?|semanas?|meses?|años?)\s+(?:despu[ée]s|m[áa]s\s+tarde)",
     lambda m: "%s%s后" % (
         m.group("num"),
         {"segundo": "秒", "segundos": "秒", "minuto": "分钟",
          "minutos": "分钟", "hora": "小时", "horas": "小时",
          "día": "天", "días": "天", "semana": "周", "semanas": "周",
          "mes": "月", "meses": "月", "año": "年", "años": "年"}[
             m.group("unit").lower()])),
    (r"(?i)hace\s*(?P<num>\d+)\s*(?P<unit>segundos?|minutos?|horas?|días?|semanas?|meses?|años?)",
     lambda m: "%s%s前" % (
         m.group("num"),
         {"segundo": "秒", "segundos": "秒", "minuto": "分钟",
          "minutos": "分钟", "hora": "小时", "horas": "小时",
          "día": "天", "días": "天", "semana": "周", "semanas": "周",
          "mes": "月", "meses": "月", "año": "年", "años": "年"}[
             m.group("unit").lower()])),
    (r"(?i)(?P<num>\d+)\s*(?P<unit>segundos?|minutos?|horas?|días?|semanas?|meses?|años?)\s+(?:atr[áa]s|antes)",
     lambda m: "%s%s前" % (
         m.group("num"),
         {"segundo": "秒", "segundos": "秒", "minuto": "分钟",
          "minutos": "分钟", "hora": "小时", "horas": "小时",
          "día": "天", "días": "天", "semana": "周", "semanas": "周",
          "mes": "月", "meses": "月", "año": "年", "años": "年"}[
             m.group("unit").lower()])),
    (r"(?i)(?:la\s+)?(?:pr[óo]xim[oa]\s+semana\b|semana\s+que\s+viene\b)", "下周"),
    (r"(?i)(?:la\s+)?semana\s+(?:pasada|anterior)", "上周"),
    (r"(?i)(?:el\s+)?(?:pr[óo]xim[oa]\s+mes\b|mes\s+que\s+viene\b)", "下个月"),
    (r"(?i)(?:el\s+)?mes\s+(?:pasado|anterior)", "上个月"),
    (r"(?i)(?:el\s+)?(?:pr[óo]xim[oa]\s+a[ñn]o\b|a[ñn]o\s+que\s+viene\b)", "明年"),
    (r"(?i)(?:el\s+)?a[ñn]o\s+(?:pasado|anterior)", "去年"),
]
FUZZY_REGEX_LIST = []
