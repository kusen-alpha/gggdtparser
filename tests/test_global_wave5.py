# -*- coding: utf-8 -*-

import datetime

import pytest

from gggdtparser import parse
from gggdtparser.calendars import (
    hijri_to_gregorian,
    iso_week_to_gregorian,
    ordinal_day_to_month_day,
)


dt = datetime.datetime
BASE = dt(2026, 9, 18, 15, 4, 5)


ISO_ORDINAL_CASES = [
    ("en", "2025-W15-3", dt(2025, 4, 9)),
    ("en", "2024-W01-1", dt(2024, 1, 1)),
    ("en", "2024-W01-7", dt(2024, 1, 7)),
    ("en", "2026-W38-5", dt(2026, 9, 18)),
    ("en", "2025-001", dt(2025, 1, 1)),
    ("en", "2025-060", dt(2025, 3, 1)),
    ("en", "2024-060", dt(2024, 2, 29)),
    ("en", "2027-365", dt(2027, 12, 31)),
]


HIJRI_CASES = [
    ("ar", "6 شوال 1443", dt(2022, 5, 7)),
    ("ar", "٦ شوال ١٤٤٣", dt(2022, 5, 7)),
    ("ar", "6 شوال 1443 هـ", dt(2022, 5, 7)),
    ("ar", "1 محرم 1444", dt(2022, 7, 30)),
    ("ar", "1 محرم 1443", dt(2021, 8, 9)),
    ("ar", "10 رمضان 1444", dt(2023, 4, 1)),
]


DIRECTIONAL_WEEKDAY_CASES = [
    ("zh", "下周一", dt(2026, 9, 21)),
    ("zh", "下周六", dt(2026, 9, 26)),
    ("zh", "上周五", dt(2026, 9, 11)),
    ("zh", "上周日", dt(2026, 9, 13)),
    ("zh", "这周六", dt(2026, 9, 19)),
    ("en", "next Monday", dt(2026, 9, 21)),
    ("en", "next Saturday", dt(2026, 9, 26)),
    ("en", "next Sunday", dt(2026, 9, 27)),
    ("en", "next Friday", dt(2026, 9, 25)),
    ("en", "last Friday", dt(2026, 9, 11)),
    ("en", "last Sunday", dt(2026, 9, 13)),
    ("en", "this Monday", dt(2026, 9, 14)),
    ("fra", "lundi prochain", dt(2026, 9, 21)),
    ("fra", "samedi prochain", dt(2026, 9, 26)),
    ("fra", "vendredi dernier", dt(2026, 9, 11)),
    ("fra", "dimanche dernier", dt(2026, 9, 13)),
    ("fra", "ce lundi", dt(2026, 9, 14)),
    ("de", "nächsten Montag", dt(2026, 9, 21)),
    ("de", "kommenden Montag", dt(2026, 9, 21)),
    ("de", "nächsten Samstag", dt(2026, 9, 26)),
    ("de", "nächsten Sonntag", dt(2026, 9, 27)),
    ("de", "letzten Freitag", dt(2026, 9, 11)),
    ("de", "letzten Sonntag", dt(2026, 9, 13)),
    ("de", "vergangener Sonntag", dt(2026, 9, 13)),
    ("de", "diesen Montag", dt(2026, 9, 14)),
    ("es", "el próximo lunes", dt(2026, 9, 21)),
    ("es", "el próximo sábado", dt(2026, 9, 26)),
    ("es", "viernes pasado", dt(2026, 9, 11)),
    ("es", "domingo pasado", dt(2026, 9, 13)),
    ("es", "este lunes", dt(2026, 9, 14)),
    ("es", "lunes que viene", dt(2026, 9, 21)),
    ("es", "sábado que viene", dt(2026, 9, 26)),
    ("es", "el domingo que viene", dt(2026, 9, 27)),
    ("ru", "в следующий понедельник", dt(2026, 9, 21)),
    ("ru", "в следующую субботу", dt(2026, 9, 26)),
    ("ru", "в следующее воскресенье", dt(2026, 9, 27)),
    ("ru", "прошлую пятницу", dt(2026, 9, 11)),
    ("ru", "прошлое воскресенье", dt(2026, 9, 13)),
    ("ru", "этот понедельник", dt(2026, 9, 14)),
    ("it", "lunedì prossimo", dt(2026, 9, 21)),
    ("it", "sabato prossimo", dt(2026, 9, 26)),
    ("it", "domenica prossima", dt(2026, 9, 27)),
    ("it", "prossimo sabato", dt(2026, 9, 26)),
    ("it", "venerdì scorso", dt(2026, 9, 11)),
    ("it", "domenica scorsa", dt(2026, 9, 13)),
    ("it", "questo lunedì", dt(2026, 9, 14)),
    ("ja", "来週の月曜日", dt(2026, 9, 21)),
    ("ja", "来週の土曜日", dt(2026, 9, 26)),
    ("ja", "次の月曜日", dt(2026, 9, 21)),
    ("ja", "先週の金曜日", dt(2026, 9, 11)),
    ("ja", "先週の日曜日", dt(2026, 9, 13)),
    ("ko", "오는 월요일", dt(2026, 9, 21)),
    ("ko", "다음 주 월요일", dt(2026, 9, 21)),
    ("ko", "다음 주 토요일", dt(2026, 9, 26)),
    ("ko", "지난 주 금요일", dt(2026, 9, 11)),
    ("ko", "지난 주 일요일", dt(2026, 9, 13)),
    ("ko", "이번 주 월요일", dt(2026, 9, 14)),
    ("ar", "الجمعة القادم", dt(2026, 9, 25)),
    ("ar", "السبت القادم", dt(2026, 9, 26)),
    ("ar", "الجمعة الماضي", dt(2026, 9, 11)),
    ("ar", "الأحد الماضي", dt(2026, 9, 13)),
    ("he", "יום ראשון הבא", dt(2026, 9, 27)),
    ("he", "שבת הבאה", dt(2026, 9, 26)),
    ("he", "יום שישי שעבר", dt(2026, 9, 11)),
    ("he", "יום ראשון שעבר", dt(2026, 9, 13)),
    ("he", "שבת שעברה", dt(2026, 9, 12)),
]


