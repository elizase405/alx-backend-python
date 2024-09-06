#!/usr/bin/env python3
"""1 function: sum_mixed_list(mxd_list) - sum of mxd_list """
from typing import List
from typung import Union


def sum_mixed_list(mxd_list: List[Union[float, int]]) -> float:
    """returns the sum of input_list"""
    return float(sum(mxd_list))
