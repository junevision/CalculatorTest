#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: __init__.py
@time: 2021/2/2 18:54
@desc: hook function in init file
"""
import logging
from typing import List
import pytest

logging.basicConfig(level=logging.INFO,
                    # log format
                    format='[%(levelname)s] %(asctime)s %(filename)s[line:%(lineno)d] %(message)s',
                    # log real time
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    # log file address
                    filename='report.log',
                    # the way of opening log
                    filemode='w'
                    )
logger = logging.getLogger(__name__)


def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    """Called after collection has been performed. May filter or re-order
    the items in-place.

    :param pytest.Session session: The pytest session object.
    :param _pytest.config.Config config: The pytest config object.
    :param List[pytest.Item] items: List of item objects.
    """
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        logger.info(f"item.name: {item.name}")
        logger.info(f"item._nodeid: {item._nodeid}")
        if 'add' in item._nodeid:
            item.add_marker(pytest.mark.add)
        elif 'div' in item._nodeid:
            item.add_marker(pytest.mark.div)