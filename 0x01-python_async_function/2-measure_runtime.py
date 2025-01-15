#!/usr/bin/env python3
""" wait_n: measure runtime of multiple
            coroutines at the same time with async
    measure_time(5, 9) - 1.75970
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measures the total execution time
    for wait_n(n, max_delay)

    args:
        n (int) - number of times to spawn wait_random
        max_delay(int) - maximum random delay value

    return: float - total_time / n
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start_time

    return total_time / n
