# -*- coding: utf-8 -*-

import datetime

import pytest

from gggdtparser import parse


dt = datetime.datetime
BASE = dt(2026, 9, 18, 15, 4, 5)


HU_MONTHS = [
    ("január", 1), ("február", 2), ("március", 3), ("április", 4),
    ("május", 5), ("június", 6), ("július", 7), ("augusztus", 8),
    ("szeptember", 9), ("október", 10), ("november", 11), ("december", 12),
]
HU_ABBRS = [
    ("jan.", 1), ("febr.", 2), ("márc.", 3), ("ápr.", 4),
    ("máj.", 5), ("jún.", 6), ("júl.", 7), ("aug.", 8),
    ("szept.", 9), ("okt.", 10), ("nov.", 11), ("dec.", 12),
]
PL_NOM_MONTHS = [
    ("styczeń", 1), ("luty", 2), ("marzec", 3), ("kwiecień", 4),
    ("maj", 5), ("czerwiec", 6), ("lipiec", 7), ("sierpień", 8),
    ("wrzesień", 9), ("październik", 10), ("listopad", 11),
    ("grudzień", 12),
]
PL_GEN_MONTHS = [
    ("stycznia", 1), ("lutego", 2), ("marca", 3), ("kwietnia", 4),
    ("maja", 5), ("czerwca", 6), ("lipca", 7), ("sierpnia", 8),
    ("września", 9), ("października", 10), ("listopada", 11),
    ("grudnia", 12),
]
PL_ABBRS = [
    ("sty", 1), ("lut", 2), ("mar", 3), ("kwi", 4), ("maj", 5),
    ("cze", 6), ("lip", 7), ("sie", 8), ("wrz", 9), ("paź", 10),
    ("lis", 11), ("gru", 12),
]
FI_MONTHS = [
    ("tammikuussa", 1), ("helmikuussa", 2), ("maaliskuussa", 3),
    ("huhtikuussa", 4), ("toukokuussa", 5), ("kesäkuussa", 6),
    ("heinäkuussa", 7), ("elokuussa", 8), ("syyskuussa", 9),
    ("lokakuussa", 10), ("marraskuussa", 11), ("joulukuussa", 12),
]


def _month_cases(lang, months, day=5):
    return [
        (lang, "5 %s 2023" % name, dt(2023, month, day))
        for name, month in months
    ]


WAVE19_CASES = [
    # Hungarian full month names (sample uppercase forms included)
    ("hu", "5 JANUÁR 2023", dt(2023, 1, 5)),
    ("hu", "5 MÁRCIUS 2023", dt(2023, 3, 5)),
    ("hu", "5 DECEMBER 2023", dt(2023, 12, 5)),
] + _month_cases("hu", HU_MONTHS)

WAVE19_CASES += [
    # Hungarian dotted month abbreviations (sample uppercase included)
    ("hu", "5 FEBR. 2023", dt(2023, 2, 5)),
    ("hu", "5 SZEPT. 2023", dt(2023, 9, 5)),
    ("hu", "5 DEC. 2023", dt(2023, 12, 5)),
] + _month_cases("hu", HU_ABBRS)

WAVE19_CASES += [
    # Polish nominative and genitive month names
    ("pl", "5 WRZESIEŃ 2023", dt(2023, 9, 5)),
] + _month_cases("pl", PL_NOM_MONTHS) + _month_cases("pl", PL_GEN_MONTHS)

WAVE19_CASES += [
    # Polish common month abbreviations
    ("pl", "5 PAŹ 2023", dt(2023, 10, 5)),
] + _month_cases("pl", PL_ABBRS)

WAVE19_CASES += [
    # Finnish inessive month forms ("in March" etc.)
    ("fi", "HELMIKUUSSA 5, 2023", dt(2023, 2, 5)),
    ("fi", "JOULUKUUSSA 5, 2023", dt(2023, 12, 5)),
] + [
    ("fi", "%s 5, 2023" % name, dt(2023, month, 5))
    for name, month in FI_MONTHS
]


@pytest.mark.parametrize("lang,text,expected", WAVE19_CASES)
def test_wave19_global_scenarios(lang, text, expected):
    assert parse(text, langs=[lang], base_datetime=BASE) == expected
