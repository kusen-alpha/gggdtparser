# -*- coding: utf-8 -*-

import datetime

import pytest

from gggdtparser import parse


dt = datetime.datetime
BASE = dt(2026, 9, 18, 15, 4, 5)


WAVE10_CASES = [
    # Filipino
    ("fil", "susunod na Lunes", dt(2026, 9, 21)),
    ("fil", "darating na Sabado", dt(2026, 9, 26)),
    ("fil", "nakaraang Biyernes", dt(2026, 9, 11)),
    ("fil", "nakaraang Sabado", dt(2026, 9, 12)),
    ("fil", "ngayong Lunes", dt(2026, 9, 14)),
    ("fil", "ngayong Sabado", dt(2026, 9, 19)),
    ("fil", "ngayong umaga", dt(2026, 9, 18, 8, 0)),
    ("fil", "kaninang umaga", dt(2026, 9, 18, 8, 0)),
    ("fil", "ngayong hapon", dt(2026, 9, 18, 15, 0)),
    ("fil", "ngayong gabi", dt(2026, 9, 18, 20, 0)),
    ("fil", "mamayang gabi", dt(2026, 9, 18, 22, 0)),
    ("fil", "bukas ng umaga", dt(2026, 9, 19, 8, 0)),
    ("fil", "kagabi", dt(2026, 9, 17, 22, 0)),
    ("fil", "tanghali", dt(2026, 9, 18, 12, 0)),
    ("fil", "hatinggabi", dt(2026, 9, 18, 0, 0)),
    # Swahili
    ("sw", "Jumatatu ijayo", dt(2026, 9, 21)),
    ("sw", "Jumamosi ijayo", dt(2026, 9, 26)),
    ("sw", "Jumapili ijayo", dt(2026, 9, 27)),
    ("sw", "Ijumaa iliyopita", dt(2026, 9, 11)),
    ("sw", "Jumamosi iliyopita", dt(2026, 9, 12)),
    ("sw", "Jumapili iliyopita", dt(2026, 9, 13)),
    ("sw", "Jumatatu hii", dt(2026, 9, 14)),
    ("sw", "asubuhi hii", dt(2026, 9, 18, 8, 0)),
    ("sw", "mchana huu", dt(2026, 9, 18, 15, 0)),
    ("sw", "jioni hii", dt(2026, 9, 18, 20, 0)),
    ("sw", "kesho asubuhi", dt(2026, 9, 19, 8, 0)),
    ("sw", "jana jioni", dt(2026, 9, 17, 20, 0)),
    ("sw", "adhuhuri", dt(2026, 9, 18, 12, 0)),
    ("sw", "usiku wa manane", dt(2026, 9, 18, 0, 0)),
    # Uzbek
    ("uz", "kelasi dushanba", dt(2026, 9, 21)),
    ("uz", "kelasi shanba", dt(2026, 9, 26)),
    ("uz", "kelasi yakshanba", dt(2026, 9, 27)),
    ("uz", "o'tgan juma", dt(2026, 9, 11)),
    ("uz", "o'tgan shanba", dt(2026, 9, 12)),
    ("uz", "o'tgan yakshanba", dt(2026, 9, 13)),
    ("uz", "shu dushanba", dt(2026, 9, 14)),
    ("uz", "bugun ertalab", dt(2026, 9, 18, 8, 0)),
    ("uz", "bugun tushda", dt(2026, 9, 18, 12, 0)),
    ("uz", "bugun tushdan keyin", dt(2026, 9, 18, 15, 0)),
    ("uz", "bugun kechqurun", dt(2026, 9, 18, 20, 0)),
    ("uz", "ertaga ertalab", dt(2026, 9, 19, 8, 0)),
    ("uz", "kecha kechqurun", dt(2026, 9, 17, 20, 0)),
    ("uz", "yarim tun", dt(2026, 9, 18, 0, 0)),
    # Afrikaans
    ("af", "volgende Maandag", dt(2026, 9, 21)),
    ("af", "volgende Saterdag", dt(2026, 9, 26)),
    ("af", "volgende Sondag", dt(2026, 9, 27)),
    ("af", "verlede Vrydag", dt(2026, 9, 11)),
    ("af", "verlede Saterdag", dt(2026, 9, 12)),
    ("af", "verlede Sondag", dt(2026, 9, 13)),
    ("af", "hierdie Maandag", dt(2026, 9, 14)),
    ("af", "vanoggend", dt(2026, 9, 18, 8, 0)),
    ("af", "vanmiddag", dt(2026, 9, 18, 15, 0)),
    ("af", "vanaand", dt(2026, 9, 18, 20, 0)),
    ("af", "môre oggend", dt(2026, 9, 19, 8, 0)),
    ("af", "gisteraand", dt(2026, 9, 17, 20, 0)),
    ("af", "middag", dt(2026, 9, 18, 12, 0)),
    ("af", "middernag", dt(2026, 9, 18, 0, 0)),
]


@pytest.mark.parametrize("lang,text,expected", WAVE10_CASES)
def test_wave10_global_scenarios(lang, text, expected):
    assert parse(text, langs=[lang], base_datetime=BASE) == expected
