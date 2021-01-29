#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: test_calculator.py
@time: 2021/1/29 15:36
@desc: Test Class
"""
import sys
import pytest
import yaml

sys.path.append('..')
from pythoncode.Calculator import Calculator


def get_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
        return (datas["add"]["datas"], datas["add"]["ids"])


class TestCalc:
    datas:list = get_datas()
    def setup_class(self):
        print("Start Calculate...")
        self.calc = Calculator()

    def teardown_class(self):
        print("Calculation End")

    @pytest.mark.add
    @pytest.mark.parametrize("a, b, result", datas[0], ids=datas[1])
    def test_add(self, a, b, result):
        print(f"a={a}, b={b}, result={result}")
        assert result == self.calc.add(a, b)

    # todo: complete add function
    # todo: div function
    # done: main function
    @pytest.mark.div
    def test_div(self):
        pass
