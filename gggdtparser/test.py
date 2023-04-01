#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/3/24


import datetime
from .dtparser import parse
from .dtparser import check


def test(test_string_datetime):
    for string_datetime, configs in test_string_datetime.items():
        for mode, check_dt in configs.items():
            accurately = True
            if mode == 'accurately':
                pass
            elif mode == 'un_accurately':
                accurately = False
            else:
                continue
            result = parse(string_datetime, accurately=accurately,
                           max_datetime=datetime.datetime(year=2030,month=1,
                                                          day=1))
            check_result = check(result, check_dt)
            if not check_result:
                print('字符串时间：%s | 解析结果：%s | 严格模式：%s | 预期效果：%s | 验证结果：%s' % (
                    string_datetime, result, accurately, check_dt, check_result))


now = datetime.datetime.now()
HAS_TEST_STRING_DATETIME = {
    '1643738522': {
        'accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=2, minute=2, second=2),
        'un_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=2, minute=2, second=2),
    },
    '1643738522000': {
        'accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=2, minute=2, second=2),
        'un_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=2, minute=2, second=2),
    },
    '2022-02-02T02:02:02+00:00': {
        'accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=2, minute=2, second=2),
        'un_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=2, minute=2, second=2),
    },
    '2022年02月02日 02:02:02': {
        'accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=2, minute=2, second=2),
        'un_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=2, minute=2, second=2),
    },
    '2022年02月02日 02:02': {
        'accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=2, minute=2),
        'un_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=2, minute=2, second=now.second),
    },
    '2022-02-02 02:02': {
        'accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=2, minute=2),
        'un_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=2, minute=2, second=now.second),
    },
    '2022年02月02日 02': {
        'accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=2),
        'un_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=2, minute=now.minute, second=now.second),
    },
    '2022年02月02日': {
        'accurately': datetime.datetime(
            year=2022, month=2, day=2, ),
        'un_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=now.hour, minute=now.minute, second=now.second),
    },
    '2022/02/02': {
        'accurately': datetime.datetime(
            year=2022, month=2, day=2, ),
        'un_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=now.hour, minute=now.minute, second=now.second),
    },
    '20220202': {
        'accurately': datetime.datetime(
            year=2022, month=2, day=2, ),
        'un_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=now.hour, minute=now.minute, second=now.second),
    },
    '2022.02.02': {
        'accurately': datetime.datetime(
            year=2022, month=2, day=2, ),
        'un_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=now.hour, minute=now.minute, second=now.second),
    },
    '二零二二年二月二日': {
        'accurately': datetime.datetime(
            year=2022, month=2, day=2, ),
        'un_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=now.hour, minute=now.minute, second=now.second),
    },
    '2022/0202': {
        'accurately': datetime.datetime(
            year=2022, month=2, day=2, hour=0,
            minute=0, second=0),
        'un_accurately': datetime.datetime(
            year=2022, month=2, day=2, hour=now.hour,
            minute=now.minute, second=now.second)
    },
    '2022年02月': {
        'accurately': datetime.datetime(
            year=2022, month=2, day=1),
        'un_accurately': datetime.datetime(
            year=2022, month=2, day=now.day,
            hour=now.hour, minute=now.minute, second=now.second),
    },
    '2022/2': {
        'accurately': datetime.datetime(
            year=2022, month=2, day=1),
        'un_accurately': datetime.datetime(
            year=2022, month=2, day=now.day,
            hour=now.hour, minute=now.minute, second=now.second),
    },
    '2022.2': {
        'accurately': datetime.datetime(
            year=2022, month=2, day=1),
        'un_accurately': datetime.datetime(
            year=2022, month=2, day=now.day,
            hour=now.hour, minute=now.minute, second=now.second),
    },
    '2022年': {
        'accurately': datetime.datetime(
            year=2022, month=1, day=1),
        'un_accurately': datetime.datetime(
            year=2022, month=now.month, day=now.day,
            hour=now.hour, minute=now.minute, second=now.second),
    },
    '02月02日 02:02:02': {
        'accurately': datetime.datetime(
            year=now.year, month=2, day=2, hour=2,
            minute=2, second=2),
        'un_accurately': datetime.datetime(
            year=now.year, month=2, day=2, hour=2,
            minute=2, second=2),
    },
    '02月02日 02:02': {
        'accurately': datetime.datetime(
            year=now.year, month=2, day=2, hour=2,
            minute=2, second=0),
        'un_accurately': datetime.datetime(
            year=now.year, month=2, day=2, hour=2,
            minute=2, second=now.second),
    },
    '02/02 02:02': {
        'accurately': datetime.datetime(
            year=now.year, month=2, day=2, hour=2,
            minute=2, second=0),
        'un_accurately': datetime.datetime(
            year=now.year, month=2, day=2, hour=2,
            minute=2, second=now.second)
    },
    '02月02日 02': {
        'accurately': datetime.datetime(
            year=now.year, month=2, day=2, hour=2,
            minute=0, second=0),
        'un_accurately': datetime.datetime(
            year=now.year, month=2, day=2, hour=2,
            minute=now.minute, second=now.second),
    },
    '02月02日': {
        'accurately': datetime.datetime(
            year=now.year, month=2, day=2, hour=0,
            minute=0, second=0),
        'un_accurately': datetime.datetime(
            year=now.year, month=2, day=2, hour=now.hour,
            minute=now.minute, second=now.second),
    },
    '02-02': {
        'accurately': datetime.datetime(
            year=now.year, month=2, day=2, hour=0,
            minute=0, second=0),
        'un_accurately': datetime.datetime(
            year=now.year, month=2, day=2, hour=now.hour,
            minute=now.minute, second=now.second),
    },
    '2/2': {
        'accurately': datetime.datetime(
            year=now.year, month=2, day=2, hour=0,
            minute=0, second=0),
        'un_accurately': datetime.datetime(
            year=now.year, month=2, day=2, hour=now.hour,
            minute=now.minute, second=now.second)
    },
    '02月': {
        'accurately': datetime.datetime(
            year=now.year, month=2, day=1, hour=0,
            minute=0, second=0),
        'un_accurately': datetime.datetime(
            year=now.year, month=2, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second),
    },
    '02:02:02': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=2),
        'un_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=2),
    },
    '02:02': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=0),
        'un_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=now.second),
    },
    '前天': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=0,
            minute=0, second=0) - datetime.timedelta(days=2),
        'un_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) - datetime.timedelta(
            days=2),
    },
    '前天02:02:02': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=2) - datetime.timedelta(days=2),
        'un_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=2) - datetime.timedelta(days=2),
    },
    '前天02:02': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=0) - datetime.timedelta(days=2),
        'un_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=now.second) - datetime.timedelta(days=2),
    },
    '前天02': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=0, second=0) - datetime.timedelta(days=2),
        'un_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=now.minute, second=now.second) - datetime.timedelta(
            days=2),
    },
    '昨天': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=0,
            minute=0, second=0) - datetime.timedelta(days=1),
        'un_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) - datetime.timedelta(
            days=1),
    },
    '昨天02:02:02': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=2) - datetime.timedelta(days=1),
        'un_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=2) - datetime.timedelta(days=1),
    },
    '昨天02:02': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=0) - datetime.timedelta(days=1),
        'un_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=now.second) - datetime.timedelta(days=1),
    },
    '昨天02': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=0, second=0) - datetime.timedelta(days=1),
        'un_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=now.minute, second=now.second) - datetime.timedelta(
            days=1),
    },
    '今天': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=0,
            minute=0, second=0),
        'un_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second),
    },
    '今天02:02:02': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=2),
        'un_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=2),
    },
    '今天02:02': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=0),
        'un_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=now.second),
    },
    '今天02': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=0, second=0),
        'un_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=now.minute, second=now.second),
    },
    '刚刚': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) - datetime.timedelta(
            seconds=5),
        'un_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) - datetime.timedelta(
            seconds=5),
    },
    '2年前': {
        'accurately': datetime.datetime(
            year=now.year - 2, month=1, day=1),
        'un_accurately': (now-datetime.timedelta(days=365*3),
                          now-datetime.timedelta(days=365*2)),
    },
    '2月前': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day) -
                      datetime.timedelta(days=30 * 2),
        'un_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=30 * 3),
                          datetime.datetime(
                              year=now.year, month=now.month, day=now.day,
                              hour=now.hour,
                              minute=now.minute, second=now.second) -
                          datetime.timedelta(days=30 * 2)),
    },
    '2星期前': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day) -
                      datetime.timedelta(days=7 * 2),
        'un_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=7 * 3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=7 * 2)),
    },
    '2周前': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day) -
                      datetime.timedelta(days=7 * 2),
        'un_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=7 * 3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=7 * 2)),
    },
    '2天前': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day) -
                      datetime.timedelta(days=2),
        'un_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=2)),
    },
    '2小时前': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour) -
                      datetime.timedelta(hours=2),
        'un_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(hours=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(hours=2)),
    },
    '2分钟前': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute) -
                      datetime.timedelta(minutes=2),
        'un_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(minutes=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(minutes=2)),
    },
    '2秒前': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                      datetime.timedelta(seconds=2),
        'un_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(seconds=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(seconds=2)),
    },
    '2年内': {
        'accurately': datetime.datetime(
            year=now.year - 2, month=1, day=1),
        'un_accurately': (now-datetime.timedelta(days=365*2),
                          now-datetime.timedelta(days=365*1)),
    },
    '2月内': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day) -
                      datetime.timedelta(days=30 * 2),
        'un_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=30 * 2),
                          datetime.datetime(
                              year=now.year, month=now.month, day=now.day,
                              hour=now.hour,
                              minute=now.minute, second=now.second) -
                          datetime.timedelta(days=30 * 1)),
    },
    '2星期内': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day) -
                      datetime.timedelta(days=7 * 2),
        'un_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=7 * 2), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=7 * 1)),
    },
    '2周内': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day) -
                      datetime.timedelta(days=7 * 2),
        'un_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=7 * 2), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=7 * 1)),
    },
    '2天内': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day) -
                      datetime.timedelta(days=2),
        'un_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=2), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=1)),
    },
    '2小时内': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour) -
                      datetime.timedelta(hours=2),
        'un_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(hours=2), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(hours=1)),
    },
    '2分钟内': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute) -
                      datetime.timedelta(minutes=2),
        'un_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(minutes=2), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(minutes=1)),
    },
    '2秒内': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                      datetime.timedelta(seconds=2),
        'un_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(seconds=2), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(seconds=1)),
    },
    # 中国台湾繁体
    '民國111年02月02日': {
        'accurately': datetime.datetime(
            year=2022, month=2, day=2, hour=0,
            minute=0, second=0),
        'un_accurately': datetime.datetime(
            year=2022, month=2, day=2, hour=now.hour,
            minute=now.minute, second=now.second)
    },
    '2小時前': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour) -
                      datetime.timedelta(hours=2),
        'un_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(hours=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(hours=2)),
    },
    '2分鐘前': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute) -
                      datetime.timedelta(minutes=2),
        'un_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(minutes=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(minutes=2)),
    },
    # 英语
    'Thu February 02 02:02:02 2022 UTC': {
        'accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=2, minute=2, second=2),
        'un_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=2, minute=2, second=2),
    },
    'Thu February 02 02:02:02 2022': {
        'accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=2, minute=2, second=2),
        'un_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=2, minute=2, second=2),
    },
    'Feb 02, 2022 02:02 pm': {
        'accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=14, minute=2),
        'un_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=14, minute=2,
                                           second=now.second),
    },
    'Feb 02, 2022 02:02': {
        'accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=2, minute=2),
        'un_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=2, minute=2,
                                           second=now.second),
    },
    'Mon, Feb 02, 2022 - 02:02 AM': {
        'accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=2, minute=2),
        'un_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=2, minute=2,
                                           second=now.second),
    },
    '02 Feb 2022 | 02:02 AM': {
        'accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=2, minute=2),
        'un_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=2, minute=2,
                                           second=now.second),
    },
    '02:02, 2 Feb 2022': {
        'accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=2, minute=2),
        'un_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=2, minute=2,
                                           second=now.second),
    },
    '02 Feb 2022 at 2:02am': {
        'accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=2, minute=2),
        'un_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=2, minute=2,
                                           second=now.second),
    },
    'February 2, 2022': {
        'accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=0, minute=0, second=0),
        'un_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=now.hour, minute=now.minute,
                                           second=now.second),
    },
    'Feb. 02, 2022': {
        'accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=0, minute=0, second=0),
        'un_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=now.hour, minute=now.minute,
                                           second=now.second),
    },
    '2 February 2022': {
        'accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=0, minute=0, second=0),
        'un_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=now.hour, minute=now.minute,
                                           second=now.second),
    },
    'Feb 2': {
        'accurately': datetime.datetime(year=now.year, month=2, day=2,
                                        hour=0, minute=0, second=0),
        'un_accurately': datetime.datetime(year=now.year, month=2, day=2,
                                           hour=now.hour, minute=now.minute,
                                           second=now.second),
    },
    '2 years ago': {
        'accurately': datetime.datetime(
            year=now.year - 2, month=1, day=1),
        'un_accurately': (now-datetime.timedelta(days=365*3),
                          now-datetime.timedelta(days=365*2)),
    },
    '2 month ago': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day) -
                      datetime.timedelta(days=30 * 2),
        'un_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=30 * 3),
                          datetime.datetime(
                              year=now.year, month=now.month, day=now.day,
                              hour=now.hour,
                              minute=now.minute, second=now.second) -
                          datetime.timedelta(days=30 * 2)),
    },
    '2 weeks ago': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day) -
                      datetime.timedelta(days=7 * 2),
        'un_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=7 * 3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=7 * 2)),
    },
    '2 days ago': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day) -
                      datetime.timedelta(days=2),
        'un_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=2)),
    },
    '2h ago': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour) -
                      datetime.timedelta(hours=2),
        'un_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(hours=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(hours=2)),
    },
    '2 hours ago': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour) -
                      datetime.timedelta(hours=2),
        'un_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(hours=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(hours=2)),
    },
    '2 minutes ago': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute) -
                      datetime.timedelta(minutes=2),
        'un_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(minutes=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(minutes=2)),
    },
    '2m ago': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute) -
                      datetime.timedelta(minutes=2),
        'un_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(minutes=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(minutes=2)),
    },
    '2 seconds ago': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                      datetime.timedelta(seconds=2),
        'un_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(seconds=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(seconds=2)),
    },
    # 法语
    '02/02/22 à 02h02': {
        'accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=2, minute=2),
        'un_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=2, minute=2, second=now.second),
    },
    '02/02/2022 à 02h02': {
        'accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=2, minute=2),
        'un_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=2, minute=2, second=now.second),
    },
    '02 février 2022 à 02h02': {
        'accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=2, minute=2),
        'un_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=2, minute=2, second=now.second),
    },
    'aujourd’hui à 02h02': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day,
            hour=2, minute=2
        ),
        'un_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day,
            hour=2, minute=2, second=now.second
        ),
    },
    'à 02h02': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day,
            hour=2, minute=2
        ),
        'un_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day,
            hour=2, minute=2, second=now.second
        ),
    },
    'il y a 2 heures': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour) -
                      datetime.timedelta(hours=2),
        'un_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(hours=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(hours=2)),
    },
    '2 heure': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour) -
                      datetime.timedelta(hours=2),
        'un_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(hours=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(hours=2)),
    },
    'à l’instant': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) - datetime.timedelta(
            seconds=5),
        'un_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) - datetime.timedelta(
            seconds=5),
    },
    # 德语
    '02.02.2022, 02.02 Uhr': {
        'accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=2, minute=2),
        'un_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=2, minute=2, second=now.second),
    },
    '02.02.2022': {
        'accurately': datetime.datetime(
            year=2022, month=2, day=2),
        'un_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=now.hour, minute=now.minute, second=now.second),
    },
    '02. Februar 2022': {
        'accurately': datetime.datetime(
            year=2022, month=2, day=2, ),
        'un_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=now.hour, minute=now.minute, second=now.second),
    },
    # 越南语
    '2 phút trước': {
        'accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute) -
                      datetime.timedelta(minutes=2),
        'un_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(minutes=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(minutes=2)),
    },
}
if __name__ == '__main__':
    pass
