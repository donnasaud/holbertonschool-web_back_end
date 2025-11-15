#!/usr/bin/env python3
"""
Module 1-concurrent_coroutines.py
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay
    Returns the list of all the delays (float values)
    """

    coroutines = [wait_random(max_delay) for i in range(n)]

    delays_list = []
    for completed in asyncio.as_completed(coroutines):
        delay = await completed
        delays_list.append(delay)
    return delays_list
