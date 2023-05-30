# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/4/26


def get_sort_dict(d, sort_list=None):
    """
    字典排序
    :param d:
    :param sort_list:
    :return:
    """
    if not sort_list:
        return d
    return {k: d[k] for k in sort_list if k in d} | {k: d[
        k] for k in d if k not in sort_list}
