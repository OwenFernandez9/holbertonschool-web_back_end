#!/usr/bin/env python3
"""
this module contains a function
"""
import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    this function should measure the total runtime and return it.
    """
    start_time = time.time()

    asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    total_time = (end_time - start_time)
    return total_time
