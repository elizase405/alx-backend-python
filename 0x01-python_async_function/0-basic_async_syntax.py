#!/usr/bin/env python3
""" wait_random: Asynchronous coroutine
    wait_random(5) - float value between 0 and 5"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that takes an arg,
    waits for a random delay between 0 and arg,
    and eventually returns it.

    args: max_delay(int) - maximumrandom  delay value

    return: (int) - randomly generated value
    """

    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
