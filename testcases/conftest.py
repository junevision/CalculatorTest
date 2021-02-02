#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: conftest.py.py
@time: 2021/2/2 11:12
@desc: get test data from yaml
"""
import pytest
import yaml


def get_datas(name, type='int'):
    with open("./datas/calc.yml") as f:
        all_datas = yaml.safe_load(f)
    datas = all_datas[name][type]['datas']
    ids = all_datas[name][type]['ids']
    return datas, ids


@pytest.fixture(params=get_datas('add', 'int')[0], ids=get_datas('add', 'int')[1])
def get_add_int_datas_with_fixture(request):
    return request.param


@pytest.fixture(params=get_datas('add', 'float')[0], ids=get_datas('add', 'float')[1])
def get_add_float_datas_with_fixture(request):
    return request.param


@pytest.fixture(params=get_datas('div', 'int_normal')[0], ids=get_datas('div', 'int_normal')[1])
def get_div_int_normal_datas_with_fixture(request):
    return request.param


@pytest.fixture(params=get_datas('div', 'int_error')[0], ids=get_datas('div', 'int_error')[1])
def get_div_int_error_datas_with_fixture(request):
    return request.param

