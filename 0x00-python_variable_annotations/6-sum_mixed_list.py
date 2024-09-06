#!/usr/bin/env python3
"""This module defines a function `sum_mixed_list`"""
from typing import Union
from typing import List


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """returns the sum of list elements"""
    return float(sum(mxd_list))
