# -*- coding: utf-8 -*-

import datetime

import pytest

from gggdtparser import parse
from gggdtparser import parse_by_format


dt = datetime.datetime
UTC = datetime.timezone.utc
TZ8 = datetime.timezone(datetime.timedelta(hours=8))
TZ0530 = datetime.timezone(datetime.timedelta(hours=5, minutes=30))


@pytest.mark.parametrize(
    "text,expected",
    [
        ("2022-02-02T02:02:02+08:00",
         dt(2022, 2, 2, 2, 2, 2, tzinfo=TZ8)),
        ("2022-02-02T02:02:02Z",
         dt(2022, 2, 2, 2, 2, 2, tzinfo=UTC)),
        ("2022-02-02 02:02:02 +0530",
         dt(2022, 2, 2, 2, 2, 2, tzinfo=TZ0530)),
        ("2022-02-02 02:02:02 UTC",
         dt(2022, 2, 2, 2, 2, 2, tzinfo=UTC)),
    ],
)
def test_preserve_offset(text, expected):
    assert parse(text, timezone=False) == expected


def test_convert_offset_to_target_timezone():
    result = parse("2022-02-02T02:02:02+08:00", timezone=UTC)
    assert result == dt(2022, 2, 1, 18, 2, 2, tzinfo=UTC)
    assert result.tzinfo is UTC


@pytest.mark.parametrize(
    "text,langs,expected",
    [
        ("Wed, 02 Feb 2022 14:30:20 +0530", ["en"],
         dt(2022, 2, 2, 14, 30, 20, tzinfo=TZ0530)),
        ("2 Aug 2022 02:02:02 +0530", ["en"],
         dt(2022, 8, 2, 2, 2, 2, tzinfo=TZ0530)),
        ("Sat, 05 Feb 2022 18:33:00 GMT", ["en"],
         dt(2022, 2, 5, 18, 33, tzinfo=UTC)),
        ("2022-02-02T02:02:02.123+08:00", [],
         dt(2022, 2, 2, 2, 2, 2, 123000, tzinfo=TZ8)),
        ("2022-02-02T02:02:02,123+08:00", [],
         dt(2022, 2, 2, 2, 2, 2, 123000, tzinfo=TZ8)),
        ("2022-02-02T02:02:02.123Z", [],
         dt(2022, 2, 2, 2, 2, 2, 123000, tzinfo=UTC)),
        ("2022-02-02T02:02:02.1234567+08:00", [],
         dt(2022, 2, 2, 2, 2, 2, 123456, tzinfo=TZ8)),
    ],
)
def test_preserve_offset_for_rfc822_and_fraction(text, langs, expected):
    assert parse(text, langs=langs, timezone=False) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        ("2022-02-02T02:02:02z",
         dt(2022, 2, 2, 2, 2, 2, tzinfo=UTC)),
        ("2022-02-02 02:02:02 utc",
         dt(2022, 2, 2, 2, 2, 2, tzinfo=UTC)),
        ("2022-02-02 02:02:02 gmt",
         dt(2022, 2, 2, 2, 2, 2, tzinfo=UTC)),
        ("2022-02-02T02:02:02+08:00",
         dt(2022, 2, 2, 2, 2, 2, tzinfo=TZ8)),
    ],
)
def test_preserve_offset_case_insensitive(text, expected):
    assert parse(text, timezone=False) == expected


def test_attach_timezone_without_offset():
    result = parse("2022-02-02 02:02", timezone=TZ8)
    assert result == dt(2022, 2, 2, 2, 2, tzinfo=TZ8)


def test_timestamp_with_target_timezone():
    timestamp = 1643738522
    expected = datetime.datetime.fromtimestamp(timestamp, UTC)
    assert parse(str(timestamp), timezone=UTC) == expected
    assert parse(str(timestamp * 1000), timezone=UTC) == expected


def test_parse_by_format_keeps_and_converts_offset():
    aware = parse_by_format(
        "2022-02-02T02:02:02+08:00", ["%Y-%m-%dT%H:%M:%S%z"])
    assert aware == dt(2022, 2, 2, 2, 2, 2, tzinfo=TZ8)
    converted = parse_by_format(
        "2022-02-02T02:02:02+08:00",
        ["%Y-%m-%dT%H:%M:%S%z"], timezone=UTC)
    assert converted == dt(2022, 2, 1, 18, 2, 2, tzinfo=UTC)


def test_parse_by_format_with_offset_string_target():
    result = parse_by_format(
        "2022-02-02 02:02", ["%Y-%m-%d %H:%M"], timezone="+08:00")
    assert result == dt(2022, 2, 2, 2, 2, tzinfo=TZ8)


def test_timezone_boundary_checks():
    assert parse(
        "2022-02-02T02:02:02+00:00", timezone=False,
        max_datetime=dt(2022, 2, 2, 2, 2, 3),
    ) == dt(2022, 2, 2, 2, 2, 2, tzinfo=UTC)
    assert parse(
        "2022-02-02T02:02:02+00:00", timezone=False,
        min_datetime=dt(2022, 2, 2, 2, 2, 1),
    ) == dt(2022, 2, 2, 2, 2, 2, tzinfo=UTC)


def test_invalid_timezone_argument():
    with pytest.raises(ValueError):
        parse("2022-02-02", timezone="Mars/Olympus_Mons")
    with pytest.raises(ValueError):
        parse("2022-02-02", timezone="+25:00")
    with pytest.raises(ValueError):
        parse("2022-02-02", timezone=+9999)


def test_parse_iana_timezone_name():
    try:
        from zoneinfo import ZoneInfo

        tz = ZoneInfo("Asia/Shanghai")
    except Exception:
        pytest.skip("IANA tzdata not available")
    result = parse("2022-02-02 02:02", timezone="Asia/Shanghai")
    assert result == dt(2022, 2, 2, 2, 2, tzinfo=tz)
