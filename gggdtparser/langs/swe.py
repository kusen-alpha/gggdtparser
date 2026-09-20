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

_PT_WEEKDAYS = {
    "segunda": "周一",
    "terca": "周二",
    "quarta": "周三",
    "quinta": "周四",
    "sexta": "周五",
    "sabado": "周六",
    "sábado": "周六",
    "domingo": "周日",
}


def _pt_weekday(value):
    return _PT_WEEKDAYS[value.lower().replace("ç", "c").replace("-feira", "")]


SUB_TRANSLATE = [
    (r"(?i)\bpr[óo]xim[oa]\s+((?:segunda|ter[çc]a|quarta|quinta|sexta|s[áa]bado|domingo)(?:-feira)?)\b",
     lambda m: "下%s" % _pt_weekday(m.group(1))),
    (r"(?i)\b((?:segunda|ter[çc]a|quarta|quinta|sexta|s[áa]bado|domingo)(?:-feira)?)\s+que\s+vem\b",
     lambda m: "下%s" % _pt_weekday(m.group(1))),
    (r"(?i)\b((?:segunda|ter[çc]a|quarta|quinta|sexta|s[áa]bado|domingo)(?:-feira)?)\s+(?:passada|passado|anterior)\b",
     lambda m: "上%s" % _pt_weekday(m.group(1))),
    (r"(?i)\best[ao]\s+((?:segunda|ter[çc]a|quarta|quinta|sexta|s[áa]bado|domingo)(?:-feira)?)\b",
     lambda m: "这%s" % _pt_weekday(m.group(1))),
    (r"(?i)\bsegunda(?:-feira)?\b", "周一"),
    (r"(?i)\bter[çc]a(?:-feira)?\b", "周二"),
    (r"(?i)\bquarta(?:-feira)?\b", "周三"),
    (r"(?i)\bquinta(?:-feira)?\b", "周四"),
    (r"(?i)\bsexta(?:-feira)?\b", "周五"),
    (r"(?i)\bs[áa]bado\b", "周六"),
    (r"(?i)\bdomingo\b", "周日"),
    (r"(?i)\best[ae]\s+manhã\b", "今天 08:00 am"),
    (r"(?i)\best[ae]\s+tarde\b", "今天 15:00 pm"),
    (r"(?i)\best[ae]\s+noite\b", "今天 20:00 pm"),
    (r"(?i)\bamanhã\s+(?:de|pela)\s+manhã\b", "明天 08:00 am"),
    (r"(?i)\bamanhã\s+(?:de|pela)\s+tarde\b", "明天 15:00 pm"),
    (r"(?i)\bamanhã\s+(?:à|de|pela)\s+noite\b", "明天 20:00 pm"),
    (r"(?i)\bontem\s+(?:de|pela)\s+manhã\b", "昨天 08:00 am"),
    (r"(?i)\bontem\s+(?:à|de)\s+noite\b", "昨天 20:00 pm"),
    (r"(?i)\bao\s+meio\s*[- ]?dia\b", "12:00 pm"),
    (r"(?i)\bà\s+meia\s*[- ]?noite\b", "12:00 am"),
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
