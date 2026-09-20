# -*- coding: utf-8 -*-

import datetime

import pytest

from gggdtparser import parse


dt = datetime.datetime
BASE = dt(2026, 9, 18, 15, 4, 5)


ENGLISH_CASES = [
    ("10:30 p.m.", dt(2026, 9, 18, 22, 30)),
    ("10:30 a.m.", dt(2026, 9, 18, 10, 30)),
    ("11:45 P.M.", dt(2026, 9, 18, 23, 45)),
    ("just now", dt(2026, 9, 18, 15, 4, 0)),
    ("noon", dt(2026, 9, 18, 12, 0)),
    ("midnight", dt(2026, 9, 18, 0, 0)),
    ("today", dt(2026, 9, 18)),
    ("tomorrow", dt(2026, 9, 19)),
    ("yesterday", dt(2026, 9, 17)),
    ("the day after tomorrow", dt(2026, 9, 20)),
    ("day before yesterday", dt(2026, 9, 16)),
    ("next Monday", dt(2026, 9, 21)),
    ("last Monday", dt(2026, 9, 14)),
    ("this Monday", dt(2026, 9, 14)),
    ("in 2 hours", dt(2026, 9, 18, 17, 0)),
    ("in 3 minutes", dt(2026, 9, 18, 15, 7)),
    ("in 4 days", dt(2026, 9, 22)),
    ("in 2 weeks", dt(2026, 10, 2)),
    ("in 2 months", dt(2026, 11, 18)),
    ("in 1 year", dt(2027, 1, 1)),
    ("2 hours later", dt(2026, 9, 18, 17, 0)),
    ("half past 3", dt(2026, 9, 18, 3, 30)),
    ("quarter past 3", dt(2026, 9, 18, 3, 15)),
    ("quarter to 4", dt(2026, 9, 18, 3, 45)),
    ("next week", dt(2026, 9, 25)),
    ("last week", dt(2026, 9, 11)),
    ("next month", dt(2026, 10, 18)),
    ("last month", dt(2026, 8, 18)),
    ("next year", dt(2027, 1, 1)),
    ("last year", dt(2025, 1, 1)),
]


@pytest.mark.parametrize("text,expected", ENGLISH_CASES)
def test_english_extended_scenarios(text, expected):
    assert parse(text, langs=["en"], base_datetime=BASE) == expected


CHINESE_CASES = [
    ("今年", dt(2026, 1, 1)),
    ("明年", dt(2027, 1, 1)),
    ("去年", dt(2025, 1, 1)),
    ("明年2月2日", dt(2027, 2, 2)),
    ("去年12月31日", dt(2025, 12, 31)),
    ("上个月", dt(2026, 8, 18)),
    ("下个月", dt(2026, 10, 18)),
    ("下个月5日", dt(2026, 10, 5)),
    ("下周一", dt(2026, 9, 21)),
    ("上周一", dt(2026, 9, 14)),
    ("这周一", dt(2026, 9, 14)),
    ("星期一", dt(2026, 9, 14)),
    ("周三", dt(2026, 9, 16)),
    ("周日", dt(2026, 9, 20)),
    ("星期天", dt(2026, 9, 20)),
    ("明天", dt(2026, 9, 19)),
    ("后天", dt(2026, 9, 20)),
    ("凌晨3点", dt(2026, 9, 18, 3, 0)),
    ("早上7点", dt(2026, 9, 18, 7, 0)),
    ("中午12点", dt(2026, 9, 18, 12, 0)),
    ("下午5点", dt(2026, 9, 18, 17, 0)),
    ("傍晚6点", dt(2026, 9, 18, 18, 0)),
    ("晚上8点半", dt(2026, 9, 18, 20, 30)),
    ("夜里11点", dt(2026, 9, 18, 23, 0)),
    ("十点半", dt(2026, 9, 18, 10, 30)),
    ("上午10:00", dt(2026, 9, 18, 10, 0)),
    ("贰零零二年二月二日", dt(2002, 2, 2)),
    ("二〇二二年二月二日", dt(2022, 2, 2)),
]


@pytest.mark.parametrize("text,expected", CHINESE_CASES)
def test_chinese_extended_scenarios(text, expected):
    assert parse(text, base_datetime=BASE) == expected


JAPANESE_CASES = [
    ("R4.2.2", None, dt(2022, 2, 2)),
    ("R5年2月2日", None, dt(2023, 2, 2)),
    ("令和4年2月2日 午後3時半", None, dt(2022, 2, 2, 15, 30)),
    ("午前3時半", BASE, dt(2026, 9, 18, 3, 30)),
    ("午後3時半", BASE, dt(2026, 9, 18, 15, 30)),
    ("午後8時", BASE, dt(2026, 9, 18, 20, 0)),
]


@pytest.mark.parametrize("text,base,expected", JAPANESE_CASES)
def test_japanese_extended_scenarios(text, base, expected):
    kwargs = {"langs": ["ja"]}
    if base is not None:
        kwargs["base_datetime"] = base
    assert parse(text, **kwargs) == expected


SCRIPT_CASES = [
    ("2 فبراير 2022", ["ar"], dt(2022, 2, 2)),
    ("فبراير ٢٠٢٢", ["ar"], dt(2022, 2, 1)),
    ("١٥ مارس ٢٠٢٣", ["ar"], dt(2023, 3, 15)),
    ("15 كانون الثاني 2022", ["ar"], dt(2022, 1, 15)),
    ("۲ فوریه ۲۰۲۲", ["fa"], dt(2022, 2, 2)),
    ("فوریه ۲۰۲۲", ["fa"], dt(2022, 2, 1)),
    ("بهمن ۱۴۰۰", ["fa"], dt(2022, 1, 21)),
    ("۲۵ اسفند ۱۴۰۰", ["fa"], dt(2022, 3, 16)),
    ("۱۴۰۱/۱۱/۱۲", ["fa"], dt(2023, 2, 1)),
    ("۲۰۲۲/۰۲/۰۲", ["fa"], dt(2022, 2, 2)),
    ("১৫ মার্চ ২০২৩", ["bn"], dt(2023, 3, 15)),
    ("ফেব্রুয়ারি ২০২২", ["bn"], dt(2022, 2, 1)),
    ("২ ফেব্রুয়ারি ২০২২", ["bn"], dt(2022, 2, 2)),
    ("২০২২/০২/০২", ["bn"], dt(2022, 2, 2)),
    ("௧௫ மார்ச் ௨௦௨௩", ["ta"], dt(2023, 3, 15)),
    ("மார்ச் ௨௦௨௩", ["ta"], dt(2023, 3, 1)),
    ("15 మార్చి 2023", ["te"], dt(2023, 3, 15)),
    ("౧౫ మే ౨౦౨౩", ["te"], dt(2023, 5, 15)),
    ("15 માર્ચ 2023", ["gu"], dt(2023, 3, 15)),
    ("15 ਮਾਰਚ 2023", ["pa"], dt(2023, 3, 15)),
]


@pytest.mark.parametrize("text,langs,expected", SCRIPT_CASES)
def test_native_script_dates(text, langs, expected):
    assert parse(text, langs=langs) == expected


def test_native_script_dates_in_automatic_mode():
    assert parse("١٥ مارس ٢٠٢٣") == dt(2023, 3, 15)
    assert parse("۱۴۰۱/۱۱/۱۲") == dt(2023, 2, 1)
    assert parse("১৫ মার্চ ২০২৩") == dt(2023, 3, 15)
