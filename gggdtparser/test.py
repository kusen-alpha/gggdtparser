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
            result = parse(string_datetime, accurately=accurately)
            check_result = check(result, check_dt)
            print('字符串时间：%s | 解析结果：%s | 严格模式：%s | 预期效果：%s | 验证结果：%s' % (
                string_datetime, result, accurately, check_dt, check_result))


if __name__ == '__main__':
    now = datetime.datetime.now()
    has_test_string_datetime = {
        '1643738522': {
            'accurately': datetime.datetime(year=2022, month=2, day=2,
                                            hour=2, minute=2, second=2),
            'un_accurately': datetime.datetime(year=2020, month=2, day=2,
                                               hour=2, minute=2, second=2),
        },
        '1643738522000': {
            'accurately': datetime.datetime(year=2022, month=2, day=2,
                                            hour=2, minute=2, second=2),
            'un_accurately': datetime.datetime(year=2020, month=2, day=2,
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
                year=now.year, month=1, day=1, hour=2,
                minute=2, second=2),
            'un_accurately': datetime.datetime(
                year=now.year, month=now.month, day=now.day, hour=2,
                minute=2, second=2),
        },
        '02:02': {
            'accurately': datetime.datetime(
                year=now.year, month=1, day=1, hour=2,
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
                minute=0, second=0) - datetime.timedelta(days=2),
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
            'un_accurately': (datetime.datetime(
                year=now.year - 3, month=now.month, day=now.day, hour=now.hour,
                minute=now.minute, second=now.second), datetime.datetime(
                year=now.year - 2, month=now.month, day=now.day, hour=now.hour,
                minute=now.minute, second=now.second)),
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
            'un_accurately': (datetime.datetime(
                year=now.year - 2, month=now.month, day=now.day, hour=now.hour,
                minute=now.minute, second=now.second), datetime.datetime(
                year=now.year - 1, month=now.month, day=now.day, hour=now.hour,
                minute=now.minute, second=now.second)),
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

    }
    test_string_datetime = {
        '03/18 11:08': {
            'accurately': datetime.datetime(
                year=now.year, month=now.month, day=now.day, hour=now.hour,
                minute=now.minute, second=now.second) - datetime.timedelta(
                seconds=10),
            'un_accurately': (datetime.datetime(
                year=now.year, month=now.month, day=now.day, hour=now.hour,
                minute=now.minute, second=now.second) -
                              datetime.timedelta(seconds=10), datetime.datetime(
                year=now.year, month=now.month, day=now.day, hour=now.hour,
                minute=now.minute, second=now.second) -
                              datetime.timedelta(seconds=9)),
        },
        # 'xxx1天内xxx': {
        #     'accurately': datetime.datetime(
        #         year=now.year, month=now.month, day=now.day - 1),
        #     'un_accurately': (now - datetime.timedelta(days=2),
        #                       now - datetime.timedelta(days=1))
        # },
        # '民国99年': {
        #     'accurately': datetime.datetime(
        #         year=2010, month=1, day=1),
        #     'un_accurately': (datetime.datetime(
        #         year=2010, month=1, day=1), datetime.datetime(
        #         year=2011, month=1, day=1))
        # },
        # 'February 02, 2023': {
        #     'accurately': datetime.datetime(
        #         year=2023, month=2, day=2),
        #     'un_accurately': datetime.datetime(
        #         year=2023, month=2, day=2, hour=now.hour, minute=now.minute,
        #         second=now.second
        #     )
        # },
    }
    test(test_string_datetime, )
    # test(has_test_string_datetime, )
