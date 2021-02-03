#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: Calculator.py
@time: 2021/1/29 15:35
@desc: Tested Class: Calculator
"""
from pytest_encode import logger


class Calculator:
    def add(self, a, b):
        logger.info(f"This case is to test {a} + {b}")
        return a + b

    def div(self, a, b):
        logger.info(f"This case is to test {a} / {b}")
        return a / b
