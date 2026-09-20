# -*- coding:utf-8 -*-

"""
加泰罗尼亚语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_CA_UNITS = {
    "segon": "秒", "segons": "秒",
    "minut": "分钟", "minuts": "分钟",
    "hora": "小时", "hores": "小时",
    "dia": "天", "dies": "天",
    "setmana": "周", "setmanes": "周",
    "mes": "月", "mesos": "月",
    "any": "年", "anys": "年",
}

SUB_TRANSLATE = [
    (r"\bgener\b", "1月"),
    (r"\bfebrer\b", "2月"),
    (r"\bmarç\b", "3月"),
    (r"\babril\b", "4月"),
    (r"\bmaig\b", "5月"),
    (r"\bjuny\b", "6月"),
    (r"\bjuliol\b", "7月"),
    (r"\bagost\b", "8月"),
    (r"\bsetembre\b", "9月"),
    (r"\boctubre\b", "10月"),
    (r"\bnovembre\b", "11月"),
    (r"\bdesembre\b", "12月"),
    (r"\babans-d'ahir\b", "前天"),
    (r"\bdemà\s+passat\b", "后天"),
    (r"\bavui\b", "今天"),
    (r"\bahir\b", "昨天"),
    (r"\bdemà\b", "明天"),
    (r"(?:en|d'aquí)\s+(?P<num>\d+)\s*(?P<unit>segons?|minuts?|hores?|dies?|setmanes?|mesos?|anys?)",
     lambda m: "%s%s后" % (
         m.group("num"),
         {"segon": "秒", "segons": "秒", "minut": "分钟",
          "minuts": "分钟", "hora": "小时", "hores": "小时",
          "dia": "天", "dies": "天", "setmana": "周",
          "setmanes": "周", "mes": "月", "mesos": "月",
          "any": "年", "anys": "年"}[m.group("unit")])),
    (r"fa\s+(?P<num>\d+)\s*(?P<unit>segons?|minuts?|hores?|dies?|setmanes?|mesos?|anys?)",
     lambda m: "%s%s前" % (
         m.group("num"),
         {"segon": "秒", "segons": "秒", "minut": "分钟",
          "minuts": "分钟", "hora": "小时", "hores": "小时",
          "dia": "天", "dies": "天", "setmana": "周",
          "setmanes": "周", "mes": "月", "mesos": "月",
          "any": "年", "anys": "年"}[m.group("unit")])),
    (r"\b(?:ara\s+mateix|ara)\b", "刚刚"),
    (r"\bla\s+setmana\s+que\s+ve\b", "下周"),
    (r"\bla\s+setmana\s+passada\b", "上周"),
    (r"\bel\s+mes\s+que\s+ve\b", "下个月"),
    (r"\bel\s+mes\s+passat\b", "上个月"),
    (r"\bl'any\s+que\s+ve\b", "明年"),
    (r"\bl'any\s+passat\b", "去年"),
    (r"(?P<d>\d{1,2})\s+de\s+(?P<m>\d{1,2})月\s+de\s+(?P<Y>\d{4})",
     lambda m: "%s年%s月%s日" % (m.group("Y"), m.group("m"), m.group("d"))),
]
