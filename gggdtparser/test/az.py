# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/4/20

"""
阿塞拜疆语
"""

import datetime

now = datetime.datetime.now()
TEST_STRING_DATETIME = {
    '2 saat əvvəl': {
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
    }
}
