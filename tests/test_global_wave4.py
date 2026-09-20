# -*- coding: utf-8 -*-

import datetime

import pytest

from gggdtparser import parse


dt = datetime.datetime
BASE = dt(2026, 9, 18, 15, 4, 5)

EXPECTED = {
    "today": dt(2026, 9, 18),
    "yesterday": dt(2026, 9, 17),
    "tomorrow": dt(2026, 9, 19),
    "day_before_yesterday": dt(2026, 9, 16),
    "day_after_tomorrow": dt(2026, 9, 20),
    "two_hours_later": dt(2026, 9, 18, 17, 0, 0),
    "two_hours_ago": dt(2026, 9, 18, 13, 0, 0),
    "two_minutes_later": dt(2026, 9, 18, 15, 6, 0),
    "two_minutes_ago": dt(2026, 9, 18, 15, 2, 0),
    "next_week": dt(2026, 9, 25),
    "last_week": dt(2026, 9, 11),
    "next_month": dt(2026, 10, 18),
    "last_month": dt(2026, 8, 18),
    "next_year": dt(2027, 1, 1),
    "last_year": dt(2025, 1, 1),
    "just_now": dt(2026, 9, 18, 15, 4, 0),
}

LANG_SCENARIOS = {
    "am": {
        "today": "ዛሬ",
        "yesterday": "ትናንት",
        "tomorrow": "ነገ",
        "day_before_yesterday": "ከትናንት በፊት",
        "day_after_tomorrow": "ከነገ በኋላ",
        "two_hours_later": "ከ2 ሰዓት በኋላ",
        "two_hours_ago": "ከ2 ሰዓት በፊት",
        "two_minutes_later": "ከ2 ደቂቃ በኋላ",
        "two_minutes_ago": "ከ2 ደቂቃ በፊት",
        "next_week": "በሚቀጥለው ሳምንት",
        "last_week": "ባለፈው ሳምንት",
        "next_month": "በሚቀጥለው ወር",
        "last_month": "ባለፈው ወር",
        "next_year": "በሚቀጥለው ዓመት",
        "last_year": "ባለፈው ዓመት",
        "just_now": "አሁን",
    },
    "ceb": {
        "today": "karon",
        "yesterday": "gahapon",
        "tomorrow": "ugma",
        "day_before_yesterday": "ang adlaw sa wala pa gahapon",
        "day_after_tomorrow": "ang adlaw pagkahuman sa ugma",
        "two_hours_later": "human sa 2 ka oras",
        "two_hours_ago": "2 ka oras ang milabay",
        "two_minutes_later": "human sa 2 ka minuto",
        "two_minutes_ago": "2 ka minuto ang milabay",
        "next_week": "sunod nga semana",
        "last_week": "miaging semana",
        "next_month": "sunod nga bulan",
        "last_month": "miaging bulan",
        "next_year": "sunod nga tuig",
        "last_year": "miaging tuig",
        "just_now": "bag-o lang",
    },
    "eo": {
        "today": "hodiaŭ",
        "yesterday": "hieraŭ",
        "tomorrow": "morgaŭ",
        "day_before_yesterday": "antaŭhieraŭ",
        "day_after_tomorrow": "postmorgaŭ",
        "two_hours_later": "post 2 horoj",
        "two_hours_ago": "antaŭ 2 horoj",
        "two_minutes_later": "post 2 minutoj",
        "two_minutes_ago": "antaŭ 2 minutoj",
        "next_week": "venonta semajno",
        "last_week": "pasinta semajno",
        "next_month": "venonta monato",
        "last_month": "pasinta monato",
        "next_year": "venonta jaro",
        "last_year": "pasinta jaro",
        "just_now": "ĵus",
    },
    "ha": {
        "today": "yau",
        "yesterday": "jiya",
        "tomorrow": "gobe",
        "day_before_yesterday": "kwana biyu da suka gabata",
        "day_after_tomorrow": "kwana biyu masu zuwa",
        "two_hours_later": "bayan awa biyu",
        "two_hours_ago": "awa biyu da suka wuce",
        "two_minutes_later": "bayan minti biyu",
        "two_minutes_ago": "minti biyu da suka wuce",
        "next_week": "mako mai zuwa",
        "last_week": "makon da ya gabata",
        "next_month": "wata mai zuwa",
        "last_month": "watan da ya gabata",
        "next_year": "shekara mai zuwa",
        "last_year": "shekarar da ta gabata",
        "just_now": "yanzu",
    },
    "ht": {
        "today": "jodi a",
        "yesterday": "yè",
        "tomorrow": "demen",
        "day_before_yesterday": "avantyè",
        "day_after_tomorrow": "apre demen",
        "two_hours_later": "nan 2 èdtan",
        "two_hours_ago": "sa gen 2 èdtan",
        "two_minutes_later": "nan 2 minit",
        "two_minutes_ago": "sa gen 2 minit",
        "next_week": "semèn pwochèn",
        "last_week": "semèn pase",
        "next_month": "mwa pwochèn",
        "last_month": "mwa pase",
        "next_year": "ane pwochèn",
        "last_year": "ane pase",
        "just_now": "fèk",
    },
    "ia": {
        "today": "hodie",
        "yesterday": "heri",
        "tomorrow": "deman",
        "day_before_yesterday": "heri ante",
        "day_after_tomorrow": "post deman",
        "two_hours_later": "post 2 horas",
        "two_hours_ago": "2 horas retro",
        "two_minutes_later": "post 2 minutas",
        "two_minutes_ago": "2 minutas retro",
        "next_week": "proxime septimana",
        "last_week": "septimana passate",
        "next_month": "proxime mense",
        "last_month": "mense passate",
        "next_year": "proxime anno",
        "last_year": "anno passate",
        "just_now": "justo nunc",
    },
    "jv": {
        "today": "dina iki",
        "yesterday": "wingi",
        "tomorrow": "sesuk",
        "day_before_yesterday": "2 dina kepungkur",
        "day_after_tomorrow": "2 dina maneh",
        "two_hours_later": "2 jam maneh",
        "two_hours_ago": "2 jam kepungkur",
        "two_minutes_later": "2 menit maneh",
        "two_minutes_ago": "2 menit kepungkur",
        "next_week": "minggu ngarep",
        "last_week": "minggu wingi",
        "next_month": "sasi ngarep",
        "last_month": "sasi wingi",
        "next_year": "taun ngarep",
        "last_year": "taun wingi",
        "just_now": "anyar wae",
    },
    "la": {
        "today": "hodie",
        "yesterday": "heri",
        "tomorrow": "cras",
        "day_before_yesterday": "ante heri",
        "day_after_tomorrow": "post cras",
        "two_hours_later": "post 2 horas",
        "two_hours_ago": "ante 2 horas",
        "two_minutes_later": "post 2 minutas",
        "two_minutes_ago": "ante 2 minutas",
        "next_week": "proxima septimana",
        "last_week": "praeterita septimana",
        "next_month": "proximo mense",
        "last_month": "praeterito mense",
        "next_year": "proximo anno",
        "last_year": "praeterito anno",
        "just_now": "modo",
    },
    "mg": {
        "today": "anio",
        "yesterday": "omaly",
        "tomorrow": "rahampitso",
        "day_before_yesterday": "2 andro lasa izay",
        "day_after_tomorrow": "2 andro avy eo",
        "two_hours_later": "afaka 2 ora",
        "two_hours_ago": "2 ora lasa izay",
        "two_minutes_later": "afaka 2 minitra",
        "two_minutes_ago": "2 minitra lasa izay",
        "next_week": "herinandro ho avy",
        "last_week": "herinandro lasa",
        "next_month": "volana ho avy",
        "last_month": "volana lasa",
        "next_year": "taona ho avy",
        "last_year": "taona lasa",
        "just_now": "izao vao",
    },
    "oc": {
        "today": "uèi",
        "yesterday": "ièr",
        "tomorrow": "deman",
        "day_before_yesterday": "abans ièr",
        "day_after_tomorrow": "aprèp deman",
        "two_hours_later": "dins 2 oras",
        "two_hours_ago": "fa 2 oras",
        "two_minutes_later": "dins 2 minutas",
        "two_minutes_ago": "fa 2 minutas",
        "next_week": "la setmana que ven",
        "last_week": "la setmana passada",
        "next_month": "lo mes que ven",
        "last_month": "lo mes passat",
        "next_year": "l'an que ven",
        "last_year": "l'an passat",
        "just_now": "ara meteis",
    },
    "tk": {
        "today": "şu gün",
        "yesterday": "düýn",
        "tomorrow": "ertir",
        "day_before_yesterday": "2 gün öň",
        "day_after_tomorrow": "2 gün soň",
        "two_hours_later": "2 sagatdan soň",
        "two_hours_ago": "2 sagat öň",
        "two_minutes_later": "2 minutdan soň",
        "two_minutes_ago": "2 minut öň",
        "next_week": "indiki hepde",
        "last_week": "geçen hepde",
        "next_month": "indiki aý",
        "last_month": "geçen aý",
        "next_year": "indiki ýyl",
        "last_year": "geçen ýyl",
        "just_now": "häzir",
    },
    "xh": {
        "today": "namhlanje",
        "yesterday": "izolo",
        "tomorrow": "ngomso",
        "day_before_yesterday": "2 iintsuku ezidlulileyo",
        "day_after_tomorrow": "2 iintsuku ezizayo",
        "two_hours_later": "2 iiyure ezizayo",
        "two_hours_ago": "2 iiyure ezidlulileyo",
        "two_minutes_later": "2 imizuzu ezizayo",
        "two_minutes_ago": "2 imizuzu ezidlulileyo",
        "next_week": "iveki ezayo",
        "last_week": "iveki ephelileyo",
        "next_month": "inyanga ezayo",
        "last_month": "inyanga ephelileyo",
        "next_year": "unyaka ozayo",
        "last_year": "unyaka ophelileyo",
        "just_now": "ngoku",
    },
    "zu": {
        "today": "namuhla",
        "yesterday": "izolo",
        "tomorrow": "kusasa",
        "day_before_yesterday": "2 izinsuku adlulile",
        "day_after_tomorrow": "2 izinsuku ezayo",
        "two_hours_later": "2 amahora ezayo",
        "two_hours_ago": "2 amahora adlulile",
        "two_minutes_later": "2 imizuzu ezayo",
        "two_minutes_ago": "2 imizuzu adlulile",
        "next_week": "isonto ezayo",
        "last_week": "isonto edlule",
        "next_month": "inyanga ezayo",
        "last_month": "inyanga edlule",
        "next_year": "unyaka ozayo",
        "last_year": "unyaka odlule",
        "just_now": "manje",
    },
}

