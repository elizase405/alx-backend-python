#!/usr/bin/env python3
""" module with 1 function: safe_first_element  """
from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
