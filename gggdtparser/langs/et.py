# -*- coding:utf-8 -*-

"""
爱沙尼亚语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_ET_UNITS = {
    "sekund": "秒", "sekundit": "秒",
    "minut": "分钟", "minutit": "分钟",
    "minuti": "分钟",
    "tund": "小时", "tundi": "小时",
    "tunni": "小时",
    "päev": "天", "päeva": "天",
    "nädal": "周", "nädalat": "周",
    "nädala": "周",
    "kuu": "月", "kuud": "月",
    "aasta": "年", "aastat": "年",
}
_ET_UNIT_RE = (
    r"sekundit?|minuti|minutit?|tunni|tund|tundi|päeva|päev|"
    r"nädala|nädalat?|kuud?|aasta|aastat"
)

_ET_WEEKDAYS = {
    "esmaspäev": "周一", "esmaspäeval": "周一",
    "teisipäev": "周二", "teisipäeval": "周二",
    "kolmapäev": "周三", "kolmapäeval": "周三",
    "neljapäev": "周四", "neljapäeval": "周四",
    "reede": "周五", "reedel": "周五",
    "laupäev": "周六", "laupäeval": "周六",
    "pühapäev": "周日", "pühapäeval": "周日",
}


def _et_later(match):
    return "%s%s后" % (match.group(1), _ET_UNITS[match.group(2)])


def _et_earlier(match):
    return "%s%s前" % (match.group(1), _ET_UNITS[match.group(2)])


SUB_TRANSLATE = [
    (r"(?i)\b(?:järgmine|järgmise|järgmisel|tulev|tuleva|tuleval)\s+(esmaspäev|esmaspäeval|teisipäev|teisipäeval|kolmapäev|kolmapäeval|neljapäev|neljapäeval|reede|reedel|laupäev|laupäeval|pühapäev|pühapäeval)\b",
     lambda m: "下%s" % _ET_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(?:eelmine|eelmise|eelmisel|möödunud)\s+(esmaspäev|esmaspäeval|teisipäev|teisipäeval|kolmapäev|kolmapäeval|neljapäev|neljapäeval|reede|reedel|laupäev|laupäeval|pühapäev|pühapäeval)\b",
     lambda m: "上%s" % _ET_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(?:see|sel(?:le)?)\s+(esmaspäev|esmaspäeval|teisipäev|teisipäeval|kolmapäev|kolmapäeval|neljapäev|neljapäeval|reede|reedel|laupäev|laupäeval|pühapäev|pühapäeval)\b",
     lambda m: "这%s" % _ET_WEEKDAYS[m.group(1).lower()]),
    (r"(?i)\b(esmaspäev(?:al)?|teisipäev(?:al)?|kolmapäev(?:al)?|neljapäev(?:al)?|reede(?:l)?|laupäev(?:al)?|pühapäev(?:al)?)\b",
     lambda m: "周%s" % {
         "esmaspäev": "一", "esmaspäeval": "一", "teisipäev": "二",
         "teisipäeval": "二", "kolmapäev": "三", "kolmapäeval": "三",
         "neljapäev": "四", "neljapäeval": "四", "reede": "五",
         "reedel": "五", "laupäev": "六", "laupäeval": "六",
         "pühapäev": "日", "pühapäeval": "日"}[m.group(1).lower()]),
    (r"(?iu)\b(?:jaanuar|jaanuari|jaanuaril)\b", "1月"),
    (r"(?iu)\b(?:veebruar|veebruari|veebruaril)\b", "2月"),
    (r"(?iu)\b(?:märts|märtsi|märtsil)\b", "3月"),
    (r"(?iu)\b(?:aprill|aprilli|aprillil)\b", "4月"),
    (r"(?iu)\b(?:mai|mail)\b", "5月"),
    (r"(?iu)\b(?:juuni|juunil)\b", "6月"),
    (r"(?iu)\b(?:juuli|juulil)\b", "7月"),
    (r"(?iu)\b(?:august|augusti|augustil)\b", "8月"),
    (r"(?iu)\b(?:september|septembri|septembril)\b", "9月"),
    (r"(?iu)\b(?:oktoober|oktoobri|oktoobril)\b", "10月"),
    (r"(?iu)\b(?:november|novembri|novembril)\b", "11月"),
    (r"(?iu)\b(?:detsember|detsembri|detsembril)\b", "12月"),
    (r"\büleeile\b", "前天"),
    (r"\bülehomme\b", "后天"),
    (r"(?i)\btäna\s+hommikul\b", "今天 08:00 am"),
    (r"(?i)\btäna\s+pärastlõunal\b", "今天 15:00 pm"),
    (r"(?i)\btäna\s+õhtul\b", "今天 20:00 pm"),
    (r"(?i)\bhomme\s+hommikul\b", "明天 08:00 am"),
    (r"(?i)\bhomme\s+õhtul\b", "明天 20:00 pm"),
    (r"(?i)\beile\s+õhtul\b", "昨天 20:00 pm"),
    (r"(?i)\bkeskpäeval\b", "12:00 pm"),
    (r"(?i)\bkeskööl\b", "12:00 am"),
    (r"\btäna\b", "今天"),
    (r"\beile\b", "昨天"),
    (r"\bhomme\b", "明天"),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+pärast" % _ET_UNIT_RE, _et_later),
    (r"(?P<a>\d+)\s*(?P<b>%s)\s+tagasi" % _ET_UNIT_RE, _et_earlier),
    (r"\b(?:praegu|hetkel)\b", "刚刚"),
    (r"\bjärgmisel\s+nädalal\b", "下周"),
    (r"\beelmisel\s+nädalal\b", "上周"),
    (r"\bjärgmisel\s+kuul\b", "下个月"),
    (r"\beelmisel\s+kuul\b", "上个月"),
    (r"\bjärgmisel\s+aastal\b", "明年"),
    (r"\beelmisel\s+aastal\b", "去年"),
]
