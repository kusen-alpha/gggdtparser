# -*- coding:utf-8 -*-
"""Non-Gregorian calendar conversions shared by language modules.

These helpers convert civil/tabular Hijri, ISO week and ordinal day notations
into Gregorian dates so the parser only works with one calendar.
"""

import datetime


def iso_week_to_gregorian(year, week, weekday):
    """Convert ISO 8601 year/week/weekday (Monday=1) to a Gregorian date."""
    if 1 <= int(week) <= 53 and 1 <= int(weekday) <= 7:
        try:
            return datetime.date.fromisocalendar(
                int(year), int(week), int(weekday))
        except ValueError:
            return None
    return None


def ordinal_day_to_month_day(year, day_of_year):
    """Convert day-of-year to (month, day), or None when out of range."""
    year = int(year)
    try:
        date_value = datetime.date(year, 1, 1) + datetime.timedelta(
            days=int(day_of_year) - 1)
    except (ValueError, OverflowError):
        return None
    if date_value.year != year:
        return None
    return date_value.month, date_value.day


def hijri_to_gregorian(hy, hm, hd):
    """Civil/tabular Islamic (Hijri) calendar date to Gregorian date."""
    hy, hm, hd = int(hy), int(hm), int(hd)
    if not 1 <= hm <= 12:
        return None
    month_lengths = (30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30,
                     30 if (11 * hy + 14) % 30 < 11 else 29)
    if not 1 <= hd <= month_lengths[hm - 1]:
        return None
    days = (hy - 1) * 10631 // 30 + sum(month_lengths[:hm - 1]) + hd - 1
    jdn = days + 1948440
    return datetime.date.fromordinal(jdn - 1721425)
