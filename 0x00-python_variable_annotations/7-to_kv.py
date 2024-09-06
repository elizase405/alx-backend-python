#!/usr/bin/env python3
"""This module defines the function `to_kv`"""
from typing import List, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple"""
    return (k, float(v**2))
