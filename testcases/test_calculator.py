#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: test_calculator.py
@time: 2021/1/29 15:36
@desc: Test Class
"""
import sys

import allure
import pytest

sys.path.append('..')
from pythoncode.Calculator import Calculator


@pytest.fixture()
def get_instance():
    print("Start Calculate...")
    calc = Calculator()
    yield calc
    print("Calculation End!")


@allure.feature("Calculator")
class TestCalc:
    # datas: list = get_datas()
    # add_int_data = get_datas('add', 'int')
    # add_float_data = get_datas('add', 'float')
    # div_int_normal_data = get_datas('div', 'int_normal')
    # div_int_error_data = get_datas('div', 'int_error')

    # @pytest.mark.add
    # @pytest.mark.parametrize("a, b, expected", add_int_data[0], ids=add_int_data[1])
    # def test_add_int(self, get_instance, a, b, expected):
    #     print(f"a={a}, b={b}, expected result={expected}")
    #     actual_result = get_instance.add(a, b)
    #     assert actual_result == expected

    # @pytest.mark.add
    # @pytest.mark.parametrize("a, b, expected", add_float_data[0], ids=add_float_data[1])
    # def test_add_float(self, get_instance, a, b, expected):
    #     print(f"a={a}, b={b}, expected result={expected}")
    #     actual_result = round(get_instance.add(a, b), 8)
    #     assert actual_result == expected
    #
    # @pytest.mark.div
    # @pytest.mark.parametrize("a, b, expected", div_int_normal_data[0], ids=div_int_normal_data[1])
    # def test_div_normal(self, get_instance, a, b, expected):
    #     print(f"a={a}, b={b}, expected result={expected}")
    #     actual_result = get_instance.div(a, b)
    #     assert actual_result == expected
    #
    # @pytest.mark.div
    # @pytest.mark.parametrize("a, b, expected", div_int_error_data[0], ids=div_int_error_data[1])
    # def test_div_zero(self, get_instance, a, b, expected):
    #     print(f"a={a}, b={b}, expected result={expected}")
    #     with pytest.raises(ZeroDivisionError):  # pytest inner function
    #         get_instance.div(a, b)
    #     try:
    #         self.calc.div(a, b)
    #     except Exception as e:
    #         print(e)

    @allure.title("add_{get_add_int_datas_with_fixture[0]}_{get_add_int_datas_with_fixture[1]}")
    @allure.story("Add Integer Function")
    def test_add_int(self, get_instance, get_add_int_datas_with_fixture):
        gaidwf = get_add_int_datas_with_fixture
        assert gaidwf[2] == get_instance.add(gaidwf[0], gaidwf[1])

    @allure.title("add_{get_add_float_datas_with_fixture[0]}_{get_add_float_datas_with_fixture[1]}")
    @allure.story("Add float Function")
    def test_add_float(self, get_instance, get_add_float_datas_with_fixture):
        gafdwf = get_add_float_datas_with_fixture
        assert gafdwf[2] == round(get_instance.add(gafdwf[0], gafdwf[1]), 8)

    @allure.title("div_{get_div_int_normal_datas_with_fixture[0]}_{get_div_int_normal_datas_with_fixture[1]}")
    @allure.story("div Integer normal Function")
    def test_div_int_normal(self, get_instance, get_div_int_normal_datas_with_fixture):
        gdindwf = get_div_int_normal_datas_with_fixture
        assert gdindwf[2] == get_instance.div(gdindwf[0], gdindwf[1])

    @allure.title("div_{get_div_int_error_datas_with_fixture[0]}_{get_div_int_error_datas_with_fixture[1]}")
    @allure.story("div Integer error Function")
    def test_div_int_zero(self, get_instance, get_div_int_error_datas_with_fixture):
        gdiedwf = get_div_int_error_datas_with_fixture
        with pytest.raises(ZeroDivisionError):  # pytest inner function
            get_instance.div(gdiedwf[0], gdiedwf[1])


if __name__ == '__main__':
    pytest.main(['-vs', 'test_calculator.py'])