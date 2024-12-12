#!/usr/bin/env python3
"""
this module contains a function
"""
import asyncio
import time
from typing import List
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> List[float]:
    """
    this function should measure the total runtime and return it.
    """
    start_time = asyncio.get_event_loop.time()

    asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    total_time = (end_time - start_time)
    return total_time
