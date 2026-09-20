# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/3/27


from .dtparser import parse
from .dtparser import check
from .dtparser import parse_by_format
from .dtparser import parse_by_regex
from .dtframe import parse as parse_frame

__version__ = "0.2.0"

__all__ = [
    "parse",
    "check",
    "parse_by_format",
    "parse_by_regex",
    "parse_frame",
    "__version__",
]
