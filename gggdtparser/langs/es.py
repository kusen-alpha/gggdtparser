# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/5/16


"""
西班牙语
"""

ACCURATE_REGEX_LIST = [
]

SUB_TRANSLATE = [
    (r"(de)?\s*enero\s*(de)?", "1月"),
    (r"(de)?\s*febrero\s*(de)?", "2月"),
    (r"(de)?\s*marzo\s*(de)?", "3月"),
    (r"(de)?\s*abril\s*(de)?", "4月"),
    (r"(de)?\s*mayo\s*(de)?", "5月"),
    (r"(de)?\s*junio\s*(de)?", "6月"),
    (r"(de)?\s*julio\s*(de)?", "7月"),
    (r"(de)?\s*agosto\s*(de)?", "8月"),
    (r"(de)?\s*septiembre\s*(de)?", "9月"),
    (r"(de)?\s*octubre\s*(de)?", "10月"),
    (r"(de)?\s*noviembre\s*(de)?", "11月"),
    (r"(de)?\s*diciembre\s*(de)?", "12月"),
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
