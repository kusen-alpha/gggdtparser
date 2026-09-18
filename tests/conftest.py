# -*- coding: utf-8 -*-

import datetime

import pytest


@pytest.fixture
def base_dt():
    """固定基准时间，避免测试依赖真实当前时间。"""
    return datetime.datetime(2026, 9, 18, 15, 4, 5)
