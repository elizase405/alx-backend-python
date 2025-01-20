#!/usr/bin/env python3
""" task_wait_n: execute multiple coroutines
            at the same time with async
    task_wait_n(5, 5) - [0.343. 2.43, 2.764, 4.55, 4.96]"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine that takes 2 arg,
    and returns a list of n random delay between 0 and max_delay.

    args:
        n (int) - number of times to spawn wait_random
        max_delay(int) - maximum random delay value

    return: (list[float]) - randomly generated value
    """

    res = [await wait_random(max_delay) for _ in range(n)]
    return sorted(res)
