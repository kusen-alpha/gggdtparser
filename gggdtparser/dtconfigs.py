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
    "zh-cn": "zh",
    "zh-chs": "zh",
    "zh-hans": "zh",
    # 繁体/中国台湾
    "cht": "zht",
    "zht": "zht",
    "zh-tw": "zht",
    "zh-cht": "zht",
    "zh-hant": "zht",
    # 德语
    "de": "de",
    # 法语
    "fra": "fra",
    "fr": "fra",
    # 葡萄牙语(模块名保留 swe)
    "swe": 'swe',
    "sv": 'sv_se',
    "pt": 'swe',
    "por": 'swe',
    # 越南语
    "vie": 'vie',
    "vi": 'vie',
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
    "_id": "_id",
    # 卢旺达语
    "rw": "rw",
    # 僧伽罗语
    "si": "si",
    # 塔吉克语
    "tg": "tg",
    # 印地语
    "hi": "hi",
    # 日语
    "ja": 'ja',
    # 韩语
    "ko": 'ko',
    # 意大利语
    "it": "it",
    # 荷兰语
    "nl": "nl",
    # 波兰语
    "pl": "pl",
    # 希腊语
    "el": "el",
    # 泰语
    "th": "th",
    # 芬兰语
    "fi": "fi",
    # 匈牙利语
    "hu": "hu",
    # 捷克语
    "cs": "cs",
    # 瑞典语
    "sv_se": "sv_se",
    # 挪威语/丹麦语共享工具词形，模块分开以便各自扩展
    "nb": "nb",
    "no": "nb",
    "nn": "nb",
    "da": "da",
    # 希伯来语
    "he": "he",
    "iw": "he",
    # 阿拉伯语
    "ar": "ar",
    "ara": "ar",
    # 波斯语
    "fa": "fa",
    "per": "fa",
    # 孟加拉语
    "bn": "bn",
    "ben": "bn",
    # 罗马尼亚语
    "ro": "ro",
    "ron": "ro",
    # 保加利亚语
    "bg": "bg",
    "bul": "bg",
    # 塞尔维亚语
    "sr": "sr",
    "srp": "sr",
    # 克罗地亚语
    "hr": "hr",
    "hrv": "hr",
    # 斯洛伐克语
    "sk": "sk",
    "slk": "sk",
    # 斯洛文尼亚语
    "sl": "sl",
    "slv": "sl",
    # 立陶宛语
    "lt": "lt",
    "lit": "lt",
    # 拉脱维亚语
    "lv": "lv",
    "lav": "lv",
    # 爱沙尼亚语
    "et": "et",
    "est": "et",
    # 马来语
    "ms": "ms",
    "msa": "ms",
    # 菲律宾语
    "fil": "fil",
    "tl": "fil",
    # 冰岛语
    "is": "is",
    "isl": "is",
    # 南非荷兰语
    "af": "af",
    "afr": "af",
    # 加泰罗尼亚语
    "ca": "ca",
    "cat": "ca",
    # 马其顿语
    "mk": "mk",
    "mkd": "mk",
    # 阿尔巴尼亚语
    "sq": "sq",
    "sqi": "sq",
    # 亚美尼亚语
    "hy": "hy",
    "hye": "hy",
    # 格鲁吉亚语
    "ka": "ka",
    "kat": "ka",
    # 哈萨克语
    "kk": "kk",
    "kaz": "kk",
    # 乌兹别克语
    "uz": "uz",
    "uzb": "uz",
    # 尼泊尔语
    "ne": "ne",
    "nep": "ne",
    # 南亚语言
    "ta": "ta",
    "te": "te",
    "gu": "gu",
    "pa": "pa",
    # 白俄罗斯语
    "be": "be",
    "bel": "be",
    # 波斯尼亚语
    "bs": "bs",
    "bos": "bs",
    # 蒙古语
    "mn": "mn",
    "mon": "mn",
    # 卡纳达语
    "kn": "kn",
    "kan": "kn",
    # 马拉雅拉姆语
    "ml": "ml",
    "mal": "ml",
    # 奥里亚语
    "or": "or",
    "ory": "or",
    # 阿萨姆语
    "as": "as",
    "asm": "as",
    # 威尔士语
    "cy": "cy",
    "cym": "cy",
    # 爱尔兰语
    "ga": "ga",
    "gle": "ga",
    # 巴斯克语
    "eu": "eu",
    "eus": "eu",
    # 加利西亚语
    "gl": "gl",
    "glg": "gl",
    # 马耳他语
    "mt": "mt",
    "mlt": "mt",
    # 卢森堡语
    "lb": "lb",
    "ltz": "lb",
    # 缅甸语
    "my": "my",
    "mya": "my",
    # 高棉语
    "km": "km",
    "khm": "km",
    # 老挝语
    "lo": "lo",
    "lao": "lo",
}

TRANSLATE_LANGS = []

_LANG_LIST_SORT = ['default', 'en', 'zh', 'zht', 'de', 'fra', 'swe',
                   'vie', 'ru', 'es', 'so', 'mr', 'az', "uk", 'sw',
    'tr', 'ky', 'ur', '_id', 'rw', 'si', 'tg', 'hi',
                   'ja', 'ko', 'it', 'nl', 'pl', 'el', 'th', 'fi',
                   'hu', 'cs', 'sv_se', 'nb', 'da', 'he',
                   'ar', 'fa', 'bn', 'ta', 'te', 'gu', 'pa',
                   'ro', 'bg', 'sr', 'hr', 'sk', 'sl', 'lt', 'lv',
                   'et', 'ms', 'fil', 'is', 'af', 'ca',
                   'mk', 'sq', 'hy', 'ka', 'kk', 'uz', 'ne',
                   'be', 'bs', 'mn', 'kn', 'ml', 'or', 'as',
                   'cy', 'ga', 'eu', 'gl', 'mt', 'lb',
                   'my', 'km', 'lo'
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
