# -*- coding:utf-8 -*-

"""
捷克语
"""

ACCURATE_REGEX_LIST = []

SUB_TRANSLATE = [
    (r"\bledna\b|\bleden\b", "1月"),
    (r"\búnora\b|\búnor\b", "2月"),
    (r"\bbřezna\b|\bbřezen\b", "3月"),
    (r"\bdubna\b|\bduben\b", "4月"),
    (r"\bkvětna\b|\bkvěten\b", "5月"),
    (r"\bčervna\b|\bčerven\b", "6月"),
    (r"\bčervence\b|\bčervenec\b", "7月"),
    (r"\bsrpna\b|\bsrpen\b", "8月"),
    (r"\bz[áa]ří\b", "9月"),
    (r"\bříjna\b|\bříjen\b", "10月"),
    (r"\blistopadu\b|\blistopad\b", "11月"),
    (r"\bprosince\b|\bprosinec\b|\bpros\b", "12月"),
    (r"pondělí", ""),
    (r"úterý|úter", ""),
    (r"středa|střed", ""),
    (r"čtvrtek|čtvrtk", ""),
    (r"pátek|pátk", ""),
    (r"sobota|sobot", ""),
    (r"neděle|neděl", ""),
    (r"(?P<num>\d+)\s*hodinami?\s*zpět", lambda m: "%s小时前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*minutami?\s*zpět", lambda m: "%s分钟前" % int(m.group("num"))),
    (r"(?P<num>\d+)\s*dny?\s*zpět", lambda m: "%s天前" % int(m.group("num"))),
    (r"právě teď", "刚刚"),
    (r"předevčírem", "前天"),
    (r"pozítří", "后天"),
    (r"dnes", "今天"),
    (r"včera", "昨天"),
    (r"zítra", "明天"),
    (r"za\s+(?P<num>\d+)\s*(?P<unit>sekundu|sekundy|sekund|minutu|minuty|minut|hodinu|hodiny|hodin|den|dny|dní|týden|týdny|týdnů|měsíc|měsíce|rok|roky|let)",
     lambda m: "%s%s后" % (
         m.group("num"),
         {"sekunda": "秒", "sekundy": "秒", "sekund": "秒",
          "minuta": "分钟", "minuty": "分钟", "minut": "分钟",
          "hodina": "小时", "hodiny": "小时", "hodin": "小时",
          "den": "天", "dny": "天", "dní": "天",
          "týden": "周", "týdny": "周", "týdnů": "周",
          "měsíc": "月", "měsíce": "月", "rok": "年",
          "roky": "年", "let": "年"}[m.group("unit")])),
    (r"příští\s+týden\b", "下周"),
    (r"minulý\s+týden\b", "上周"),
    (r"příští\s+měsíc\b", "下个月"),
    (r"minulý\s+měsíc\b", "上个月"),
    (r"příští\s+rok\b", "明年"),
    (r"minulý\s+rok\b", "去年"),
]

FUZZY_REGEX_LIST = []
