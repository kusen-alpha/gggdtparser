# -*- coding: utf-8 -*-

import datetime

import pytest

from gggdtparser import parse


dt = datetime.datetime
BASE = dt(2026, 9, 18, 15, 4, 5)

_WD_DATES = [
    dt(2026, 9, 14),  # Monday
    dt(2026, 9, 15),  # Tuesday
    dt(2026, 9, 16),  # Wednesday
    dt(2026, 9, 17),  # Thursday
    dt(2026, 9, 18),  # Friday
    dt(2026, 9, 19),  # Saturday
    dt(2026, 9, 20),  # Sunday
]


def _wd_cases(lang, forms):
    return [
        (lang, form, _WD_DATES[index])
        for index, form in enumerate(forms)
    ]


def _month_cases(lang, months, dotted_day=False):
    day_prefix = "5. " if dotted_day else "5 "
    return [
        (lang, day_prefix + name + " 2023", dt(2023, month, 5))
        for name, month in months
    ]


WAVE20_CASES = []

WAVE20_CASES += _wd_cases("de", ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"])
WAVE20_CASES += _wd_cases(
    "de", ["Mo.", "Di.", "Mi.", "Do.", "Fr.", "Sa.", "So."])
WAVE20_CASES += [
    ("de", "FREITAG", dt(2026, 9, 18)),
] + _month_cases(
    "de",
    [("Jan", 1), ("Feb", 2), ("Mär", 3), ("Apr", 4), ("Mai", 5),
     ("Jun", 6), ("Jul", 7), ("Aug", 8), ("Sep", 9), ("Sept", 9),
     ("Okt", 10), ("Nov", 11), ("Dez", 12)],
    dotted_day=True,
)
WAVE20_CASES += _month_cases(
    "de",
    [("Jan.", 1), ("Apr.", 4), ("Sept.", 9), ("Dez.", 12)],
    dotted_day=True,
)

WAVE20_CASES += _wd_cases("nl", ["ma", "di", "wo", "do", "vr", "za", "zo"])
WAVE20_CASES += _wd_cases(
    "nl", ["ma.", "di.", "wo.", "do.", "vr.", "za.", "zo."])

for lang in ("da", "nb"):
    WAVE20_CASES += _wd_cases(
        lang, ["man", "tir", "ons", "tor", "fre", "lør", "søn"])
WAVE20_CASES += _wd_cases(
    "sv_se", ["mån", "tis", "ons", "tors", "fre", "lör", "sön"])
WAVE20_CASES += _wd_cases("fi", ["ma", "ti", "ke", "to", "pe", "la", "su"])

WAVE20_CASES += _wd_cases("hu", ["h", "k", "sze", "cs", "p", "szo", "v"])
WAVE20_CASES += [
    ("hu", "H", dt(2026, 9, 14)),
    ("hu", "CS", dt(2026, 9, 17)),
    ("hu", "V", dt(2026, 9, 20)),
] + _month_cases(
    "hu",
    [("jan.", 1), ("febr.", 2), ("márc.", 3), ("ápr.", 4), ("máj.", 5),
     ("jún.", 6), ("júl.", 7), ("aug.", 8), ("szept.", 9), ("okt.", 10),
     ("nov.", 11), ("dec.", 12)],
)

WAVE20_CASES += _wd_cases(
    "pl", ["pon", "wt", "śr", "czw", "pt", "sob", "niedz"])
WAVE20_CASES += _wd_cases(
    "pl", ["pon.", "wt.", "śr.", "czw.", "pt.", "sob.", "niedz."])
WAVE20_CASES += _month_cases(
    "pl",
    [("sty", 1), ("lut", 2), ("mar", 3), ("kwi", 4), ("maj", 5),
     ("cze", 6), ("lip", 7), ("sie", 8), ("wrz", 9), ("paź", 10),
     ("lis", 11), ("gru", 12)],
)

WAVE20_CASES += _wd_cases(
    "el", ["Δευ", "Τρι", "Τετ", "Πεμ", "Παρ", "Σαβ", "Κυρ"])
WAVE20_CASES += _month_cases(
    "el",
    [("Ιαν", 1), ("Φεβ", 2), ("Μαρ", 3), ("Απρ", 4), ("Μαΐ", 5),
     ("Ιουν", 6), ("Ιουλ", 7), ("Αυγ", 8), ("Σεπτ", 9), ("Οκτ", 10),
     ("Νοε", 11), ("Δεκ", 12)],
)

WAVE20_CASES += _wd_cases("bg", ["пн", "вт", "ср", "чт", "пт", "сб", "нд"])
WAVE20_CASES += [
    ("bg", "ПТ", dt(2026, 9, 18)),
] + _month_cases(
    "bg",
    [("януари", 1), ("март", 3), ("юни", 6), ("декември", 12)],
)

WAVE20_CASES += _wd_cases(
    "tr", ["Pzt", "Sal", "Çar", "Per", "Cum", "Cmt", "Paz"])
WAVE20_CASES += _wd_cases(
    "tr", ["pzt", "sal", "çar", "per", "cum", "cmt", "paz"])
WAVE20_CASES += [
    ("tr", "PZT", dt(2026, 9, 14)),
    ("tr", "CMT", dt(2026, 9, 19)),
] + _month_cases(
    "tr",
    [("Oca", 1), ("Şub", 2), ("Mar", 3), ("Nis", 4), ("May", 5),
     ("Haz", 6), ("Tem", 7), ("Ağu", 8), ("Eyl", 9), ("Eki", 10),
     ("Kas", 11), ("Ara", 12)],
)

WAVE20_CASES += _wd_cases(
    "ro", ["lun", "mar", "mie", "joi", "vin", "sâm", "dum"])
WAVE20_CASES += _wd_cases(
    "ro", ["lun.", "mar.", "mie.", "joi.", "vin.", "sâm.", "dum."])
WAVE20_CASES += _month_cases(
    "ro",
    [("ian", 1), ("feb", 2), ("mar", 3), ("apr", 4), ("mai", 5),
     ("iun", 6), ("iul", 7), ("aug", 8), ("sept", 9), ("oct", 10),
     ("nov", 11), ("dec", 12)],
)

WAVE20_CASES += _month_cases(
    "cs",
    [("led", 1), ("úno", 2), ("bře", 3), ("dub", 4), ("kvě", 5),
     ("čvn", 6), ("čvc", 7), ("srp", 8), ("zář", 9), ("říj", 10),
     ("lis", 11), ("pro", 12)],
    dotted_day=True,
)
WAVE20_CASES += _month_cases(
    "sk",
    [("jan", 1), ("feb", 2), ("mar", 3), ("apr", 4), ("máj", 5),
     ("jún", 6), ("júl", 7), ("aug", 8), ("sep", 9), ("okt", 10),
     ("nov", 11), ("dec", 12)],
    dotted_day=True,
)
WAVE20_CASES += _month_cases(
    "uk",
    [("січ", 1), ("лют", 2), ("бер", 3), ("квіт", 4), ("трав", 5),
     ("черв", 6), ("лип", 7), ("серп", 8), ("вер", 9), ("жовт", 10),
     ("лист", 11), ("груд", 12)],
)
WAVE20_CASES += [
    ("uk", "СІЧ 5, 2023", dt(2023, 1, 5)),
    ("uk", "трав 5, 2023", dt(2023, 5, 5)),
]

# Ambiguous weekday/month abbreviations resolved by surrounding date context.
WAVE20_CASES += [
    ("ro", "5 mart. 2023", dt(2023, 3, 5)),
    ("ro", "mar 5 mar 2023", dt(2023, 3, 5)),
    ("tr", "Paz 5 Ara 2023", dt(2023, 12, 5)),
    ("cs", "po 5. pros 2023", dt(2023, 12, 5)),
    ("hu", "sze 5. dec. 2023", dt(2023, 12, 5)),
    ("uk", "пн 5 квіт 2023", dt(2023, 4, 5)),
    ("el", "Δευ 5 Μαρ 2023", dt(2023, 3, 5)),
    ("bg", "пн 5 януари 2023", dt(2023, 1, 5)),
    ("de", "Mo 5. Sept. 2023", dt(2023, 9, 5)),
]


@pytest.mark.parametrize("lang,text,expected", WAVE20_CASES)
def test_wave20_global_scenarios(lang, text, expected):
    assert parse(text, langs=[lang], base_datetime=BASE) == expected
