#!/usr/bin/env python3
"""1 function: sum_list(input_list) - sum of input_list """
from typing import List
from functools import reduce


def sum_list(input_list: List[float]) -> float:
    """returns the sum of input_list"""
    return reduce(lambda x, y: x + y, input_list)
