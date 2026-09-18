# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/5/16

"""
日语
"""

ACCURATE_REGEX_LIST = [
]

SUB_TRANSLATE = [
    (r'\(月\)|\(火\)|\(水\)|\(木\)|\(金\)|\(土\)|\(日\)', ''),
    (r'か', '个'),
    (r"令和\s*(\d+)年", lambda m: "%s年" % (2018 + int(m.group(1)))),
    (r"平成\s*(\d+)年", lambda m: "%s年" % (1988 + int(m.group(1)))),
    (r"昭和\s*(\d+)年", lambda m: "%s年" % (1925 + int(m.group(1)))),
    (r"大正\s*(\d+)年", lambda m: "%s年" % (1911 + int(m.group(1)))),
]

FUZZY_REGEX_LIST = [
]
