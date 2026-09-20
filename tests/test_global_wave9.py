# -*- coding: utf-8 -*-

import datetime

import pytest

from gggdtparser import parse


dt = datetime.datetime
BASE = dt(2026, 9, 18, 15, 4, 5)


WAVE9_CASES = [
    # Slovak
    ("sk", "budúci pondelok", dt(2026, 9, 21)),
    ("sk", "budúca sobota", dt(2026, 9, 26)),
    ("sk", "budúca nedeľa", dt(2026, 9, 27)),
    ("sk", "minulý piatok", dt(2026, 9, 11)),
    ("sk", "minulá sobota", dt(2026, 9, 12)),
    ("sk", "minulá nedeľa", dt(2026, 9, 13)),
    ("sk", "tento pondelok", dt(2026, 9, 14)),
    ("sk", "dnes ráno", dt(2026, 9, 18, 8, 0)),
    ("sk", "dnes večer", dt(2026, 9, 18, 20, 0)),
    ("sk", "zajtra ráno", dt(2026, 9, 19, 8, 0)),
    ("sk", "zajtra večer", dt(2026, 9, 19, 20, 0)),
    ("sk", "včera večer", dt(2026, 9, 17, 20, 0)),
    ("sk", "napoludnie", dt(2026, 9, 18, 12, 0)),
    ("sk", "o polnoci", dt(2026, 9, 18, 0, 0)),
    # Croatian
    ("hr", "sljedeći ponedjeljak", dt(2026, 9, 21)),
    ("hr", "sljedeća subota", dt(2026, 9, 26)),
    ("hr", "sljedeća nedjelja", dt(2026, 9, 27)),
    ("hr", "idući petak", dt(2026, 9, 25)),
    ("hr", "prošli petak", dt(2026, 9, 11)),
    ("hr", "prošla subota", dt(2026, 9, 12)),
    ("hr", "prošla nedjelja", dt(2026, 9, 13)),
    ("hr", "ova subota", dt(2026, 9, 19)),
    ("hr", "danas ujutro", dt(2026, 9, 18, 8, 0)),
    ("hr", "jutros", dt(2026, 9, 18, 8, 0)),
    ("hr", "danas popodne", dt(2026, 9, 18, 15, 0)),
    ("hr", "danas navečer", dt(2026, 9, 18, 20, 0)),
    ("hr", "sutra ujutro", dt(2026, 9, 19, 8, 0)),
    ("hr", "jučer navečer", dt(2026, 9, 17, 20, 0)),
    ("hr", "u podne", dt(2026, 9, 18, 12, 0)),
    ("hr", "ponoć", dt(2026, 9, 18, 0, 0)),
    # Serbian (Cyrillic)
    ("sr", "следећи понедељак", dt(2026, 9, 21)),
    ("sr", "следећа субота", dt(2026, 9, 26)),
    ("sr", "следећа недеља", dt(2026, 9, 27)),
    ("sr", "прошли петак", dt(2026, 9, 11)),
    ("sr", "прошла субота", dt(2026, 9, 12)),
    ("sr", "прошла недеља", dt(2026, 9, 13)),
    ("sr", "овај понедељак", dt(2026, 9, 14)),
    ("sr", "данас ујутру", dt(2026, 9, 18, 8, 0)),
    ("sr", "данас поподне", dt(2026, 9, 18, 15, 0)),
    ("sr", "данас увече", dt(2026, 9, 18, 20, 0)),
    ("sr", "сутра ујутро", dt(2026, 9, 19, 8, 0)),
    ("sr", "јуче увече", dt(2026, 9, 17, 20, 0)),
    ("sr", "у подне", dt(2026, 9, 18, 12, 0)),
    ("sr", "поноћ", dt(2026, 9, 18, 0, 0)),
    # Bulgarian
    ("bg", "следващия понеделник", dt(2026, 9, 21)),
    ("bg", "следващата събота", dt(2026, 9, 26)),
    ("bg", "следващата неделя", dt(2026, 9, 27)),
    ("bg", "миналия петък", dt(2026, 9, 11)),
    ("bg", "миналата събота", dt(2026, 9, 12)),
    ("bg", "миналата неделя", dt(2026, 9, 13)),
    ("bg", "тази събота", dt(2026, 9, 19)),
    ("bg", "тази сутрин", dt(2026, 9, 18, 8, 0)),
    ("bg", "днес следобед", dt(2026, 9, 18, 15, 0)),
    ("bg", "днес вечерта", dt(2026, 9, 18, 20, 0)),
    ("bg", "утре сутринта", dt(2026, 9, 19, 8, 0)),
    ("bg", "вчера вечерта", dt(2026, 9, 17, 20, 0)),
    ("bg", "на обяд", dt(2026, 9, 18, 12, 0)),
    ("bg", "полунощ", dt(2026, 9, 18, 0, 0)),
    # Catalan
    ("ca", "el dilluns que ve", dt(2026, 9, 21)),
    ("ca", "dissabte que ve", dt(2026, 9, 26)),
    ("ca", "el diumenge que ve", dt(2026, 9, 27)),
    ("ca", "el divendres passat", dt(2026, 9, 11)),
    ("ca", "dissabte passat", dt(2026, 9, 12)),
    ("ca", "diumenge passat", dt(2026, 9, 13)),
    ("ca", "aquest dilluns", dt(2026, 9, 14)),
    ("ca", "aquest dissabte", dt(2026, 9, 19)),
    ("ca", "aquest matí", dt(2026, 9, 18, 8, 0)),
    ("ca", "aquesta tarda", dt(2026, 9, 18, 15, 0)),
    ("ca", "aquest vespre", dt(2026, 9, 18, 20, 0)),
    ("ca", "aquesta nit", dt(2026, 9, 18, 22, 0)),
    ("ca", "demà al matí", dt(2026, 9, 19, 8, 0)),
    ("ca", "ahir a la nit", dt(2026, 9, 17, 22, 0)),
    ("ca", "al migdia", dt(2026, 9, 18, 12, 0)),
    ("ca", "mitjanit", dt(2026, 9, 18, 0, 0)),
    # Lithuanian
    ("lt", "kitą pirmadienį", dt(2026, 9, 21)),
    ("lt", "kitą šeštadienį", dt(2026, 9, 26)),
    ("lt", "kitą sekmadienį", dt(2026, 9, 27)),
    ("lt", "praėjusį penktadienį", dt(2026, 9, 11)),
    ("lt", "praėjusį šeštadienį", dt(2026, 9, 12)),
    ("lt", "praėjusį sekmadienį", dt(2026, 9, 13)),
    ("lt", "šį pirmadienį", dt(2026, 9, 14)),
    ("lt", "šį šeštadienį", dt(2026, 9, 19)),
    ("lt", "šį rytą", dt(2026, 9, 18, 8, 0)),
    ("lt", "šiandien vakare", dt(2026, 9, 18, 20, 0)),
    ("lt", "rytoj rytą", dt(2026, 9, 19, 8, 0)),
    ("lt", "vakar vakare", dt(2026, 9, 17, 20, 0)),
    ("lt", "per pietus", dt(2026, 9, 18, 12, 0)),
    ("lt", "vidurnaktį", dt(2026, 9, 18, 0, 0)),
    # Japanese eras and this-week days
    ("ja", "明治3年", dt(1870, 1, 1)),
    ("ja", "明治45年", dt(1912, 1, 1)),
    ("ja", "大正10年", dt(1921, 1, 1)),
    ("ja", "今週の月曜日", dt(2026, 9, 14)),
    ("ja", "今週の土曜日", dt(2026, 9, 19)),
    # Lao Buddhist calendar years
    ("lo", "15 ກຸມພາ 2569", dt(2026, 2, 15)),
    ("lo", "20 ກໍລະກົດ 2569", dt(2026, 7, 20)),
    ("lo", "໒໕໖໙/໐໒/໐໒", dt(2026, 2, 2)),
    ("lo", "5 ກຸມພາ 2022", dt(2022, 2, 5)),
    # Khmer Buddhist calendar years
    ("km", "15 កុម្ភៈ 2569", dt(2026, 2, 15)),
    ("km", "20 កក្កដា 2569", dt(2026, 7, 20)),
    ("km", "២៥៦៩/០២/០២", dt(2026, 2, 2)),
    ("km", "5 កុម្ភៈ 2022", dt(2022, 2, 5)),
]


@pytest.mark.parametrize("lang,text,expected", WAVE9_CASES)
def test_wave9_global_scenarios(lang, text, expected):
    assert parse(text, langs=[lang], base_datetime=BASE) == expected
