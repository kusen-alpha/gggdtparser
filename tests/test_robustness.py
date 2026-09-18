# -*- coding: utf-8 -*-

import datetime

import pytest

from gggdtparser import check
from gggdtparser import parse
from gggdtparser import parse_by_format
from gggdtparser import parse_by_regex
from gggdtparser import parse_frame


dt = datetime.datetime


@pytest.mark.parametrize("value", [None, 123, 12.5, ["2022-02-02"],
                                   {"t": "2022-02-02"}, b"2022-02-02"])
def test_parse_rejects_non_string(value):
    assert parse(value) is None


@pytest.mark.parametrize("text", ["", "   ", "\t\n"])
def test_parse_empty_or_blank(text):
    assert parse(text) is None


def test_parse_noise_text_without_date():
    assert parse("这是一段完全没有日期时间的文本") is None
    assert parse("<div>hello world</div>") is None


@pytest.mark.parametrize(
    "text,expected",
    [
        ("2023-02-31", None),
        ("2023-02-30", None),
        ("2022-13-01", None),
        ("2022-00-01", None),
        ("2022-02-00", None),
        ("2022-02-02 24:00", None),
        ("2022-02-02 25:61", None),
        ("2022-02-02 02:61", None),
        ("12345678", None),
        ("2022-02-32", None),
    ],
)
def test_parse_invalid_dates(text, expected):
    assert parse(text) is expected


def test_parse_result_boundaries(base_dt):
    value = parse(
        "2022-02-02 02:02",
        max_datetime=dt(2022, 2, 2, 3),
        min_datetime=dt(2022, 2, 2, 1),
    )
    assert value == dt(2022, 2, 2, 2, 2)
    assert parse("2022-02-02", max_datetime=dt(2022, 1, 1)) is None
    assert parse("2022-02-02", min_datetime=dt(2022, 3, 1)) is None


def test_parse_by_regex_invalid_lang(base_dt):
    assert parse_by_regex("2022-02-02", langs=["xx"]) is None


def test_parse_by_regex_invalid_patterns():
    # 无效正则被静默跳过，默认规则仍可兜底解析
    assert parse_by_regex("2022-02-02", regex_list=[r"["]) == dt(2022, 2, 2)
    assert parse_by_regex("没有日期", regex_list=[r"["]) is None
    assert parse("2022-02-02", regex_list=[r"["]) == dt(2022, 2, 2)
    assert parse("没有日期", regex_list=[r"["]) is None


def test_parse_by_format_default_paths():
    assert parse_by_format("2022-02-02", ["%Y-%m-%d"]) == dt(2022, 2, 2)
    assert parse_by_format("2022-02-02", ["%Y/%m/%d"]) is None
    assert parse_by_format("2022-02-02") is None


def test_parse_frame_exception_safety():
    assert parse_frame("") == (None, None)
    assert parse_frame(None) == (None, None)
    assert parse_frame("只有一句话") == (None, None)


def test_check_equal_and_range():
    value = dt(2022, 2, 2, 2, 2)
    assert check(value, value) is True
    assert check(value, (dt(2022, 2, 2, 2), dt(2022, 2, 2, 3))) is True
    assert check(value, (dt(2022, 2, 2, 3), dt(2022, 2, 2, 4))) is False


def test_check_invalid_input_raises():
    with pytest.raises(TypeError):
        check(dt(2022, 2, 2), None)
