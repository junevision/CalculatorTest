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
        return datas


class TestCalc:
    datas: list = get_datas()

    def setup_class(self):
        print("Start Calculate...")
        self.calc = Calculator()

    def teardown_class(self):
        print("Calculation End!")

    def setup(self):
        print("--Calculation case begin--")

    def teardown(self):
        print("--Calculation case complete--")

    @pytest.mark.add
    @pytest.mark.parametrize("a, b, expected", datas["add"]["datas"], ids=datas["add"]["ids"])
    def test_add(self, a, b, expected):
        print(f"a={a}, b={b}, expected result={expected}")
        actual_result = self.calc.add(a, b)
        assert expected == actual_result

    # done: complete add function
    # done: div function
    # done: main function
    @pytest.mark.div
    @pytest.mark.parametrize("a, b, expected", datas["div"]["datas"], ids=datas["div"]["ids"])
    def test_div(self, a, b, expected):
        print(f"a={a}, b={b}, expected result={expected}")
        if b != 0:
            actual_result = self.calc.div(a, b)
            assert expected == actual_result
        else:
            try:
                self.calc.div(a, b)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    pytest.main(['-vs', 'testcases/test_calculator.py'])