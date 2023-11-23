# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/4/26
import datetime
import sys


def get_sort_dict(d, sort_list=None):
    """
    字典排序
    :param d:
    :param sort_list:
    :return:
    """
    if not sort_list:
        return d
    if sys.version_info >= (3, 9):
        return {k: d[k] for k in sort_list if k in d} | {k: d[
            k] for k in d if k not in sort_list}
    else:
        _d = {k: d[k] for k in sort_list if k in d}
        _d.update({k: d[k] for k in d if k not in sort_list})
        return _d


def s2dt(s, format_list):
    for _format in format_list:
        try:
            return datetime.datetime.strptime(s, _format)
        except ValueError:
            continue
