# -*- coding: utf-8 -*-

import datetime

import pytest

from gggdtparser import parse


dt = datetime.datetime
BASE = dt(2026, 9, 18, 15, 4, 5)


WAVE7_CASES = [
    # Swedish
    ("sv_se", "nästa måndag", dt(2026, 9, 21)),
    ("sv_se", "kommande lördag", dt(2026, 9, 26)),
    ("sv_se", "nästa söndag", dt(2026, 9, 27)),
    ("sv_se", "förra fredag", dt(2026, 9, 11)),
    ("sv_se", "förra lördag", dt(2026, 9, 12)),
    ("sv_se", "förra söndag", dt(2026, 9, 13)),
    ("sv_se", "denna måndag", dt(2026, 9, 14)),
    ("sv_se", "i morse", dt(2026, 9, 18, 8, 0)),
    ("sv_se", "i eftermiddags", dt(2026, 9, 18, 15, 0)),
    ("sv_se", "ikväll", dt(2026, 9, 18, 20, 0)),
    ("sv_se", "inatt", dt(2026, 9, 18, 22, 0)),
    ("sv_se", "imorgon bitti", dt(2026, 9, 19, 8, 0)),
    ("sv_se", "imorgon kväll", dt(2026, 9, 19, 20, 0)),
    ("sv_se", "igår kväll", dt(2026, 9, 17, 20, 0)),
    ("sv_se", "vid lunch", dt(2026, 9, 18, 12, 0)),
    ("sv_se", "midnatt", dt(2026, 9, 18, 0, 0)),
    # Danish
    ("da", "næste mandag", dt(2026, 9, 21)),
    ("da", "kommende lørdag", dt(2026, 9, 26)),
    ("da", "næste søndag", dt(2026, 9, 27)),
    ("da", "sidste fredag", dt(2026, 9, 11)),
    ("da", "sidste lørdag", dt(2026, 9, 12)),
    ("da", "sidste søndag", dt(2026, 9, 13)),
    ("da", "denne mandag", dt(2026, 9, 14)),
    ("da", "i morges", dt(2026, 9, 18, 8, 0)),
    ("da", "i eftermiddags", dt(2026, 9, 18, 15, 0)),
    ("da", "i aften", dt(2026, 9, 18, 20, 0)),
    ("da", "i nat", dt(2026, 9, 18, 22, 0)),
    ("da", "i morgen tidlig", dt(2026, 9, 19, 8, 0)),
    ("da", "i morgen aften", dt(2026, 9, 19, 20, 0)),
    ("da", "i går aftes", dt(2026, 9, 17, 20, 0)),
    ("da", "ved middagstid", dt(2026, 9, 18, 12, 0)),
    ("da", "midnat", dt(2026, 9, 18, 0, 0)),
    # Norwegian
    ("nb", "neste mandag", dt(2026, 9, 21)),
    ("nb", "kommende lørdag", dt(2026, 9, 26)),
    ("nb", "neste søndag", dt(2026, 9, 27)),
    ("nb", "forrige fredag", dt(2026, 9, 11)),
    ("nb", "forrige lørdag", dt(2026, 9, 12)),
    ("nb", "forrige søndag", dt(2026, 9, 13)),
    ("nb", "denne mandag", dt(2026, 9, 14)),
    ("nb", "i morges", dt(2026, 9, 18, 8, 0)),
    ("nb", "i ettermiddag", dt(2026, 9, 18, 15, 0)),
    ("nb", "i kveld", dt(2026, 9, 18, 20, 0)),
    ("nb", "i natt", dt(2026, 9, 18, 22, 0)),
    ("nb", "i morgen tidlig", dt(2026, 9, 19, 8, 0)),
    ("nb", "i morgen kveld", dt(2026, 9, 19, 20, 0)),
    ("nb", "i går kveld", dt(2026, 9, 17, 20, 0)),
    ("nb", "ved middagstid", dt(2026, 9, 18, 12, 0)),
    ("nb", "midnatt", dt(2026, 9, 18, 0, 0)),
    # Malay
    ("ms", "isnin depan", dt(2026, 9, 21)),
    ("ms", "sabtu depan", dt(2026, 9, 26)),
    ("ms", "ahad depan", dt(2026, 9, 27)),
    ("ms", "jumaat lepas", dt(2026, 9, 11)),
    ("ms", "sabtu lepas", dt(2026, 9, 12)),
    ("ms", "ahad yang lalu", dt(2026, 9, 13)),
    ("ms", "isnin ini", dt(2026, 9, 14)),
    ("ms", "ahad ini", dt(2026, 9, 20)),
    ("ms", "pagi ini", dt(2026, 9, 18, 8, 0)),
    ("ms", "tengah hari", dt(2026, 9, 18, 12, 0)),
    ("ms", "petang ini", dt(2026, 9, 18, 15, 0)),
    ("ms", "malam ini", dt(2026, 9, 18, 20, 0)),
    ("ms", "esok pagi", dt(2026, 9, 19, 8, 0)),
    ("ms", "esok malam", dt(2026, 9, 19, 20, 0)),
    ("ms", "malam semalam", dt(2026, 9, 17, 20, 0)),
    ("ms", "tengah malam", dt(2026, 9, 18, 0, 0)),
    # Romanian
    ("ro", "lunea viitoare", dt(2026, 9, 21)),
    ("ro", "sâmbăta viitoare", dt(2026, 9, 26)),
    ("ro", "duminică viitoare", dt(2026, 9, 27)),
    ("ro", "vinerea trecută", dt(2026, 9, 11)),
    ("ro", "sâmbăta trecută", dt(2026, 9, 12)),
    ("ro", "duminica trecută", dt(2026, 9, 13)),
    ("ro", "lunea aceasta", dt(2026, 9, 14)),
    ("ro", "în această dimineață", dt(2026, 9, 18, 8, 0)),
    ("ro", "la prânz", dt(2026, 9, 18, 12, 0)),
    ("ro", "diseară", dt(2026, 9, 18, 20, 0)),
    ("ro", "mâine dimineață", dt(2026, 9, 19, 8, 0)),
    ("ro", "mâine seară", dt(2026, 9, 19, 20, 0)),
    ("ro", "ieri seară", dt(2026, 9, 17, 20, 0)),
    ("ro", "la miezul nopții", dt(2026, 9, 18, 0, 0)),
    # Hungarian
    ("hu", "jövő hétfőn", dt(2026, 9, 21)),
    ("hu", "jövő szombaton", dt(2026, 9, 26)),
    ("hu", "a következő vasárnap", dt(2026, 9, 27)),
    ("hu", "múlt pénteken", dt(2026, 9, 11)),
    ("hu", "múlt szombaton", dt(2026, 9, 12)),
    ("hu", "múlt vasárnap", dt(2026, 9, 13)),
    ("hu", "ez a hétfő", dt(2026, 9, 14)),
    ("hu", "ezen a szombaton", dt(2026, 9, 19)),
    ("hu", "ma reggel", dt(2026, 9, 18, 8, 0)),
    ("hu", "délben", dt(2026, 9, 18, 12, 0)),
    ("hu", "ma este", dt(2026, 9, 18, 20, 0)),
    ("hu", "holnap reggel", dt(2026, 9, 19, 8, 0)),
    ("hu", "holnap este", dt(2026, 9, 19, 20, 0)),
    ("hu", "tegnap este", dt(2026, 9, 17, 20, 0)),
    ("hu", "éjfélkor", dt(2026, 9, 18, 0, 0)),
]


@pytest.mark.parametrize("lang,text,expected", WAVE7_CASES)
def test_wave7_global_scenarios(lang, text, expected):
    assert parse(text, langs=[lang], base_datetime=BASE) == expected