LANG_MONTHS = {
    "am": [
        "ጃንዋሪ", "ፌብሩዋሪ", "ማርች", "ኤፕሪል", "ሜይ", "ጁን",
        "ጁላይ", "ኦገስት", "ሴፕቴምበር", "ኦክቶበር", "ኖቬምበር", "ዲሴምበር",
    ],
    "ceb": [
        "Enero", "Pebrero", "Marso", "Abril", "Mayo", "Hunyo",
        "Hulyo", "Agosto", "Septiyembre", "Oktubre", "Nobiyembre",
        "Disiyembre",
    ],
    "eo": [
        "Januaro", "Februaro", "Marto", "Aprilo", "Majo", "Junio",
        "Julio", "Aŭgusto", "Septembro", "Oktobro", "Novembro",
        "Decembro",
    ],
    "ha": [
        "Janairu", "Fabrairu", "Maris", "Afrilu", "Mayu", "Yuni",
        "Yuli", "Agusta", "Satumba", "Oktoba", "Nuwamba", "Disamba",
    ],
    "ht": [
        "janvye", "fevriye", "mas", "avril", "me", "jen",
        "jiyè", "out", "septanm", "oktòb", "novanm", "desanm",
    ],
    "ia": [
        "januario", "februario", "martio", "april", "maio", "junio",
        "julio", "augusto", "septembre", "octobre", "novembre",
        "decembre",
    ],
    "jv": [
        "Januari", "Februari", "Maret", "April", "Mei", "Juni",
        "Juli", "Agustus", "September", "Oktober", "Nopember",
        "Desember",
    ],
    "la": [
        "Ianuarius", "Februarius", "Martius", "Aprilis", "Maius",
        "Iunius", "Iulius", "Augustus", "September", "October",
        "November", "December",
    ],
    "mg": [
        "Janoary", "Febroary", "Martsa", "Aprily", "Mey", "Jona",
        "Jolay", "Aogositra", "Septambra", "Oktobra", "Novambra",
        "Desambra",
    ],
    "oc": [
        "genièr", "febrièr", "març", "abril", "mai", "junh",
        "julhet", "agost", "setembre", "octobre", "novembre",
        "decembre",
    ],
    "tk": [
        "ýanwar", "fewral", "mart", "aprel", "maý", "iýun",
        "iýul", "awgust", "sentýabr", "oktýabr", "noýabr", "dekabr",
    ],
    "xh": [
        "uJanuwari", "uFebruwari", "uMatshi", "uAprili", "uMeyi",
        "uJuni", "uJulayi", "uAgasti", "uSeptemba", "uOktobha",
        "uNovemba", "uDisemba",
    ],
    "zu": [
        "uJanuwari", "uFebruwari", "uMashi", "u-Ephreli", "uMeyi",
        "uJuni", "uJulayi", "uAgasti", "uSepthemba", "u-Okthoba",
        "uNovemba", "uDisemba",
    ],
}


