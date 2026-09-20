# -*- coding:utf-8 -*-

"""
加利西亚语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_GL_UNIT_MAP = {
    "segundo": "秒", "segundos": "秒",
    "minuto": "分钟", "minutos": "分钟",
    "hora": "小时", "horas": "小时",
    "día": "天", "días": "天",
    "semana": "周", "semanas": "周",
    "mes": "月", "meses": "月",
    "ano": "年", "anos": "年",
}
_GL_UNIT_RE = (
    r"segundo[s]?|minuto[s]?|hora[s]?|dí[ao][s]?|"
    r"semana[s]?|mes(?:es)?|ano[s]?"
)


def _gl_later(match):
    return "%s%s后" % (match.group("a"), _GL_UNIT_MAP[match.group("b")])


def _gl_earlier(match):
    return "%s%s前" % (match.group("a"), _GL_UNIT_MAP[match.group("b")])


SUB_TRANSLATE = [
    (r"(?i)\bxaneiro\b", "1月"),
    (r"(?i)\bfebreiro\b", "2月"),
    (r"(?i)\bmarzo\b", "3月"),
    (r"(?i)\babril\b", "4月"),
    (r"(?i)\bmaio\b", "5月"),
    (r"(?i)\bxuño\b", "6月"),
    (r"(?i)\bxullo\b", "7月"),
    (r"(?i)\bagosto\b", "8月"),
    (r"(?i)\bsetembro\b", "9月"),
    (r"(?i)\boutubro\b", "10月"),
    (r"(?i)\bnovembro\b", "11月"),
    (r"(?i)\bdecembro\b", "12月"),
    (r"(?i)\bantonte\b", "前天"),
    (r"(?i)\bpasadomañá\b", "后天"),
    (r"(?i)\bhoxe\b", "今天"),
    (r"(?i)\bonte\b", "昨天"),
    (r"(?i)\bmañá\b", "明天"),
    (r"(?i)\bagora\b", "刚刚"),
    (r"(?i)(?:en|dentro\s+de)\s+(?P<a>\d+)\s*(?P<b>%s)" % _GL_UNIT_RE,
     _gl_later),
    (r"(?i)hai\s+(?P<a>\d+)\s*(?P<b>%s)" % _GL_UNIT_RE, _gl_earlier),
    (r"(?i)a\s+próxima\s+semana|a\s+semana\s+que\s+vén", "下周"),
    (r"(?i)a\s+semana\s+pasada", "上周"),
    (r"(?i)o\s+próximo\s+mes|o\s+mes\s+que\s+vén", "下个月"),
    (r"(?i)o\s+mes\s+pasado", "上个月"),
    (r"(?i)o\s+próximo\s+ano|o\s+ano\s+que\s+vén", "明年"),
    (r"(?i)o\s+ano\s+pasado", "去年"),
]
