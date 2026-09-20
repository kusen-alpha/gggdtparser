# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/5/16


"""
葡萄牙语
"""

ACCURATE_REGEX_LIST = [
    r"(?P<bS>\d+)\s*segundos?\s*",
    r"(?P<bM>\d+)\s*minutos?\s*",
    r"(?P<bH>\d+)\s*horas?\s*",
    r"(?P<bd>\d+)\s*dias?\s*",
    r"(?P<bm>\d+)\s*meses?\s*",
    r"(?P<ba>\d+)\s*semanas?\s*",
    r"(?P<bY>\d+)\s*anos?\s*",
]

SUB_TRANSLATE = [
    (r"(de)?\s*janeiro\s*(de)?", "1月"),
    (r"Fev\.?", "2月"),
    (r"(de)?\s*fevereiro\s*(de)?", "2月"),
    (r"(de)?\s*março\s*(de)?", "3月"),
    (r"(de)?\s*abril\s*(de)?", "4月"),
    (r"(de)?\s*maio\s*(de)?", "5月"),
    (r"(de)?\s*junho\s*(de)?", "6月"),
    (r"(de)?\s*julho\s*(de)?", "7月"),
    (r"(de)?\s*agosto\s*(de)?", "8月"),
    (r"(de)?\s*setembro\s*(de)?", "9月"),
    (r"(de)?\s*outubro\s*(de)?", "10月"),
    (r"(de)?\s*novembro\s*(de)?", "11月"),
    (r"(de)?\s*dezembro\s*(de)?", "12月"),
    (r"anteontem", "前天"),
    (r"depois\s+de\s+amanhã", "后天"),
    (r"ontem", "昨天"),
    (r"hoje", "今天"),
    (r"amanhã", "明天"),
    (r"agora\s+mesmo|agora", "刚刚"),
    (r"(?:em|daqui\s+a)\s+(?P<num>\d+)\s*(?P<unit>segundos?|minutos?|horas?|dias?|semanas?|meses?|anos?)",
     lambda m: "%s%s后" % (
         m.group("num"),
         {"segundo": "秒", "segundos": "秒", "minuto": "分钟",
          "minutos": "分钟", "hora": "小时", "horas": "小时",
          "dia": "天", "dias": "天", "semana": "周", "semanas": "周",
          "mês": "月", "meses": "月", "ano": "年", "anos": "年"}[
             m.group("unit").lower()])),
    (r"(?P<num>\d+)\s*(?P<unit>segundos?|minutos?|horas?|dias?|semanas?|meses?|anos?)\s+depois",
     lambda m: "%s%s后" % (
         m.group("num"),
         {"segundo": "秒", "segundos": "秒", "minuto": "分钟",
          "minutos": "分钟", "hora": "小时", "horas": "小时",
          "dia": "天", "dias": "天", "semana": "周", "semanas": "周",
          "mês": "月", "meses": "月", "ano": "年", "anos": "年"}[
             m.group("unit").lower()])),
    (r"(?:h[áa])\s+(?P<num>\d+)\s*(?P<unit>segundos?|minutos?|horas?|dias?|semanas?|meses?|anos?)",
     lambda m: "%s%s前" % (
         m.group("num"),
         {"segundo": "秒", "segundos": "秒", "minuto": "分钟",
          "minutos": "分钟", "hora": "小时", "horas": "小时",
          "dia": "天", "dias": "天", "semana": "周", "semanas": "周",
          "mês": "月", "meses": "月", "ano": "年", "anos": "年"}[
             m.group("unit").lower()])),
    (r"pr[oó]xima\s+semana\b", "下周"),
    (r"semana\s+passada\b", "上周"),
    (r"pr[oó]ximo\s+m[êe]s\b", "下个月"),
    (r"m[êe]s\s+passado\b", "上个月"),
    (r"pr[oó]ximo\s+ano\b", "明年"),
    (r"ano\s+passado\b", "去年"),
]
FUZZY_REGEX_LIST = []
