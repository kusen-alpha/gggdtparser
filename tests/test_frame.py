# -*- coding: utf-8 -*-

import datetime

import pytest

from gggdtparser import parse_frame


dt = datetime.datetime


@pytest.mark.parametrize(
    "text,seps,expected",
    [
        ("2022年10月1日至2023年10月1日", None,
         (dt(2022, 10, 1), dt(2023, 10, 1))),
        ("2022年10月1日 至 2023年10月1日", ["至"],
         (dt(2022, 10, 1), dt(2023, 10, 1))),
        ("2022-01-01 - 2022-12-31", None,
         (dt(2022, 1, 1), dt(2022, 12, 31))),
        ("2022-01-01 - 2022-12-31", ["-"],
         (dt(2022, 1, 1), dt(2022, 12, 31))),
        ("2022-01-01 ~ 2022-12-31", ["~"],
         (dt(2022, 1, 1), dt(2022, 12, 31))),
        ("2022-01-01 至 2022-12-31 ~ 2022-12-30", ["~"],
         (dt(2022, 1, 1), dt(2022, 12, 30))),
    ],
)
def test_parse_frame_ranges(text, seps, expected):
    kwargs = {}
    if seps is not None:
        kwargs["seps"] = seps
    assert parse_frame(text, **kwargs) == expected


def test_parse_frame_custom_regex_pair():
    result = parse_frame(
        "2022年1月至2022年12月",
        seps=["至"],
        regex_list=[(r"(?P<Y>\d{4})年(?P<m>\d{1,2})月",) * 2],
    )
    assert result == (dt(2022, 1, 1), dt(2022, 12, 1))


def test_parse_frame_custom_regex_single_entry(base_dt):
    result = parse_frame(
        "10个月",
        regex_list=[(r"(?P<am>\d+)\s*(个)?月",)],
        base_datetime=dt(2023, 1, 1),
    )
    assert result == (dt(2023, 1, 1), dt(2023, 11, 1))


def test_parse_frame_custom_format_list():
    result = parse_frame(
        "2022年1月至2022年12月",
        seps=["至"],
        format_list=[("%Y年%m月", "%Y年%m月")],
    )
    assert result == (dt(2022, 1, 1), dt(2022, 12, 1))


def test_frame_format_falls_back_to_default_rules():
    result = parse_frame(
        "2022年1月至2022年12月",
        seps=["至"],
        format_list=[("%Y-%m-%d", "%Y-%m-%d")],
    )
    assert result == (dt(2022, 1, 1), dt(2022, 12, 1))


@pytest.mark.parametrize(
    "text,expected",
    [
        ("10月1日", (dt(2026, 9, 18, 15, 4, 5), dt(2026, 10, 1))),
        ("至2022-01-01", (dt(2026, 9, 18, 15, 4, 5), dt(2022, 1, 1))),
    ],
)
def test_parse_frame_with_base_datetime(base_dt, text, expected):
    assert parse_frame(text, base_datetime=base_dt) == expected


def test_parse_frame_default_range_sep_list():
    result = parse_frame("2022-01-01至2022-12-31")
    assert result == (dt(2022, 1, 1), dt(2022, 12, 31))


@pytest.mark.parametrize(
    "text",
    [
        "",
        "   ",
        "no date here",
        "2022-02",
    ],
)
def test_parse_frame_no_range(text):
    assert parse_frame(text) == (None, None)


@pytest.mark.parametrize("value", [None, 123, 3.14, [], {}])
def test_parse_frame_rejects_non_string(value):
    assert parse_frame(value) == (None, None)

