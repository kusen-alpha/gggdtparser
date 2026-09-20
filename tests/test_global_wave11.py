# -*- coding: utf-8 -*-

import datetime

import pytest

from gggdtparser import parse


dt = datetime.datetime
BASE = dt(2026, 9, 18, 15, 4, 5)


WAVE11_CASES = [
    # Icelandic
    ("is", "næsti mánudagur", dt(2026, 9, 21)),
    ("is", "næsti laugardagur", dt(2026, 9, 26)),
    ("is", "næsta sunnudag", dt(2026, 9, 27)),
    ("is", "síðasti föstudagur", dt(2026, 9, 11)),
    ("is", "síðasti laugardagur", dt(2026, 9, 12)),
    ("is", "síðasti sunnudagur", dt(2026, 9, 13)),
    ("is", "þessi mánudagur", dt(2026, 9, 14)),
    ("is", "í morgun", dt(2026, 9, 18, 8, 0)),
    ("is", "eftir hádegi", dt(2026, 9, 18, 15, 0)),
    ("is", "í kvöld", dt(2026, 9, 18, 20, 0)),
    ("is", "í nótt", dt(2026, 9, 18, 22, 0)),
    ("is", "í fyrramálið", dt(2026, 9, 19, 8, 0)),
    ("is", "í gærkvöldi", dt(2026, 9, 17, 20, 0)),
    ("is", "hádegi", dt(2026, 9, 18, 12, 0)),
    ("is", "miðnætti", dt(2026, 9, 18, 0, 0)),
    # Estonian
    ("et", "järgmine esmaspäev", dt(2026, 9, 21)),
    ("et", "järgmisel laupäeval", dt(2026, 9, 26)),
    ("et", "tuleval pühapäeval", dt(2026, 9, 27)),
    ("et", "eelmine reede", dt(2026, 9, 11)),
    ("et", "eelmisel laupäeval", dt(2026, 9, 12)),
    ("et", "eelmine pühapäev", dt(2026, 9, 13)),
    ("et", "sel esmaspäeval", dt(2026, 9, 14)),
    ("et", "täna hommikul", dt(2026, 9, 18, 8, 0)),
    ("et", "täna pärastlõunal", dt(2026, 9, 18, 15, 0)),
    ("et", "täna õhtul", dt(2026, 9, 18, 20, 0)),
    ("et", "homme hommikul", dt(2026, 9, 19, 8, 0)),
    ("et", "eile õhtul", dt(2026, 9, 17, 20, 0)),
    ("et", "keskpäeval", dt(2026, 9, 18, 12, 0)),
    ("et", "keskööl", dt(2026, 9, 18, 0, 0)),
    # Latvian
    ("lv", "nākamā pirmdiena", dt(2026, 9, 21)),
    ("lv", "nākamajā sestdienā", dt(2026, 9, 26)),
    ("lv", "nākošā svētdiena", dt(2026, 9, 27)),
    ("lv", "pagājušā piektdiena", dt(2026, 9, 11)),
    ("lv", "pagājušajā sestdienā", dt(2026, 9, 12)),
    ("lv", "pagājušā svētdiena", dt(2026, 9, 13)),
    ("lv", "šī pirmdiena", dt(2026, 9, 14)),
    ("lv", "šorīt", dt(2026, 9, 18, 8, 0)),
    ("lv", "šodien pēcpusdienā", dt(2026, 9, 18, 15, 0)),
    ("lv", "šovakar", dt(2026, 9, 18, 20, 0)),
    ("lv", "rīt no rīta", dt(2026, 9, 19, 8, 0)),
    ("lv", "vakar vakarā", dt(2026, 9, 17, 20, 0)),
    ("lv", "pusdienlaikā", dt(2026, 9, 18, 12, 0)),
    ("lv", "pusnaktī", dt(2026, 9, 18, 0, 0)),
    # Slovenian
    ("sl", "naslednji ponedeljek", dt(2026, 9, 21)),
    ("sl", "naslednja sobota", dt(2026, 9, 26)),
    ("sl", "naslednja nedelja", dt(2026, 9, 27)),
    ("sl", "prejšnji petek", dt(2026, 9, 11)),
    ("sl", "prejšnja sobota", dt(2026, 9, 12)),
    ("sl", "prejšnja nedelja", dt(2026, 9, 13)),
    ("sl", "ta ponedeljek", dt(2026, 9, 14)),
    ("sl", "danes zjutraj", dt(2026, 9, 18, 8, 0)),
    ("sl", "danes popoldne", dt(2026, 9, 18, 15, 0)),
    ("sl", "danes zvečer", dt(2026, 9, 18, 20, 0)),
    ("sl", "jutri zjutraj", dt(2026, 9, 19, 8, 0)),
    ("sl", "včeraj zvečer", dt(2026, 9, 17, 20, 0)),
    ("sl", "opoldne", dt(2026, 9, 18, 12, 0)),
    ("sl", "polnoči", dt(2026, 9, 18, 0, 0)),
    # Bosnian
    ("bs", "sljedeći ponedjeljak", dt(2026, 9, 21)),
    ("bs", "sljedeća subota", dt(2026, 9, 26)),
    ("bs", "sljedeća nedjelja", dt(2026, 9, 27)),
    ("bs", "prošli petak", dt(2026, 9, 11)),
    ("bs", "prošla subota", dt(2026, 9, 12)),
    ("bs", "prošla nedjelja", dt(2026, 9, 13)),
    ("bs", "ova subota", dt(2026, 9, 19)),
    ("bs", "danas ujutro", dt(2026, 9, 18, 8, 0)),
    ("bs", "danas popodne", dt(2026, 9, 18, 15, 0)),
    ("bs", "danas navečer", dt(2026, 9, 18, 20, 0)),
    ("bs", "sutra ujutro", dt(2026, 9, 19, 8, 0)),
    ("bs", "jučer navečer", dt(2026, 9, 17, 20, 0)),
    ("bs", "u podne", dt(2026, 9, 18, 12, 0)),
    ("bs", "ponoć", dt(2026, 9, 18, 0, 0)),
    # Turkmen
    ("tk", "indiki duşenbe", dt(2026, 9, 21)),
    ("tk", "indiki şenbe", dt(2026, 9, 26)),
    ("tk", "indiki ýekşenbe", dt(2026, 9, 27)),
    ("tk", "geçen anna", dt(2026, 9, 11)),
    ("tk", "geçen şenbe", dt(2026, 9, 12)),
    ("tk", "geçen ýekşenbe", dt(2026, 9, 13)),
    ("tk", "şu duşenbe", dt(2026, 9, 14)),
    ("tk", "şu gün irden", dt(2026, 9, 18, 8, 0)),
    ("tk", "şu gün öýlän", dt(2026, 9, 18, 12, 0)),
    ("tk", "şu gün günortandan soň", dt(2026, 9, 18, 15, 0)),
    ("tk", "şu gün agşam", dt(2026, 9, 18, 20, 0)),
    ("tk", "ertir irden", dt(2026, 9, 19, 8, 0)),
    ("tk", "düýn agşam", dt(2026, 9, 17, 20, 0)),
    ("tk", "gijäniň ýarynda", dt(2026, 9, 18, 0, 0)),
]


@pytest.mark.parametrize("lang,text,expected", WAVE11_CASES)
def test_wave11_global_scenarios(lang, text, expected):
    assert parse(text, langs=[lang], base_datetime=BASE) == expected
