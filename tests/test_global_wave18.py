# -*- coding: utf-8 -*-

import datetime

import pytest

from gggdtparser import parse


dt = datetime.datetime
BASE = dt(2026, 9, 18, 15, 4, 5)


UK_MONTHS = [
    ("січня", 1), ("лютого", 2), ("березня", 3), ("квітня", 4),
    ("травня", 5), ("червня", 6), ("липня", 7), ("серпня", 8),
    ("вересня", 9), ("жовтня", 10), ("листопада", 11), ("грудня", 12),
]
SK_MONTHS = [
    ("januára", 1), ("februára", 2), ("marca", 3), ("apríla", 4),
    ("mája", 5), ("júna", 6), ("júla", 7), ("augusta", 8),
    ("septembra", 9), ("októbra", 10), ("novembra", 11), ("decembra", 12),
]
SL_MONTHS = [
    ("januarja", 1), ("februarja", 2), ("marca", 3), ("aprila", 4),
    ("maja", 5), ("junija", 6), ("julija", 7), ("avgusta", 8),
    ("septembra", 9), ("oktobra", 10), ("novembra", 11), ("decembra", 12),
]
HR_MONTHS = [
    ("siječnja", 1), ("veljače", 2), ("ožujka", 3), ("travnja", 4),
    ("svibnja", 5), ("lipnja", 6), ("srpnja", 7), ("kolovoza", 8),
    ("rujna", 9), ("listopada", 10), ("studenoga", 11), ("prosinca", 12),
]
SR_MONTHS = [
    ("јануара", 1), ("фебруара", 2), ("марта", 3), ("априла", 4),
    ("маја", 5), ("јуна", 6), ("јула", 7), ("августа", 8),
    ("септембра", 9), ("октобра", 10), ("новембра", 11), ("децембра", 12),
]
LT_MONTHS = [
    ("sausio", 1), ("vasario", 2), ("kovo", 3), ("balandžio", 4),
    ("gegužės", 5), ("birželio", 6), ("liepos", 7), ("rugpjūčio", 8),
    ("rugsėjo", 9), ("spalio", 10), ("lapkričio", 11), ("gruodžio", 12),
]
LV_MONTHS = [
    ("janvāra", "janvārī", 1), ("februāra", "februārī", 2),
    ("marta", "martā", 3), ("aprīļa", "aprīlī", 4),
    ("maija", "majā", 5), ("jūnija", "jūnijā", 6),
    ("jūlija", "jūlijā", 7), ("augusta", "augustā", 8),
    ("septembra", "septembrī", 9), ("oktobra", "oktobrī", 10),
    ("novembra", "novembrī", 11), ("decembra", "decembrī", 12),
]
ET_MONTHS = [
    ("jaanuaril", 1), ("veebruaril", 2), ("märtsil", 3), ("aprillil", 4),
    ("mail", 5), ("juunil", 6), ("juulil", 7), ("augustil", 8),
    ("septembril", 9), ("oktoobril", 10), ("novembril", 11),
    ("detsembril", 12),
]


def _month_cases(lang, months, day=5):
    return [
        (lang, "5. %s 2023" % name, dt(2023, month, day))
        for name, month in months
    ]


WAVE18_CASES = [
    # Ukrainian genitive months and weekday abbreviations
    ("uk", "ПН, 5 ЛЮТОГО 2023", dt(2023, 2, 5)),
    ("uk", "пн", dt(2026, 9, 14)),
    ("uk", "нд", dt(2026, 9, 20)),
] + _month_cases("uk", UK_MONTHS)

WAVE18_CASES += [
    # Slovak genitive months
    ("sk", "5. JANUÁRA 2023", dt(2023, 1, 5)),
    ("sk", "po", dt(2026, 9, 14)),
    ("sk", "ne", dt(2026, 9, 20)),
] + _month_cases("sk", SK_MONTHS)

WAVE18_CASES += [
    # Slovenian genitive months
    ("sl", "5. JANUARJA 2023", dt(2023, 1, 5)),
    ("sl", "pon.", dt(2026, 9, 14)),
] + _month_cases("sl", SL_MONTHS)

WAVE18_CASES += [
    # Croatian genitive months
    ("hr", "5. SIJEČNJA 2023", dt(2023, 1, 5)),
    ("hr", "pon.", dt(2026, 9, 14)),
] + _month_cases("hr", HR_MONTHS)

WAVE18_CASES += [
    # Serbian (Cyrillic) genitive months
    ("sr", "5. ЈАНУАРА 2023", dt(2023, 1, 5)),
] + _month_cases("sr", SR_MONTHS)

