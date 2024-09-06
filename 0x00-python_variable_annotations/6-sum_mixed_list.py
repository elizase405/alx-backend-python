#!/usr/bin/env python3
"""1 function: sum_mixed_list(mxd_list) - sum of mxd_list """
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[float, int]]) -> float:
    """returns the sum of input_list"""
    return sum(mxd_list)
