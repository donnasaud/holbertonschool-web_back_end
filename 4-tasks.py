#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random
is being called."""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay
    Returns the list of all the delays (float values)
    """

    coroutines = [task_wait_random(max_delay) for i in range(n)]

    delays_list = []
    for completed in asyncio.as_completed(coroutines):
        delay = await completed
        delays_list.append(delay)
    return delays_list
