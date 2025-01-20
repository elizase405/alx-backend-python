#!/usr/bin/env python3
"""
function task_wait_random(3) - returns asyncio Task.
"""

import asyncio
from asyncio import Task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    returns a asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
