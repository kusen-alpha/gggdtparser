# -*- coding: utf-8 -*-

import datetime

import pytest

from gggdtparser import parse


dt = datetime.datetime
td = datetime.timedelta


STRICT_CASES = [
    # 之前
    ("2年前", dt(2024, 1, 1)),
    ("2月前", dt(2026, 7, 18)),
    ("2周前", dt(2026, 9, 4)),
    ("2星期前", dt(2026, 9, 4)),
    ("2天前", dt(2026, 9, 16)),
    ("2小时前", dt(2026, 9, 18, 13, 0)),
    ("2分钟前", dt(2026, 9, 18, 15, 2)),
    ("2秒前", dt(2026, 9, 18, 15, 4, 3)),
    # 之内
    ("2天内", dt(2026, 9, 16)),
    ("2小时内", dt(2026, 9, 18, 13, 0)),
    ("2分钟内", dt(2026, 9, 18, 15, 2)),
    ("2秒内", dt(2026, 9, 18, 15, 4, 3)),
    ("2星期内", dt(2026, 9, 4)),
    # 之后
    ("2天后", dt(2026, 9, 20)),
    ("2小时后", dt(2026, 9, 18, 17, 0)),
    ("2分钟后", dt(2026, 9, 18, 15, 6)),
    ("2秒后", dt(2026, 9, 18, 15, 4, 7)),
    # 特殊语义
    ("今天", dt(2026, 9, 18)),
    ("今天 02:02", dt(2026, 9, 18, 2, 2)),
    ("昨天", dt(2026, 9, 17)),
    ("昨天02", dt(2026, 9, 17, 2, 0)),
    ("前天", dt(2026, 9, 16)),
    ("前天02:02:02", dt(2026, 9, 16, 2, 2, 2)),
    ("刚刚", dt(2026, 9, 18, 15, 4, 0)),
]


@pytest.mark.parametrize("text,expected", STRICT_CASES)
def test_relative_strict(base_dt, text, expected):
    assert parse(text, base_datetime=base_dt) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        ("1月后", dt(2024, 2, 29)),
    ],
)
def test_relative_month_end_clamp(text, expected):
    assert parse(text, base_datetime=dt(2024, 1, 31)) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        ("2022年02月", dt(2022, 2, 18, 15, 4, 5)),
        ("02月02日", dt(2026, 2, 2, 15, 4, 5)),
        ("2022-02-02 02:02", dt(2022, 2, 2, 2, 2, 5)),
    ],
)
def test_relative_unstrict_without_jitter(base_dt, text, expected):
    assert parse(
        text, result_accurately=False, base_datetime=base_dt
    ) == expected


@pytest.mark.parametrize(
    "text,start_offset,end_offset",
    [
        ("2天前", td(days=-3), td(days=-2)),
        ("2小时内", td(hours=-2), td(hours=-1)),
        ("2分钟内", td(minutes=-2), td(minutes=-1)),
        ("2秒内", td(seconds=-2), td(seconds=-1)),
        ("2天后", td(days=1), td(days=2)),
        ("2小时后", td(hours=1), td(hours=2)),
        ("2分钟后", td(minutes=1), td(minutes=2)),
        ("2秒后", td(seconds=1), td(seconds=2)),
    ],
)
def test_relative_unstrict_range(base_dt, text, start_offset, end_offset):
    result = parse(text, result_accurately=False, base_datetime=base_dt)
    assert base_dt + start_offset <= result <= base_dt + end_offset