TIME_OF_DAY_CASES = [
    ("zh", "今晚", dt(2026, 9, 18, 22, 0)),
    ("zh", "明天早上", dt(2026, 9, 19, 8, 0)),
    ("zh", "昨天晚上", dt(2026, 9, 17, 22, 0)),
    ("zh", "半小时后", dt(2026, 9, 18, 15, 34, 0)),
    ("zh", "半小时前", dt(2026, 9, 18, 14, 34, 0)),
    ("zh", "一刻钟后", dt(2026, 9, 18, 15, 19, 0)),
    ("en", "this morning", dt(2026, 9, 18, 8, 0)),
    ("en", "this afternoon", dt(2026, 9, 18, 15, 0)),
    ("en", "tonight", dt(2026, 9, 18, 20, 0)),
    ("en", "tomorrow morning", dt(2026, 9, 19, 8, 0)),
    ("en", "tomorrow afternoon", dt(2026, 9, 19, 15, 0)),
    ("en", "tomorrow evening", dt(2026, 9, 19, 20, 0)),
    ("en", "at noon", dt(2026, 9, 18, 12, 0)),
    ("en", "midnight", dt(2026, 9, 18, 0, 0)),
    ("fra", "ce matin", dt(2026, 9, 18, 8, 0)),
    ("fra", "ce midi", dt(2026, 9, 18, 12, 0)),
    ("fra", "cet après-midi", dt(2026, 9, 18, 15, 0)),
    ("fra", "ce soir", dt(2026, 9, 18, 22, 0)),
    ("fra", "hier soir", dt(2026, 9, 17, 20, 0)),
    ("fra", "demain matin", dt(2026, 9, 19, 8, 0)),
    ("fra", "demain soir", dt(2026, 9, 19, 20, 0)),
    ("de", "heute Morgen", dt(2026, 9, 18, 8, 0)),
    ("de", "heute Mittag", dt(2026, 9, 18, 12, 0)),
    ("de", "heute Abend", dt(2026, 9, 18, 20, 0)),
    ("de", "gestern Morgen", dt(2026, 9, 17, 8, 0)),
    ("de", "morgen früh", dt(2026, 9, 19, 8, 0)),
    ("de", "um Mitternacht", dt(2026, 9, 18, 0, 0)),
    ("es", "esta mañana", dt(2026, 9, 18, 8, 0)),
    ("es", "esta noche", dt(2026, 9, 18, 22, 0)),
    ("es", "anoche", dt(2026, 9, 17, 22, 0)),
    ("es", "mañana por la mañana", dt(2026, 9, 19, 8, 0)),
    ("es", "a mediodía", dt(2026, 9, 18, 12, 0)),
    ("ru", "сегодня вечером", dt(2026, 9, 18, 20, 0)),
    ("ru", "завтра утром", dt(2026, 9, 19, 8, 0)),
    ("ru", "вчера вечером", dt(2026, 9, 17, 20, 0)),
    ("ru", "в полдень", dt(2026, 9, 18, 12, 0)),
    ("it", "stamattina", dt(2026, 9, 18, 8, 0)),
    ("it", "stasera", dt(2026, 9, 18, 20, 0)),
    ("it", "stanotte", dt(2026, 9, 18, 23, 0)),
    ("it", "domani sera", dt(2026, 9, 19, 20, 0)),
    ("it", "ieri sera", dt(2026, 9, 17, 20, 0)),
    ("ja", "今朝", dt(2026, 9, 18, 8, 0)),
    ("ja", "今夜", dt(2026, 9, 18, 22, 0)),
    ("ja", "明日の朝", dt(2026, 9, 19, 8, 0)),
    ("ja", "昨日の夜", dt(2026, 9, 17, 22, 0)),
    ("ja", "正午", dt(2026, 9, 18, 12, 0)),
    ("ko", "오늘 아침", dt(2026, 9, 18, 8, 0)),
    ("ko", "내일 아침", dt(2026, 9, 19, 8, 0)),
    ("ko", "어제 밤", dt(2026, 9, 17, 20, 0)),
    ("ko", "정오", dt(2026, 9, 18, 12, 0)),
    ("ar", "الليلة", dt(2026, 9, 18, 20, 0)),
    ("ar", "اليوم في الصباح", dt(2026, 9, 18, 8, 0)),
    ("ar", "غدا في الصباح", dt(2026, 9, 19, 8, 0)),
    ("ar", "منتصف الليل", dt(2026, 9, 18, 0, 0)),
    ("he", "הבוקר", dt(2026, 9, 18, 8, 0)),
    ("he", "הצהריים", dt(2026, 9, 18, 12, 0)),
    ("he", "הערב", dt(2026, 9, 18, 20, 0)),
    ("he", "מחר בבוקר", dt(2026, 9, 19, 8, 0)),
    ("he", "אתמול בערב", dt(2026, 9, 17, 20, 0)),
    ("he", "חצות", dt(2026, 9, 18, 0, 0)),
]


