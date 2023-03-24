#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/3/24
import datetime
from dtparser import parse


def check(dst_dt, check_dt):
    if isinstance(check_dt, datetime.datetime):
        return dst_dt == check_dt
    start_dt, end_dt = check_dt
    return start_dt <= dst_dt <= end_dt


def test(now):
    # 优先级：由全到简、由特征到无特征（分隔符、关键词）、由通用到特殊
    test_string_datetime = {
        '20000101': {
            'accurately': datetime.datetime(year=2000, month=1, day=1),
            'un_accurately': datetime.datetime(
                year=2000, month=1, day=1,
                hour=now.hour, minute=now.minute, second=now.second)
        },
        '2000/01/01': {
            'accurately': datetime.datetime(year=2000, month=1, day=1),
            'un_accurately': datetime.datetime(
                year=2000, month=1, day=1,
                hour=now.hour, minute=now.minute, second=now.second)
        },
        '2000年01月01日 01:01:01': {
            'accurately': datetime.datetime(
                year=2000, month=1, day=1, hour=1, minute=1, second=1),
            'un_accurately': datetime.datetime(
                year=2000, month=1, day=1, hour=1, minute=1, second=1)
        },
        '2000-01-01 01:01': {
            'accurately': datetime.datetime(
                year=2000, month=1, day=1, hour=1, minute=1),
            'un_accurately': datetime.datetime(
                year=2000, month=1, day=1, hour=1, minute=1, second=now.second)
        },
        '2000年01月01日': {
            'accurately': datetime.datetime(
                year=2000, month=1, day=1),
            'un_accurately': datetime.datetime(
                year=2000, month=1, day=1, hour=now.hour,
                minute=now.minute, second=now.second)
        },
        '2000年01月': {
            'accurately': datetime.datetime(
                year=2000, month=1, day=1),
            'un_accurately': datetime.datetime(
                year=2000, month=1, day=now.day, hour=now.hour,
                minute=now.minute, second=now.second)
        },
        '2000/1': {
            'accurately': datetime.datetime(
                year=2000, month=1, day=1),
            'un_accurately': datetime.datetime(
                year=2000, month=1, day=now.day, hour=now.hour,
                minute=now.minute, second=now.second)
        },
        '01-01': {
            'accurately': datetime.datetime(
                year=now.year, month=1, day=1),
            'un_accurately': datetime.datetime(
                year=now.year, month=1, day=1, hour=now.hour,
                minute=now.minute, second=now.second)
        },
        'xxx1天前xxx': {
            'accurately': datetime.datetime(
                year=now.year, month=now.month, day=now.day - 1),
            'un_accurately': (now - datetime.timedelta(days=2),
                              now - datetime.timedelta(days=1))
        },
        '民国99年': {
            'accurately': datetime.datetime(
                year=2010, month=1, day=1),
            'un_accurately': (datetime.datetime(
                year=2010, month=1, day=1), datetime.datetime(
                year=2011, month=1, day=1))
        },
        'February 02, 2023': {
            'accurately': datetime.datetime(
                year=2023, month=2, day=2),
            'un_accurately': datetime.datetime(
                year=2023, month=2, day=2, hour=now.hour, minute=now.minute,
                second=now.second
            )
        },
    }

    for string_datetime, configs in test_string_datetime.items():
        for mode, check_dt in configs.items():
            accurately = True
            if mode == 'accurately':
                pass
            elif mode == 'un_accurately':
                accurately = False
            else:
                continue
            result = parse(string_datetime, accurately=accurately)
            check_result = check(result, check_dt)
            print('字符串时间：%s | 解析结果：%s | 严格模式：%s | 预期效果：%s | 验证结果：%s' % (
                string_datetime, result, accurately, check_dt, check_result))


if __name__ == '__main__':
    test(datetime.datetime.now())
