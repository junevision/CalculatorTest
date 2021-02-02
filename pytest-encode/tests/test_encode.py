#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: test_encode.py
@time: 2021/2/2 19:05
@desc: 
"""
import pytest
from pytest_encode import logger


@pytest.mark.parametrize('name', ['吐槽大会', '脱口秀'])
def test_encode(name):
    logger.info(f"test data: {name}")
    print(name)