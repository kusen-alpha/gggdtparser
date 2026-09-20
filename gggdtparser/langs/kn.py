# -*- coding:utf-8 -*-

"""
卡纳达语
"""

ACCURATE_REGEX_LIST = []
FUZZY_REGEX_LIST = []

_KN_DIGITS = str.maketrans("೦೧೨೩೪೫೬೭೮೯", "0123456789")

_KN_MONTHS = {
    "ಜನವರಿ": "1月",
    "ಫೆಬ್ರವರಿ": "2月",
    "ಫೆಬ್ರುವರಿ": "2月",
    "ಮಾರ್ಚ್": "3月",
    "ಏಪ್ರಿಲ್": "4月",
    "ಮೇ": "5月",
    "ಜೂನ್": "6月",
    "ಜುಲೈ": "7月",
    "ಆಗಸ್ಟ್": "8月",
    "ಸೆಪ್ಟೆಂಬರ್": "9月",
    "ಅಕ್ಟೋಬರ್": "10月",
    "ನವೆಂಬರ್": "11月",
    "ಡಿಸೆಂಬರ್": "12月",
}
_KN_MONTHS_RE = "|".join(sorted(_KN_MONTHS, key=len, reverse=True))

_KN_UNIT_MAP = {
    "ಸೆಕೆಂಡು": "秒", "ನಿಮಿಷ": "分钟", "ಗಂಟೆ": "小时",
    "ದಿನ": "天", "ವಾರ": "周", "ತಿಂಗಳು": "月", "ವರ್ಷ": "年",
}
_KN_UNIT_BASE_RE = (
    r"ಸೆಕೆಂಡು|ನಿಮಿಷ|ಗಂಟೆ|ದಿನ|ವಾರ|ತಿಂಗಳು|ವರ್ಷ"
)


def _kn_ascii(value):
    return value.translate(_KN_DIGITS)


def _kn_named_date(match):
    return "%s %s %s" % (
        _kn_ascii(match.group("d")),
        _KN_MONTHS[match.group("name")],
        _kn_ascii(match.group("Y")),
    )


def _kn_later(match):
    return "%s%s后" % (match.group("a"), _KN_UNIT_MAP[match.group("b")])


def _kn_earlier(match):
    return "%s%s前" % (match.group("a"), _KN_UNIT_MAP[match.group("b")])


SUB_TRANSLATE = [
    (r"[೦-೯]+", lambda m: m.group(0).translate(_KN_DIGITS)),
    (r"(?P<d>\d{1,2})\s*(?P<name>%s)\s*(?P<Y>\d{4})" % _KN_MONTHS_RE,
     _kn_named_date),
    (r"(?P<name>%s)\s*(?P<d>\d{1,2})[,\s]+\s*(?P<Y>\d{4})" % _KN_MONTHS_RE,
     _kn_named_date),
    (r"(?P<name>%s)\s*(?P<Y>\d{4})" % _KN_MONTHS_RE,
     lambda m: "%s %s" % (_KN_MONTHS[m.group("name")], m.group("Y"))),
    (r"ನಿನ್ನೆ\s+ಮೊನ್ನೆ", "前天"),
    (r"ನಾಳೆ\s+ಮರುದಿನ", "后天"),
    (r"ನಿನ್ನೆ", "昨天"),
    (r"ಇಂದು", "今天"),
    (r"ನಾಳೆ", "明天"),
    (r"ಈಗ", "刚刚"),
    (r"(?P<a>\d+)\s*(?P<b>%s)(?:ಗಳು|ಗಳ)?\s+(?:ನಂತರ|ನಂತರದ)"
     % _KN_UNIT_BASE_RE, _kn_later),
    (r"(?P<a>\d+)\s*(?P<b>%s)(?:ಗಳು|ಗಳ)?\s+ಹಿಂದೆ" % _KN_UNIT_BASE_RE,
     _kn_earlier),
    (r"ಮುಂದಿನ\s+ವಾರ", "下周"),
    (r"ಕಳೆದ\s+ವಾರ", "上周"),
    (r"ಮುಂದಿನ\s+ತಿಂಗಳು", "下个月"),
    (r"ಕಳೆದ\s+ತಿಂಗಳು", "上个月"),
    (r"ಮುಂದಿನ\s+ವರ್ಷ", "明年"),
    (r"ಕಳೆದ\s+ವರ್ಷ", "去年"),
]

for _month in sorted(_KN_MONTHS, key=len, reverse=True):
    SUB_TRANSLATE.append((_month, _KN_MONTHS[_month]))
