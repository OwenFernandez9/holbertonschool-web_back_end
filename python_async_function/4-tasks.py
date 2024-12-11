#!/usr/bin/env python3
"""
this module contains a function
"""
import asyncio
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    This function sorts the contents of a list of floats

    args: n - number, max_delay - max number the function

    Return: sorted list
    """
    listfloat = []

    for i in range(n):
        listfloat.append(task_wait_random(max_delay))
    x = await asyncio.gather(*listfloat)
    return sorted(x)