def _iter_cases():
    for lang, scenarios in sorted(LANG_SCENARIOS.items()):
        for key, text in scenarios.items():
            yield lang, key, text, EXPECTED[key]


def _iter_months():
    for lang, months in sorted(LANG_MONTHS.items()):
        for index, month in enumerate(months, start=1):
            yield lang, "5 %s 2022" % month, dt(2022, index, 5)


def _iter_month_years():
    for lang, months in sorted(LANG_MONTHS.items()):
        yield lang, "%s 2022" % months[0], dt(2022, 1, 1)


@pytest.mark.parametrize(
    "lang,key,text,expected",
    list(_iter_cases()),
)
def test_wave4_natural_language_scenarios(lang, key, text, expected):
    assert parse(text, langs=[lang], base_datetime=BASE) == expected


@pytest.mark.parametrize(
    "lang,text,expected",
    list(_iter_months()),
)
def test_wave4_month_names(lang, text, expected):
    assert parse(text, langs=[lang]) == expected


@pytest.mark.parametrize(
    "lang,text,expected",
    list(_iter_month_years()),
)
def test_wave4_month_year(lang, text, expected):
    assert parse(text, langs=[lang]) == expected


@pytest.mark.parametrize(
    "lang,text,expected",
    [
        ("am-ET", "ነገ", EXPECTED["tomorrow"]),
        ("ceb-PH", "ugma", EXPECTED["tomorrow"]),
        ("eo-XX", "morgaŭ", EXPECTED["tomorrow"]),
        ("epo", "morgaŭ", EXPECTED["tomorrow"]),
        ("ha-NG", "gobe", EXPECTED["tomorrow"]),
        ("ht-HT", "demen", EXPECTED["tomorrow"]),
        ("ia-XX", "deman", EXPECTED["tomorrow"]),
        ("jv-ID", "sesuk", EXPECTED["tomorrow"]),
        ("la-XX", "cras", EXPECTED["tomorrow"]),
        ("mg-MG", "rahampitso", EXPECTED["tomorrow"]),
        ("oc-FR", "deman", EXPECTED["tomorrow"]),
        ("tk-TM", "ertir", EXPECTED["tomorrow"]),
        ("xh-ZA", "ngomso", EXPECTED["tomorrow"]),
        ("zu-ZA", "kusasa", EXPECTED["tomorrow"]),
    ],
)
def test_wave4_bcp47_language_aliases(lang, text, expected):
    assert parse(text, langs=[lang], base_datetime=BASE) == expected
