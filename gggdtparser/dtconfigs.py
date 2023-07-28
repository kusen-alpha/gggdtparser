#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/3/24
import copy
import os
import glob
import importlib
import re

from .utils import get_sort_dict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

STRING_DATETIME_CLEAR_REGEX = [
    re.compile(r'\n+'),
    re.compile(r'(\r\n)+'),
    re.compile(r' {2,}')
]
LANG_MAPPING = {
    # 英语
    "en": "en",
    # 中文
    "zh": "zh",
    "zh-CN": "zh",
    "zh-CHS": "zh",
    # 繁体/中国台湾
    "cht": "cht",
    "zh-TW": "cht",
    "zh-CHT": "cht",
    # 德语
    "de": "de",
    # 法语
    "fra": "fra",
    "fr": "fr",
    # 瑞典语
    "swe": 'swe',
    "sv": 'sv',
    # 越南语
    "vie": 'vie',
    "vi": 'vi',
    # 阿塞拜疆语
    'az': 'az',
    # 俄语
    "ru": "ru",
    # 西班牙语
    "spa": "es",
    "es": "es",
    # 索马里语
    "so": "so",
    # 马拉地语
    "mr": "mr",
    "mar": "mr",
    # 乌克兰语
    "uk": "uk",
    # 斯瓦希里语
    "sw": "sw",
    # 土耳其语
    "tr": "tr",
    # 吉尔吉斯语
    "ky": "ky",
    # 乌尔都语
    "ur": "ur",
    # 印尼语
    "id": "_id",
    # 卢旺达语
    "rw": "rw",
    # 僧伽罗语
    "si": "si",
    # 塔吉克语
    "tg": "tg",
    # 印地语
    "hi": "hi",
    # 日语
    "ja": 'ja'
}

TRANSLATE_LANGS = [
    # 阿拉伯语
    'ara',
    'ar',
    # 泰语
    'th'
]

_LANG_LIST_SORT = ['default', 'en', 'zh', 'zht', 'de', 'fra', 'swe',
                   'vie', 'ru', 'es', 'so', 'mr', 'az', "uk", 'sw',
                   'tr', 'ky', 'ur', '_id', 'rw', 'si', 'tg', 'hi',
                   'ja'
                   ]


def compile_regex(regex, flags=0):
    return re.compile(regex, flags)


def compile_regex_list(regex_list, flags=0):
    return [compile_regex(regex, flags) for regex in regex_list]


_LANG_DIR = os.path.join(BASE_DIR, 'langs')
_LANG_FILES = glob.glob(_LANG_DIR + '/*.py')
_LANG_FILES = [filename for filename in _LANG_FILES if
               '__init__' not in filename]
LANG_SUB_TRANSLATE = {}
LANG_ACCURATE_REGEX_LIST = {}
LANG_FUZZY_REGEX_LIST = {}
for lang_file in _LANG_FILES:
    lang = os.path.basename(lang_file).replace('.py', '')
    module_name = 'gggdtparser.langs.' + lang
    module = importlib.import_module(module_name)
    if hasattr(module, 'SUB_TRANSLATE'):
        sub_list = []
        for sub in getattr(module, 'SUB_TRANSLATE'):
            sub_list.append((compile_regex(sub[0]), sub[1]))
        LANG_SUB_TRANSLATE[lang] = sub_list
    if hasattr(module, 'ACCURATE_REGEX_LIST'):
        LANG_ACCURATE_REGEX_LIST[lang] = compile_regex_list(getattr(
            module, 'ACCURATE_REGEX_LIST'), flags=re.M | re.I | re.S)
    if hasattr(module, 'FUZZY_REGEX_LIST'):
        LANG_FUZZY_REGEX_LIST[lang] = compile_regex_list(getattr(
            module, 'FUZZY_REGEX_LIST'), flags=re.M | re.I | re.S)

LANG_ACCURATE_REGEX_LIST = get_sort_dict(
    LANG_ACCURATE_REGEX_LIST, _LANG_LIST_SORT)
LANG_FUZZY_REGEX_LIST = get_sort_dict(
    LANG_FUZZY_REGEX_LIST, _LANG_LIST_SORT)

_SUB_LANG_LIST_SORT = copy.deepcopy(_LANG_LIST_SORT)
(_SUB_LANG_LIST_SORT[0], _SUB_LANG_LIST_SORT[-1]) = (
    _SUB_LANG_LIST_SORT[-1], _SUB_LANG_LIST_SORT[0])
LANG_SUB_TRANSLATE = get_sort_dict(LANG_SUB_TRANSLATE, _SUB_LANG_LIST_SORT)
