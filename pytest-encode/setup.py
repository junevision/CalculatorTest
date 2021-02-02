#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: setup.py
@time: 2021/2/2 18:55
@desc: build tool
"""

from setuptools import setup
setup(
    name='pytest_encode',
    url='https://github.com/xxx/pytest-encode',
    version='1.0',
    author="Jun_Lei",
    author_email='rainkitty1989@qq.com',
    description='set your encoding and logger',
    long_description='Show Chinese for your mark.parametrize(). Define logger variable for getting your log',
    classifiers=[
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.8',
    ],
    license='proprietary',
    packages=['pytest_encode'],
    keywords=[
        'pytest', 'py.test', 'pytest_encode',
    ],

    install_requires=[
        'pytest'
    ],
    entry_points={
        'pytest11': [
            'pytest-encode = pytest_encode',
        ]
    },
    zip_safe=False
)
