# -*- coding: utf-8 -*-

import datetime

import pytest

from gggdtparser import parse


dt = datetime.datetime
TIME_DELTA = datetime.timedelta
BASE = dt(2026, 9, 18, 15, 4, 5)


@pytest.mark.parametrize(
    "text,langs,expected",
    [
        # 日历年号
        ("令和4年2月2日", ["ja"], dt(2022, 2, 2)),
        ("平成32年2月2日", ["ja"], dt(2020, 2, 2)),
        # 朝鲜谚文上下午
        ("2022년 2월 2일 오후 3:30", ["ko"], dt(2022, 2, 2, 15, 30)),
        ("2022년 2월 2일 오전 9:05", ["ko"], dt(2022, 2, 2, 9, 5)),
        # 土耳其语上下午
        ("2 Şubat 2022 öğleden sonra 3:30", ["tr"],
         dt(2022, 2, 2, 15, 30)),
    ],
)
def test_era_and_period_notation(text, langs, expected):
    assert parse(text, langs=langs) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        ("2nd of February 2022", dt(2022, 2, 2)),
        ("February 2nd, 2022", dt(2022, 2, 2)),
        ("23rd December 2022 15:20", dt(2022, 12, 23, 15, 20)),
        ("1st March 2023", dt(2023, 3, 1)),
        ("4th July 2023", dt(2023, 7, 4)),
    ],
)
def test_english_ordinals(text, expected):
    assert parse(text, langs=["en"]) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        ("2022-02-02T14:30:20.123Z", dt(2022, 2, 2, 14, 30, 20)),
        ("2022-02-02T14:30:20+00:00", dt(2022, 2, 2, 14, 30, 20)),
        ("2022-02-02t14:30:20.123z", dt(2022, 2, 2, 14, 30, 20)),
    ],
)
def test_iso_millis_and_utc(text, expected):
    assert parse(text) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        ("Wed, 02 Feb 2022 14:30:20 +0530", dt(2022, 2, 2, 14, 30, 20)),
        ("Wed, 02 Feb 2022 14:30:20 -0500", dt(2022, 2, 2, 14, 30, 20)),
        ("Sat, 05 Feb 2022 18:33:00 GMT", dt(2022, 2, 5, 18, 33)),
    ],
)
def test_rfc822_with_seconds(text, expected):
    assert parse(text, langs=["en"]) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        ("２０２２／０２／０２", dt(2022, 2, 2)),
        ("２０２２年０２月０２日 １４：３０", dt(2022, 2, 2, 14, 30)),
        ("２０２２−０２−０２Ｔ１４：３０：２０．１２３Ｚ",
         dt(2022, 2, 2, 14, 30, 20)),
    ],
)
def test_fullwidth_digits_and_separators(text, expected):
    assert parse(text) == expected


@pytest.mark.parametrize(
    "text,langs,expected",
    [
        # 带星期的日期
        ("mercredi 2 février 2022", ["fr"], dt(2022, 2, 2)),
        ("miércoles, 2 de febrero de 2022", ["es"], dt(2022, 2, 2)),
        ("quarta-feira, 2 de fevereiro de 2022", ["pt"],
         dt(2022, 2, 2)),
        # 越南语 ngày/tháng/năm 词形
        ("ngày 2 tháng 2 năm 2022", ["vi"], dt(2022, 2, 2)),
    ],
)
def test_weekday_and_native_markers(text, langs, expected):
    assert parse(text, langs=langs) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        # 印尼语日期+点分时间
        ("2 Februari 2022 15.30", dt(2022, 2, 2, 15, 30)),
        # 韩语星期符号
        ("2022년 2월 2일 (수)", dt(2022, 2, 2)),
        # 繁体中文星期
        ("2022年2月2日（星期三）", dt(2022, 2, 2)),
    ],
)
def test_mixed_separators(text, expected):
    langs = ["id"] if "Februari" in text else (
        ["ko"] if "년" in text else ["zh-TW"])
    assert parse(text, langs=langs) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        ("2 hours ago", dt(2026, 9, 18, 13, 0)),
        ("2 days ago", dt(2026, 9, 16, 0, 0)),
        ("2 weeks ago", dt(2026, 9, 4, 0, 0)),
        ("2 months ago", dt(2026, 7, 18, 0, 0)),
        ("2 years ago", dt(2024, 1, 1)),
    ],
)
def test_english_relative_multiple_units(text, expected):
    assert parse(text, langs=["en"], base_datetime=BASE) == expected


def test_thai_digits_buddhist_year():
    # 泰文数字 2565 -> 公历 2022
    assert parse("๒๕๖๕/๐๒/๐๒", langs=["th"]) == dt(2022, 2, 2)
    # 阿拉伯-印度数字不应被佛历换算静默改写
    assert parse("٢٥٦٥/٠٢/٠٢") == dt(2565, 2, 2)
    assert parse("2565/02/02", langs=["th"]) == dt(2022, 2, 2)