INVALID_CALENDAR_CASES = [
    ("en", "2026-366"),
    ("en", "2025-W54-1"),
    ("en", "2025-W15-0"),
]


@pytest.mark.parametrize(
    "lang,text,expected",
    ISO_ORDINAL_CASES
    + HIJRI_CASES
    + DIRECTIONAL_WEEKDAY_CASES
    + TIME_OF_DAY_CASES,
)
def test_wave5_global_scenarios(lang, text, expected):
    assert parse(text, langs=[lang], base_datetime=BASE) == expected


@pytest.mark.parametrize("lang,text", INVALID_CALENDAR_CASES)
def test_wave5_invalid_calendar_dates_are_rejected(lang, text):
    assert parse(text, langs=[lang], base_datetime=BASE) is None


@pytest.mark.parametrize(
    "year,week,weekday,expected",
    [
        (2024, 1, 1, datetime.date(2024, 1, 1)),
        (2025, 15, 3, datetime.date(2025, 4, 9)),
        (2015, 53, 7, datetime.date(2016, 1, 3)),
        (2025, 54, 1, None),
    ],
)
def test_iso_week_helper(year, week, weekday, expected):
    assert iso_week_to_gregorian(year, week, weekday) == expected


@pytest.mark.parametrize(
    "year,day_of_year,expected",
    [
        (2024, 60, (2, 29)),
        (2025, 60, (3, 1)),
        (2027, 365, (12, 31)),
        (2026, 366, None),
        (2025, 0, None),
        (2025, 366, None),
    ],
)
def test_ordinal_day_helper(year, day_of_year, expected):
    assert ordinal_day_to_month_day(year, day_of_year) == expected


@pytest.mark.parametrize(
    "hy,hm,hd,expected",
    [
        (1443, 1, 1, datetime.date(2021, 8, 9)),
        (1444, 1, 1, datetime.date(2022, 7, 30)),
        (1443, 10, 6, datetime.date(2022, 5, 7)),
        (1440, 12, 30, None),
        (1443, 13, 1, None),
        (1443, 1, 0, None),
    ],
)
def test_hijri_helper(hy, hm, hd, expected):
    assert hijri_to_gregorian(hy, hm, hd) == expected
