# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/4/18


import datetime
from ..dtparser import parse
from ..dtparser import check


def test(test_string_datetime):
    for string_datetime, configs in test_string_datetime.items():
        for mode, check_dt in configs.items():
            result_accurately = True
            if mode == 'result_accurately':
                pass
            elif mode == 'un_result_accurately':
                result_accurately = False
            else:
                continue
            result = parse(string_datetime, result_accurately=result_accurately,
                           max_datetime=datetime.datetime(year=2030, month=1,
                                                          day=1))
            check_result = check(result, check_dt)
            if not check_result:
                print('字符串时间：%s | 解析结果：%s | 严格模式：%s | 预期效果：%s | 验证结果：%s' % (
                    string_datetime, result, result_accurately, check_dt,
                    check_result))


now = datetime.datetime.now()
HAS_TEST_STRING_DATETIME = {
    '1643738522': {
        'result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=2, minute=2, second=2),
        'un_result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=2, minute=2, second=2),
    },
    '1643738522000': {
        'result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=2, minute=2, second=2),
        'un_result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=2, minute=2, second=2),
    },
    '2022-02-02T02:02:02+00:00': {
        'result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=2, minute=2, second=2),
        'un_result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=2, minute=2, second=2),
    },
    '2022年02月02日 02:02:02': {
        'result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=2, minute=2, second=2),
        'un_result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=2, minute=2, second=2),
    },
    '2022年02月02日 02:02': {
        'result_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=2, minute=2),
        'un_result_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=2, minute=2, second=now.second),
    },
    '2022年2月02日，上午02:02': {
        'result_accurately': datetime.datetime(
            year=2022, month=2, day=2, hour=2,
            minute=2, second=0),
        'un_result_accurately': datetime.datetime(
            year=2022, month=2, day=2, hour=2,
            minute=2, second=now.second)
    },
    '2022-02-02 02:02': {
        'result_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=2, minute=2),
        'un_result_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=2, minute=2, second=now.second),
    },
    '2022年02月02日 02': {
        'result_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=2),
        'un_result_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=2, minute=now.minute, second=now.second),
    },
    '2022年02月02日': {
        'result_accurately': datetime.datetime(
            year=2022, month=2, day=2, ),
        'un_result_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=now.hour, minute=now.minute, second=now.second),
    },
    '2022/02/02': {
        'result_accurately': datetime.datetime(
            year=2022, month=2, day=2, ),
        'un_result_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=now.hour, minute=now.minute, second=now.second),
    },
    '20220202': {
        'result_accurately': datetime.datetime(
            year=2022, month=2, day=2, ),
        'un_result_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=now.hour, minute=now.minute, second=now.second),
    },
    '2022.02.02': {
        'result_accurately': datetime.datetime(
            year=2022, month=2, day=2, ),
        'un_result_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=now.hour, minute=now.minute, second=now.second),
    },
    '二零二二年二月二日': {
        'result_accurately': datetime.datetime(
            year=2022, month=2, day=2, ),
        'un_result_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=now.hour, minute=now.minute, second=now.second),
    },
    '2022/0202': {
        'result_accurately': datetime.datetime(
            year=2022, month=2, day=2, hour=0,
            minute=0, second=0),
        'un_result_accurately': datetime.datetime(
            year=2022, month=2, day=2, hour=now.hour,
            minute=now.minute, second=now.second)
    },
    '2022 02月02日': {
        'result_accurately': datetime.datetime(
            year=2022, month=2, day=2, ),
        'un_result_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=now.hour, minute=now.minute, second=now.second),
    },
    '2022年02月': {
        'result_accurately': datetime.datetime(
            year=2022, month=2, day=1),
        'un_result_accurately': datetime.datetime(
            year=2022, month=2, day=now.day,
            hour=now.hour, minute=now.minute, second=now.second),
    },
    '2022/2': {
        'result_accurately': datetime.datetime(
            year=2022, month=2, day=1),
        'un_result_accurately': datetime.datetime(
            year=2022, month=2, day=now.day,
            hour=now.hour, minute=now.minute, second=now.second),
    },
    '2022.2': {
        'result_accurately': datetime.datetime(
            year=2022, month=2, day=1),
        'un_result_accurately': datetime.datetime(
            year=2022, month=2, day=now.day,
            hour=now.hour, minute=now.minute, second=now.second),
    },
    '2022年': {
        'result_accurately': datetime.datetime(
            year=2022, month=1, day=1),
        'un_result_accurately': datetime.datetime(
            year=2022, month=now.month, day=now.day,
            hour=now.hour, minute=now.minute, second=now.second),
    },
    '02月02日 02:02:02': {
        'result_accurately': datetime.datetime(
            year=now.year, month=2, day=2, hour=2,
            minute=2, second=2),
        'un_result_accurately': datetime.datetime(
            year=now.year, month=2, day=2, hour=2,
            minute=2, second=2),
    },
    '02月02日 02:02': {
        'result_accurately': datetime.datetime(
            year=now.year, month=2, day=2, hour=2,
            minute=2, second=0),
        'un_result_accurately': datetime.datetime(
            year=now.year, month=2, day=2, hour=2,
            minute=2, second=now.second),
    },
    '02/02 02:02': {
        'result_accurately': datetime.datetime(
            year=now.year, month=2, day=2, hour=2,
            minute=2, second=0),
        'un_result_accurately': datetime.datetime(
            year=now.year, month=2, day=2, hour=2,
            minute=2, second=now.second)
    },
    '02月02日 02': {
        'result_accurately': datetime.datetime(
            year=now.year, month=2, day=2, hour=2,
            minute=0, second=0),
        'un_result_accurately': datetime.datetime(
            year=now.year, month=2, day=2, hour=2,
            minute=now.minute, second=now.second),
    },
    '02月02日': {
        'result_accurately': datetime.datetime(
            year=now.year, month=2, day=2, hour=0,
            minute=0, second=0),
        'un_result_accurately': datetime.datetime(
            year=now.year, month=2, day=2, hour=now.hour,
            minute=now.minute, second=now.second),
    },
    '02-02': {
        'result_accurately': datetime.datetime(
            year=now.year, month=2, day=2, hour=0,
            minute=0, second=0),
        'un_result_accurately': datetime.datetime(
            year=now.year, month=2, day=2, hour=now.hour,
            minute=now.minute, second=now.second),
    },
    '2/2': {
        'result_accurately': datetime.datetime(
            year=now.year, month=2, day=2, hour=0,
            minute=0, second=0),
        'un_result_accurately': datetime.datetime(
            year=now.year, month=2, day=2, hour=now.hour,
            minute=now.minute, second=now.second)
    },
    '02月': {
        'result_accurately': datetime.datetime(
            year=now.year, month=2, day=1, hour=0,
            minute=0, second=0),
        'un_result_accurately': datetime.datetime(
            year=now.year, month=2, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second),
    },
    '02:02:02': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=2),
        'un_result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=2),
    },
    '02:02': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=0),
        'un_result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=now.second),
    },
    '前天': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=0,
            minute=0, second=0) - datetime.timedelta(days=2),
        'un_result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) - datetime.timedelta(
            days=2),
    },
    '前天02:02:02': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=2) - datetime.timedelta(days=2),
        'un_result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=2) - datetime.timedelta(days=2),
    },
    '前天02:02': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=0) - datetime.timedelta(days=2),
        'un_result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=now.second) - datetime.timedelta(days=2),
    },
    '前天02': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=0, second=0) - datetime.timedelta(days=2),
        'un_result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=now.minute, second=now.second) - datetime.timedelta(
            days=2),
    },
    '昨天': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=0,
            minute=0, second=0) - datetime.timedelta(days=1),
        'un_result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) - datetime.timedelta(
            days=1),
    },
    '昨天02:02:02': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=2) - datetime.timedelta(days=1),
        'un_result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=2) - datetime.timedelta(days=1),
    },
    '昨天02:02': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=0) - datetime.timedelta(days=1),
        'un_result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=now.second) - datetime.timedelta(days=1),
    },
    '昨天02': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=0, second=0) - datetime.timedelta(days=1),
        'un_result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=now.minute, second=now.second) - datetime.timedelta(
            days=1),
    },
    '今天': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=0,
            minute=0, second=0),
        'un_result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second),
    },
    '今天02:02:02': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=2),
        'un_result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=2),
    },
    '今天02:02': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=0),
        'un_result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=2, second=now.second),
    },
    '今天02': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=0, second=0),
        'un_result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=2,
            minute=now.minute, second=now.second),
    },
    '刚刚': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) - datetime.timedelta(
            seconds=5),
        'un_result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) - datetime.timedelta(
            seconds=5),
    },
    '2年前': {
        'result_accurately': datetime.datetime(
            year=now.year - 2, month=1, day=1),
        'un_result_accurately': (now - datetime.timedelta(days=365 * 3),
                          now - datetime.timedelta(days=365 * 2)),
    },
    '2月前': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day) -
                      datetime.timedelta(days=30 * 2),
        'un_result_accurately': (datetime.datetime(
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
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day) -
                      datetime.timedelta(days=7 * 2),
        'un_result_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=7 * 3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=7 * 2)),
    },
    '2周前': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day) -
                      datetime.timedelta(days=7 * 2),
        'un_result_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=7 * 3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=7 * 2)),
    },
    '2天前': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day) -
                      datetime.timedelta(days=2),
        'un_result_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=2)),
    },
    '2小时前': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour) -
                      datetime.timedelta(hours=2),
        'un_result_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(hours=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(hours=2)),
    },
    '2分钟前': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute) -
                      datetime.timedelta(minutes=2),
        'un_result_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(minutes=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(minutes=2)),
    },
    '2秒前': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                      datetime.timedelta(seconds=2),
        'un_result_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(seconds=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(seconds=2)),
    },
    '2年内': {
        'result_accurately': datetime.datetime(
            year=now.year - 2, month=1, day=1),
        'un_result_accurately': (now - datetime.timedelta(days=365 * 2),
                          now - datetime.timedelta(days=365 * 1)),
    },
    '2月内': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day) -
                      datetime.timedelta(days=30 * 2),
        'un_result_accurately': (datetime.datetime(
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
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day) -
                      datetime.timedelta(days=7 * 2),
        'un_result_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=7 * 2), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=7 * 1)),
    },
    '2周内': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day) -
                      datetime.timedelta(days=7 * 2),
        'un_result_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=7 * 2), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=7 * 1)),
    },
    '2天内': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day) -
                      datetime.timedelta(days=2),
        'un_result_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=2), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=1)),
    },
    '2小时内': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour) -
                      datetime.timedelta(hours=2),
        'un_result_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(hours=2), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(hours=1)),
    },
    '2分钟内': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute) -
                      datetime.timedelta(minutes=2),
        'un_result_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(minutes=2), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(minutes=1)),
    },
    '2秒内': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                      datetime.timedelta(seconds=2),
        'un_result_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(seconds=2), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(seconds=1)),
    },
    # 中国台湾繁体
    '民國111年02月02日': {
        'result_accurately': datetime.datetime(
            year=2022, month=2, day=2, hour=0,
            minute=0, second=0),
        'un_result_accurately': datetime.datetime(
            year=2022, month=2, day=2, hour=now.hour,
            minute=now.minute, second=now.second)
    },
    '111-02-02': {
        'result_accurately': datetime.datetime(
            year=2022, month=2, day=2, hour=0,
            minute=0, second=0),
        'un_result_accurately': datetime.datetime(
            year=2022, month=2, day=2, hour=now.hour,
            minute=now.minute, second=now.second)
    },
    '2小時前': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour) -
                      datetime.timedelta(hours=2),
        'un_result_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(hours=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(hours=2)),
    },
    '2分鐘前': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute) -
                      datetime.timedelta(minutes=2),
        'un_result_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(minutes=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(minutes=2)),
    },
    # 英语
    'Thu February 02 02:02:02 2022 UTC': {
        'result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=2, minute=2, second=2),
        'un_result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=2, minute=2, second=2),
    },
    'Thu February 02 02:02:02 2022': {
        'result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=2, minute=2, second=2),
        'un_result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=2, minute=2, second=2),
    },
    'Feb 02, 2022 02:02 pm': {
        'result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=14, minute=2),
        'un_result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=14, minute=2,
                                           second=now.second),
    },
    '02:02 PM EST, Sat February 02, 2022': {
            'result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                            hour=14, minute=2),
            'un_result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                               hour=14, minute=2,
                                               second=now.second),
    },
    'Feb 02, 2022 02:02': {
        'result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=2, minute=2),
        'un_result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=2, minute=2,
                                           second=now.second),
    },
    'Mon, Feb 02, 2022 - 02:02 AM': {
        'result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=2, minute=2),
        'un_result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=2, minute=2,
                                           second=now.second),
    },
    '02 Feb 2022 | 02:02 AM': {
        'result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=2, minute=2),
        'un_result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=2, minute=2,
                                           second=now.second),
    },
    '02:02, 2 Feb 2022': {
        'result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=2, minute=2),
        'un_result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=2, minute=2,
                                           second=now.second),
    },
    '02 Feb 2022 at 2:02am': {
        'result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=2, minute=2),
        'un_result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=2, minute=2,
                                           second=now.second),
    },
    'February 2, 2022': {
        'result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=0, minute=0, second=0),
        'un_result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=now.hour, minute=now.minute,
                                           second=now.second),
    },
    'Feb. 02, 2022': {
        'result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=0, minute=0, second=0),
        'un_result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=now.hour, minute=now.minute,
                                           second=now.second),
    },
    '2 February 2022': {
        'result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                        hour=0, minute=0, second=0),
        'un_result_accurately': datetime.datetime(year=2022, month=2, day=2,
                                           hour=now.hour, minute=now.minute,
                                           second=now.second),
    },
    'February 2022': {
            'result_accurately': datetime.datetime(year=2022, month=2, day=1,
                                            hour=0, minute=0, second=0),
            'un_result_accurately': datetime.datetime(year=2022, month=2, day=now.day,
                                               hour=now.hour, minute=now.minute,
                                               second=now.second),
    },
    'Feb 2': {
        'result_accurately': datetime.datetime(year=now.year, month=2, day=2,
                                        hour=0, minute=0, second=0),
        'un_result_accurately': datetime.datetime(year=now.year, month=2, day=2,
                                           hour=now.hour, minute=now.minute,
                                           second=now.second),
    },
    '2 years ago': {
        'result_accurately': datetime.datetime(
            year=now.year - 2, month=1, day=1),
        'un_result_accurately': (now - datetime.timedelta(days=365 * 3),
                          now - datetime.timedelta(days=365 * 2)),
    },
    '2 month ago': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day) -
                      datetime.timedelta(days=30 * 2),
        'un_result_accurately': (datetime.datetime(
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
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day) -
                      datetime.timedelta(days=7 * 2),
        'un_result_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=7 * 3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=7 * 2)),
    },
    '2 days ago': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day) -
                      datetime.timedelta(days=2),
        'un_result_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(days=2)),
    },
    '2h ago': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour) -
                      datetime.timedelta(hours=2),
        'un_result_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(hours=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(hours=2)),
    },
    '2 hours ago': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour) -
                      datetime.timedelta(hours=2),
        'un_result_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(hours=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(hours=2)),
    },
    '2 minutes ago': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute) -
                      datetime.timedelta(minutes=2),
        'un_result_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(minutes=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(minutes=2)),
    },
    '2m ago': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute) -
                      datetime.timedelta(minutes=2),
        'un_result_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(minutes=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(minutes=2)),
    },
    '2 seconds ago': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                      datetime.timedelta(seconds=2),
        'un_result_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(seconds=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(seconds=2)),
    },
    # 法语
    '02/02/22 à 02h02': {
        'result_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=2, minute=2),
        'un_result_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=2, minute=2, second=now.second),
    },
    '02/02/2022 à 02h02': {
        'result_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=2, minute=2),
        'un_result_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=2, minute=2, second=now.second),
    },
    '02 février 2022 à 02h02': {
        'result_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=2, minute=2),
        'un_result_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=2, minute=2, second=now.second),
    },
    'aujourd’hui à 02h02': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day,
            hour=2, minute=2
        ),
        'un_result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day,
            hour=2, minute=2, second=now.second
        ),
    },
    'à 02h02': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day,
            hour=2, minute=2
        ),
        'un_result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day,
            hour=2, minute=2, second=now.second
        ),
    },
    'il y a 2 heures': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour) -
                      datetime.timedelta(hours=2),
        'un_result_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(hours=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(hours=2)),
    },
    '2 heure': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour) -
                      datetime.timedelta(hours=2),
        'un_result_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(hours=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(hours=2)),
    },
    'à l’instant': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) - datetime.timedelta(
            seconds=5),
        'un_result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) - datetime.timedelta(
            seconds=5),
    },
    # 德语
    '02.02.2022, 02.02 Uhr': {
        'result_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=2, minute=2),
        'un_result_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=2, minute=2, second=now.second),
    },
    '02.02.2022': {
        'result_accurately': datetime.datetime(
            year=2022, month=2, day=2),
        'un_result_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=now.hour, minute=now.minute, second=now.second),
    },
    '02. Februar 2022': {
        'result_accurately': datetime.datetime(
            year=2022, month=2, day=2, ),
        'un_result_accurately': datetime.datetime(
            year=2022, month=2, day=2,
            hour=now.hour, minute=now.minute, second=now.second),
    },

}

# 越南语
HAS_TEST_STRING_DATETIME_VIE = {
    '2 phút trước': {
        'result_accurately': datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute) -
                      datetime.timedelta(minutes=2),
        'un_result_accurately': (datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(minutes=3), datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=now.hour,
            minute=now.minute, second=now.second) -
                          datetime.timedelta(minutes=2)),
    },
    '02 tháng 2 năm 2022': {
        'result_accurately': datetime.datetime(
            year=2022, month=2, day=2, hour=0,
            minute=0, second=0),
        'un_result_accurately': datetime.datetime(
            year=2022, month=2, day=2, hour=now.hour,
            minute=now.minute, second=now.second)
    },
}
if __name__ == '__main__':
    pass
