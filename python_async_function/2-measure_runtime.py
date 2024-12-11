#!/usr/bin/env python3
"""
this module contains a function
"""
import asyncio
import time
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    This function calculates time

    args: n - number, max_delay - max number the function

    Return: total time
    """
    inicial_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    finished_time = time.time()
    total_time = (finished_time - inicial_time) / n
    return total_time
