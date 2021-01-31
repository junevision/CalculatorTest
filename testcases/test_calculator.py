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


def get_datas(name, type='int'):
    with open("./datas/calc.yml") as f:
        all_datas = yaml.safe_load(f)
        print(all_datas)
    datas = all_datas[name][type]['datas']
    print(datas)
    ids = all_datas[name][type]['ids']
    print(ids)
    return datas, ids


class TestCalc:
    # datas: list = get_datas()
    add_int_data = get_datas('add', 'int')
    add_float_data = get_datas('add', 'float')
    div_int_normal_data = get_datas('div', 'int_normal')
    div_int_error_data = get_datas('div', 'int_error')

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
    @pytest.mark.parametrize("a, b, expected", add_int_data[0], ids=add_int_data[1])
    def test_add(self, a, b, expected):
        print(f"a={a}, b={b}, expected result={expected}")
        actual_result = self.calc.add(a, b)
        assert actual_result == expected

    @pytest.mark.add
    @pytest.mark.parametrize("a, b, expected", add_float_data[0], ids=add_float_data[1])
    def test_add_float(self, a, b, expected):
        print(f"a={a}, b={b}, expected result={expected}")
        actual_result = round(self.calc.add(a, b), 8)
        assert actual_result == expected

    @pytest.mark.div
    @pytest.mark.parametrize("a, b, expected", div_int_normal_data[0], ids=div_int_normal_data[1])
    def test_div_normal(self, a, b, expected):
        print(f"a={a}, b={b}, expected result={expected}")
        actual_result = self.calc.div(a, b)
        assert actual_result == expected

    @pytest.mark.div
    @pytest.mark.parametrize("a, b, expected", div_int_error_data[0], ids=div_int_error_data[1])
    def test_div_error(self, a, b, expected):
        print(f"a={a}, b={b}, expected result={expected}")
        with pytest.raises(ZeroDivisionError):  # pytest inner function
            self.calc.div(a, b)
        # try:
        #     self.calc.div(a, b)
        # except Exception as e:
        #     print(e)


if __name__ == '__main__':
    pytest.main(['-vs', 'test_calculator.py'])