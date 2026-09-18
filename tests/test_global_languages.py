# -*- coding: utf-8 -*-

import datetime

import pytest

from gggdtparser import parse


dt = datetime.datetime
TIME_DELTA = datetime.timedelta
BASE = dt(2026, 9, 18, 15, 4, 5)


# (lang, text, base_datetime, expected)
NEW_LANG_CASES = [
    # 意大利语
    ("it", "2 febbraio 2022", None, dt(2022, 2, 2)),
    ("it", "31 marzo 2023", None, dt(2023, 3, 31)),
    ("it", "mercoledì 2 febbraio 2022", None, dt(2022, 2, 2)),
    ("it", "2 ore fa", BASE, dt(2026, 9, 18, 13, 0)),
    ("it", "2 minuti fa", BASE, dt(2026, 9, 18, 15, 2)),
    # 荷兰语
    ("nl", "2 februari 2022", None, dt(2022, 2, 2)),
    ("nl", "woensdag 2 februari 2022", None, dt(2022, 2, 2)),
    ("nl", "3 uur geleden", BASE, dt(2026, 9, 18, 12, 0)),
    ("nl", "5 minuten geleden", BASE, dt(2026, 9, 18, 14, 59)),
    # 波兰语
    ("pl", "2 lutego 2022", None, dt(2022, 2, 2)),
    ("pl", "środa, 2 lutego 2022", None, dt(2022, 2, 2)),
    ("pl", "2 godziny temu", BASE, dt(2026, 9, 18, 13, 0)),
    ("pl", "10 minut temu", BASE, dt(2026, 9, 18, 14, 54)),
    # 希腊语
    ("el", "2 Φεβρουαρίου 2022", None, dt(2022, 2, 2)),
    ("el", "πριν από 2 ώρες", BASE, dt(2026, 9, 18, 13, 0)),
    # 芬兰语
    ("fi", "2. helmikuuta 2022", None, dt(2022, 2, 2)),
    ("fi", "3 tuntia sitten", BASE, dt(2026, 9, 18, 12, 0)),
    # 匈牙利语
    ("hu", "2022. február 2.", None, dt(2022, 2, 2)),
    ("hu", "2 órája", BASE, dt(2026, 9, 18, 13, 0)),
    # 捷克语
    ("cs", "2. února 2022", None, dt(2022, 2, 2)),
    ("cs", "2 hodinami zpět", BASE, dt(2026, 9, 18, 13, 0)),
    # 瑞典语
    ("sv_se", "2 februari 2022", None, dt(2022, 2, 2)),
    ("sv_se", "3 timmar sedan", BASE, dt(2026, 9, 18, 12, 0)),
    # 挪威语
    ("nb", "2. februar 2022", None, dt(2022, 2, 2)),
    ("no", "3 timer siden", BASE, dt(2026, 9, 18, 12, 0)),
    # 丹麦语
    ("da", "2. februar 2022", None, dt(2022, 2, 2)),
    ("da", "3 timer siden", BASE, dt(2026, 9, 18, 12, 0)),
    # 希伯来语
    ("he", "2 בפברואר 2022", None, dt(2022, 2, 2)),
    ("he", "לפני 3 שעות", BASE, dt(2026, 9, 18, 12, 0)),
    # 泰语(佛历)
    ("th", "2 กุมภาพันธ์ 2565", None, dt(2022, 2, 2)),
    ("th", "2 ก.พ. 2565", None, dt(2022, 2, 2)),
    ("th", "2565/02/02", None, dt(2022, 2, 2)),
    ("th", "2565-02-02 15:30", None, dt(2022, 2, 2, 15, 30)),
]


@pytest.mark.parametrize("lang,text,base,expected", NEW_LANG_CASES)
def test_parse_new_lang(lang, text, base, expected):
    kwargs = {"langs": [lang]}
    if base is not None:
        kwargs["base_datetime"] = base
    assert parse(text, **kwargs) == expected


@pytest.mark.parametrize(
    "lang,text,expected",
    [
        ("hi", "15 फरवरी 2023", dt(2023, 2, 15)),
        ("id", "2 Februari 2022 15.30", dt(2022, 2, 2, 15, 30)),
        ("tr", "2 Şubat 2022 15:30", dt(2022, 2, 2, 15, 30)),
        ("ru", "2 февраля 2022", dt(2022, 2, 2)),
    ],
)
def test_parse_existing_lang_expanded(lang, text, expected):
    assert parse(text, langs=[lang]) == expected


@pytest.mark.parametrize("lang", ["ar", "fa", "bn"])
def test_unknown_writing_recommended_for_translation(lang):
    assert parse("2022-02-02", langs=[lang]) is None


@pytest.mark.parametrize(
    "text,expected",
    [
        # 阿拉伯文经翻译函数转成数字日期
        ("٢٠٢٢/٠٢/٠٢", dt(2022, 2, 2)),
        # 波斯文经翻译函数并按波斯历换算成公历日期
        ("۱۴۰۱/۱۱/۱۲", dt(2023, 2, 1)),
        # 孟加拉文经翻译函数转成数字日期
        ("২০২২/০২/০২", dt(2022, 2, 2)),
    ],
)
def test_translate_func_for_other_scripts(text, expected):
    def _is_leap_jalali(year):
        return (25 * year + 11) % 33 < 8

    def _jalali_to_gregorian(jy, jm, jd):
        day_of_year = (
            (jm - 1) * 31 + jd if jm <= 6 else 186 + (jm - 7) * 30 + jd)
        ordinal = datetime.date(2022, 3, 21).toordinal()
        for year in range(1401, jy):
            ordinal += 365 + int(_is_leap_jalali(year))
        return datetime.date.fromordinal(ordinal + day_of_year - 1)

    def translate(s):
        has_persian_digits = any(c in "۰۱۲۳۴۵۶۷۸۹" for c in s)
        table = {
            "٠": "0", "١": "1", "٢": "2", "٣": "3", "٤": "4",
            "٥": "5", "٦": "6", "٧": "7", "٨": "8", "٩": "9",
            "۰": "0", "۱": "1", "۲": "2", "۳": "3", "۴": "4",
            "۵": "5", "۶": "6", "۷": "7", "۸": "8", "۹": "9",
            "০": "0", "১": "1", "২": "2", "৩": "3", "৪": "4",
            "৫": "5", "৬": "6", "৭": "7", "৮": "8", "৯": "9",
        }
        s = "".join(table.get(c, c) for c in s)
        parts = s.split("/")
        if has_persian_digits and len(parts) == 3 and parts[0].isdigit():
            jy, jm, jd = (int(p) for p in parts)
            gy, gm, gd = _jalali_to_gregorian(jy, jm, jd).timetuple()[:3]
            return "%04d-%02d-%02d" % (gy, gm, gd)
        return s

    assert parse(text, translate_func=translate) == expected
