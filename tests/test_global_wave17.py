# -*- coding: utf-8 -*-

import datetime

import pytest

from gggdtparser import parse


dt = datetime.datetime
BASE = dt(2026, 9, 18, 15, 4, 5)


WAVE17_CASES = [
    # Afrikaans bare weekdays
    ("af", "maandag", dt(2026, 9, 14)),
    ("af", "dinsdag", dt(2026, 9, 15)),
    ("af", "woensdag", dt(2026, 9, 16)),
    ("af", "donderdag", dt(2026, 9, 17)),
    ("af", "vrydag", dt(2026, 9, 18)),
    ("af", "saterdag", dt(2026, 9, 19)),
    ("af", "sondag", dt(2026, 9, 20)),
    # Basque short weekday forms
    ("eu", "astelehen", dt(2026, 9, 14)),
    ("eu", "astearte", dt(2026, 9, 15)),
    ("eu", "asteazken", dt(2026, 9, 16)),
    ("eu", "ostegun", dt(2026, 9, 17)),
    ("eu", "ostiral", dt(2026, 9, 18)),
    ("eu", "larunbat", dt(2026, 9, 19)),
    ("eu", "igande", dt(2026, 9, 20)),
    # Welsh: dydd Mawrth is Tuesday, bare mawrth stays March
    ("cy", "dydd Mawrth", dt(2026, 9, 15)),
    ("cy", "dydd mawrth", dt(2026, 9, 15)),
    ("cy", "Mawrth", dt(2026, 3, 1)),
    # Persian: یکشنبه must stay Sunday, not Saturday
    ("fa", "یکشنبه", dt(2026, 9, 20)),
    ("fa", "یکشنبه بعد", dt(2026, 9, 27)),
    # Khmer weekday variants ending in subscript marks
    ("km", "អង្គាក់", dt(2026, 9, 15)),
    ("km", "ព្រហស្បតិ៍", dt(2026, 9, 17)),
    ("km", "ព្រហស្បតិ៏", dt(2026, 9, 17)),
    ("km", "សៅរ៍", dt(2026, 9, 19)),
    # Somali definite weekdays
    ("so", "Isniinta", dt(2026, 9, 14)),
    ("so", "Talaadada", dt(2026, 9, 15)),
    ("so", "Arbacada", dt(2026, 9, 16)),
    ("so", "Khamiista", dt(2026, 9, 17)),
    ("so", "Jimcaha", dt(2026, 9, 18)),
    ("so", "Sabtida", dt(2026, 9, 19)),
    ("so", "Axadda", dt(2026, 9, 20)),
    # Somali past weekdays
    ("so", "Isniintii", dt(2026, 9, 14)),
    ("so", "Talaadadii", dt(2026, 9, 15)),
    ("so", "Arbacidii", dt(2026, 9, 16)),
    ("so", "Khamiistii", dt(2026, 9, 17)),
    ("so", "Jimcihii", dt(2026, 9, 18)),
    ("so", "Sabtidii", dt(2026, 9, 19)),
    ("so", "Axaddii", dt(2026, 9, 20)),
    # Indonesian bare minggu plus phrase priority
    ("_id", "minggu", dt(2026, 9, 20)),
    ("_id", "Minggu", dt(2026, 9, 20)),
    ("_id", "minggu ini", dt(2026, 9, 20)),
    ("_id", "Minggu ini", dt(2026, 9, 20)),
    ("_id", "hari minggu ini", dt(2026, 9, 20)),
    ("_id", "minggu depan", dt(2026, 9, 25)),
    ("_id", "minggu lalu", dt(2026, 9, 11)),
]


@pytest.mark.parametrize("lang,text,expected", WAVE17_CASES)
def test_wave17_global_scenarios(lang, text, expected):
    assert parse(text, langs=[lang], base_datetime=BASE) == expected