WAVE18_CASES += [
    # Lithuanian genitive months: month-first and year-first forms
    ("lt", "Sausio 5, 2023", dt(2023, 1, 5)),
    ("lt", "2023 M. SAUSIO 5 D.", dt(2023, 1, 5)),
] + [
    ("lt", "2023 m. %s %d d." % (name, 5 + index), dt(2023, month, 5 + index))
    for index, (name, month) in enumerate(LT_MONTHS)
]

WAVE18_CASES += [
    # Latvian genitive and locative months, including gada structure
    ("lv", "2023. GADA 5. JANVĀRĪ", dt(2023, 1, 5)),
] + [
    ("lv", "5. %s 2023" % gen, dt(2023, month, 5))
    for gen, _, month in LV_MONTHS
] + [
    ("lv", "2023. gada %d. %s" % (5 + index, loc),
     dt(2023, month, 5 + index))
    for index, (_, loc, month) in enumerate(LV_MONTHS)
]

WAVE18_CASES += [
    # Estonian adessive month forms
    ("et", "5. JAANUARIL 2023", dt(2023, 1, 5)),
] + _month_cases("et", ET_MONTHS)

WAVE18_CASES += [
    # French dotted weekday/month abbreviations
    ("fra", "lun. 5 févr. 2023", dt(2023, 2, 5)),
    ("fra", "LUN. 5 FÉVR. 2023", dt(2023, 2, 5)),
    ("fra", "mar. 7 févr. 2023", dt(2023, 2, 7)),
    ("fra", "5 janv. 2023", dt(2023, 1, 5)),
    ("fra", "5 avr. 2023", dt(2023, 4, 5)),
    ("fra", "5 sept. 2023", dt(2023, 9, 5)),
    ("fra", "5 déc. 2023", dt(2023, 12, 5)),
    ("fra", "5 MARS 2023", dt(2023, 3, 5)),
    ("fra", "lun.", dt(2026, 9, 14)),
    # Spanish weekday/month abbreviations
    ("es", "lun 5 feb 2023", dt(2023, 2, 5)),
    ("es", "LUN 5 FEB 2023", dt(2023, 2, 5)),
    ("es", "mar 5 mar 2023", dt(2023, 3, 5)),
    ("es", "lun 5 de febrero de 2023", dt(2023, 2, 5)),
    ("es", "LUN 5 DE FEBRERO DE 2023", dt(2023, 2, 5)),
    ("es", "5 ene 2023", dt(2023, 1, 5)),
    ("es", "31 dic 2023", dt(2023, 12, 31)),
    ("es", "lun", dt(2026, 9, 14)),
    # Italian weekday/month abbreviations with and without dots
    ("it", "lun 5 feb 2023", dt(2023, 2, 5)),
    ("it", "LUN 5 FEB 2023", dt(2023, 2, 5)),
    ("it", "mar 5 mar 2023", dt(2023, 3, 5)),
    ("it", "LUN 5 FEBBRAIO 2023", dt(2023, 2, 5)),
    ("it", "5 feb. 2023", dt(2023, 2, 5)),
    ("it", "5 mag 2023", dt(2023, 5, 5)),
    ("it", "5 dic. 2023", dt(2023, 12, 5)),
    ("it", "lun", dt(2026, 9, 14)),
    # Portuguese weekday/month abbreviations
    ("swe", "seg 5 fev 2023", dt(2023, 2, 5)),
    ("swe", "SEG 5 FEV 2023", dt(2023, 2, 5)),
    ("swe", "ter 5 mar 2023", dt(2023, 3, 5)),
    ("swe", "SEG 5 FEVEREIRO 2023", dt(2023, 2, 5)),
    ("swe", "5 fev. 2023", dt(2023, 2, 5)),
    ("swe", "31 dez 2023", dt(2023, 12, 31)),
    ("swe", "seg", dt(2026, 9, 14)),
    # Czech weekday abbreviations and day-first numeric dates
    ("cs", "po 6. 2. 2023", dt(2023, 2, 6)),
    ("cs", "ST 7. 6. 2023", dt(2023, 6, 7)),
    ("cs", "po 5. 2. 2023", dt(2023, 2, 5)),
    ("cs", "po", dt(2026, 9, 14)),
    # Romanian dotted month abbreviations
    ("ro", "5 ian. 2023", dt(2023, 1, 5)),
    ("ro", "5 FEB. 2023", dt(2023, 2, 5)),
    ("ro", "5 FEBRUARIE 2023", dt(2023, 2, 5)),
    ("ro", "5 nov. 2023", dt(2023, 11, 5)),
]


@pytest.mark.parametrize("lang,text,expected", WAVE18_CASES)
def test_wave18_global_scenarios(lang, text, expected):
    assert parse(text, langs=[lang], base_datetime=BASE) == expected
