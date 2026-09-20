# -*- coding:utf-8 -*-

"""
罗马尼亚语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_RO_UNITS = {
    "secundă": "秒", "secunda": "秒", "secunde": "秒",
    "minut": "分钟", "minute": "分钟",
    "oră": "小时", "ora": "小时", "ore": "小时",
    "zi": "天", "zile": "天",
    "săptămână": "周", "săptămâna": "周", "săptămâni": "周",
    "lună": "月", "luna": "月", "luni": "月",
    "an": "年", "ani": "年",
}
_RO_UNIT_RE = (
    r"secund[ăa]|secunde|minut|minute|or[ăa]|ore|zi|zile|"
    r"săptămân[ăa]|săptămâni|lun[ăa]|luni|an|ani"
)


def _ro_later(match):
    return "%s%s后" % (match.group(1), _RO_UNITS[match.group(2)])


def _ro_earlier(match):
    return "%s%s前" % (match.group(1), _RO_UNITS[match.group(2)])


SUB_TRANSLATE = [
    (r"(?i)\b(luni|lunea|marți|marțea|miercuri|miercurea|joi|joia|vineri|vinerea|sâmbătă|sâmbăta|duminică|duminica)\s+viitoare\b",
     lambda m: "下%s" % {
         "luni": "周一", "lunea": "周一", "marți": "周二", "marțea": "周二",
         "miercuri": "周三", "miercurea": "周三", "joi": "周四", "joia": "周四",
         "vineri": "周五", "vinerea": "周五", "sâmbătă": "周六",
         "sâmbăta": "周六", "duminică": "周日", "duminica": "周日"}[
            m.group(1).lower()]),
    (r"(?i)\b(luni|lunea|marți|marțea|miercuri|miercurea|joi|joia|vineri|vinerea|sâmbătă|sâmbăta|duminică|duminica)\s+(?:trecută|trecute)\b",
     lambda m: "上%s" % {
         "luni": "周一", "lunea": "周一", "marți": "周二", "marțea": "周二",
         "miercuri": "周三", "miercurea": "周三", "joi": "周四", "joia": "周四",
         "vineri": "周五", "vinerea": "周五", "sâmbătă": "周六",
         "sâmbăta": "周六", "duminică": "周日", "duminica": "周日"}[
            m.group(1).lower()]),
    (r"(?i)\b(luni|lunea|marți|marțea|miercuri|miercurea|joi|joia|vineri|vinerea|sâmbătă|sâmbăta|duminică|duminica)\s+(?:aceasta|asta)\b",
     lambda m: "这%s" % {
         "luni": "周一", "lunea": "周一", "marți": "周二", "marțea": "周二",
         "miercuri": "周三", "miercurea": "周三", "joi": "周四", "joia": "周四",
         "vineri": "周五", "vinerea": "周五", "sâmbătă": "周六",
         "sâmbăta": "周六", "duminică": "周日", "duminica": "周日"}[
           m.group(1).lower()]),
    (r"(?i)\b(luni|lunea|marți|marțea|miercuri|miercurea|joi|joia|vineri|vinerea|sâmbătă|sâmbăta|duminică|duminica)\b",
     lambda m: "周%s" % {
         "luni": "一", "lunea": "一", "marți": "二", "marțea": "二",
         "miercuri": "三", "miercurea": "三", "joi": "四", "joia": "四",
         "vineri": "五", "vinerea": "五", "sâmbătă": "六", "sâmbăta": "六",
         "duminică": "日", "duminica": "日"}[m.group(1).lower()]),
    (r"\b(?:ianuarie|ian\.)\b", "1月"),
    (r"\b(?:februarie|feb\.)\b", "2月"),
    (r"\bmartie\b|\bmart\.\b", "3月"),
    (r"\baprilie\b|\bapr\.\b", "4月"),
    (r"\bmai\.?\b", "5月"),
    (r"\b(?:iunie|iun\.)\b", "6月"),
    (r"\b(?:iulie|iul\.)\b", "7月"),
    (r"\baugust\b|\baug\.\b", "8月"),
    (r"\b(?:septembrie|sept\.)\b", "9月"),
    (r"\b(?:octombrie|oct\.)\b", "10月"),
    (r"\b(?:noiembrie|nov\.)\b", "11月"),
    (r"\b(?:decembrie|dec\.)\b", "12月"),
    (r"(?i)\bdis\s+dimineață\b|\bîn\s+această\s+dimineață\b", "今天 08:00 am"),
    (r"(?i)\bla\s+prânz\b|\bprânz\b", "12:00 pm"),
    (r"(?i)\bdiseară\b|\bîn\s+această\s+seară\b", "今天 20:00 pm"),
    (r"(?i)\bmâine\s+dimineață\b", "明天 08:00 am"),
    (r"(?i)\bmâine\s+seară\b", "明天 20:00 pm"),
    (r"(?i)\bieri\s+seară\b", "昨天 20:00 pm"),
    (r"(?i)\bla\s+miezul\s+nopții\b", "12:00 am"),
    (r"\balaltăieri\b|\balaltaieri\b", "前天"),
    (r"\bpoimâine\b|\bpoimaine\b", "后天"),
    (r"\bastăzi\b|\bazi\b", "今天"),
    (r"\bieri\b", "昨天"),
    (r"\bmâine\b|\bmaine\b", "明天"),
    (r"peste\s+(?P<a>\d+)\s*(?P<b>%s)" % _RO_UNIT_RE, _ro_later),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+(?:mai\s+târziu|mai\s+tirziu)" % _RO_UNIT_RE, _ro_later),
    (r"(?:acum\s+|cu\s+)(?P<a>\d+)\s*(?P<b>%s)" % _RO_UNIT_RE, _ro_earlier),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+(?:în\s+urmă|mai\s+devreme)" % _RO_UNIT_RE, _ro_earlier),
    (r"\b(?:chiar\s+acum|acum)\b", "刚刚"),
    (r"\bsăptămâna\s+viitoare\b", "下周"),
    (r"\bsăptămâna\s+trecută\b", "上周"),
    (r"\bluna\s+viitoare\b", "下个月"),
    (r"\bluna\s+trecută\b", "上个月"),
    (r"\banul\s+viitor\b", "明年"),
    (r"\banul\s+trecut\b", "去年"),
]
