#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: test_yaml.py.py
@time: 2021/1/29 17:00
@desc: 
"""
import yaml


def test_yaml():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        print(datas["add"]["datas"])