# -*- coding: utf-8 -*-

import datetime

import pytest

from gggdtparser import parse
from gggdtparser import parse_by_format
from gggdtparser import parse_by_regex


dt = datetime.datetime


@pytest.mark.parametrize(
    "text,formats,expected",
    [
        ("2022-02-02", ["%Y-%m-%d"], dt(2022, 2, 2)),
        ("2022/02/02 02:02", ["%Y-%m-%d", "%Y/%m/%d %H:%M"],
         dt(2022, 2, 2, 2, 2)),
        ("2022年2月2日", ["%Y年%m月%d日"], dt(2022, 2, 2)),
        ("2022-02-02", "%Y-%m-%d", dt(2022, 2, 2)),
    ],
)
def test_parse_by_format(text, formats, expected):
    assert parse_by_format(text, formats) == expected


@pytest.mark.parametrize("value", [None, 123, 12.5, ["2022"], {"t": "2022"}])
def test_parse_by_format_rejects_non_string(value):
    assert parse_by_format(value, ["%Y-%m-%d"]) is None


@pytest.mark.parametrize(
    "text,formats,expected",
    [
        ("2022-02-02", ["%Y/%m/%d"], dt(2022, 2, 2)),
        ("2022年02月02日 02:02", ["%Y-%m-%d %H:%M:%S"],
         dt(2022, 2, 2, 2, 2)),
    ],
)
def test_parse_format_falls_back_to_regex(text, formats, expected):
    assert parse(text, format_list=formats) == expected


def test_parse_format_respects_max_boundary():
    assert parse(
        "2022-02-02", format_list=["%Y-%m-%d"],
        max_datetime=dt(2022, 1, 1)) is None


def test_parse_format_respects_min_boundary():
    assert parse(
        "2022-02-02", format_list=["%Y-%m-%d"],
        min_datetime=dt(2022, 3, 1)) is None


@pytest.mark.parametrize(
    "text,regex_list,expected",
    [
        ("2022-02-02", r"(?P<Y>\d{4})-(?P<m>\d{2})-(?P<d>\d{2})",
         dt(2022, 2, 2)),
        ("2022-02-02",
         [r"(?P<m>\d{2})-(?P<d>\d{2})",
          r"(?P<Y>\d{4})-(?P<m>\d{2})-(?P<d>\d{2})"],
         dt(2022, 2, 2)),
        ("发布于：2022-02-02", [r"(?P<Y>\d{4})-(?P<m>\d{2})-(?P<d>\d{2})"],
         dt(2022, 2, 2)),
        ("2022-02-02", [None, r"(?P<Y>\d{4})-(?P<m>\d{2})-(?P<d>\d{2})"],
         dt(2022, 2, 2)),
        ("2022-02-02", [42, r"(?P<Y>\d{4})-(?P<m>\d{2})-(?P<d>\d{2})"],
         dt(2022, 2, 2)),
        ("2022-02-02", [r"["], dt(2022, 2, 2)),
    ],
)
def test_custom_regex_list(text, regex_list, expected):
    assert parse(text, regex_list=regex_list) == expected


def test_custom_regex_prefers_more_accurate_candidate():
    assert parse(
        "更新于 2022-02-02 08:30",
        regex_list=[
            r"(?P<Y>\d{4})-(?P<m>\d{2})-(?P<d>\d{2})",
            r"(?P<Y>\d{4})-(?P<m>\d{2})-(?P<d>\d{2}) (?P<H>\d{2}):(?P<M>\d{2})",
        ],
    ) == dt(2022, 2, 2, 8, 30)


@pytest.mark.parametrize(
    "text,expected",
    [
        ("2022年02月02日 02:02", dt(2022, 2, 2, 2, 2)),
        ("发布于：2022/02/02 02:02:02", dt(2022, 2, 2, 2, 2, 2)),
    ],
)
def test_extract_accurately_still_extracts_exact_time(text, expected):
    assert parse(text, extract_accurately=True) == expected


def test_translate_func_is_applied_before_parsing():
    assert parse(
        "本地文本", translate_func=lambda s: "2022-02-02"
    ) == dt(2022, 2, 2)


def test_parse_by_regex_timestamp():
    assert parse_by_regex("1643738522") == dt(2022, 2, 2, 2, 2, 2)
    assert parse_by_regex("1643738522000") == dt(2022, 2, 2, 2, 2, 2)


def test_parse_by_regex_bad_lang_returns_none():
    assert parse_by_regex("2022-02-02", langs=["not-a-lang"]) is None
