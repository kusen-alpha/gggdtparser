#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/11/23


__all__ = ['parse']

from . import dtparser

SEPS = (
    '至',
    '-'
)


def _parse(s, sep, start_format_list, end_format_list, start_regex_list,
           end_regex_list, base_datetime):
    start, end = None, None
    try:
        left, right = s.split(sep)
    except ValueError:
        if base_datetime:
            start = base_datetime
            end = dtparser.parse(
                s, end_format_list, end_regex_list,
                base_datetime=base_datetime)
        return start, end
    if left:
        start = dtparser.parse(
            left, start_format_list, start_regex_list,
            base_datetime=base_datetime)
    if right:
        end = dtparser.parse(
            right, end_format_list, end_regex_list,
            base_datetime=base_datetime)
    return start, end


def parse(s, seps=None, format_list=None, regex_list=None,
          base_datetime=None, ):
    """

    :param s:
    :param seps: 范围标识符
    :param format_list: 时间模板
        [(start, start, ....), (end, end, ....)]
    :param regex_list: 正则表达式
        [(start, start, ....), (end, end, ....)]
    :param base_datetime: 相对时间的基准，当起始时间没有解析到时，当做时间的范围的起始

    :return:
    """
    if not s:
        return None, None
    if not seps:
        seps = []
    start_format_list, end_format_list = format_list if format_list else (
        None, None)

    start_regex_list, end_regex_list = regex_list if regex_list else (
        None, None)
    for sep in seps:
        start, end = _parse(
            s, sep, start_format_list, end_format_list,
            start_regex_list, end_regex_list, base_datetime)
        if any([start, end]):
            return start, end
    for sep in SEPS:
        start, end = _parse(
            s, sep, start_format_list, end_format_list,
            start_regex_list, end_regex_list, base_datetime)
        if any([start, end]):
            return start, end
    return None, None


if __name__ == '__main__':
    print(parse('2022年10月1日至2023年10月1日',))
