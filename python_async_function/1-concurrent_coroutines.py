#!/usr/bin/env python3
"""
this module contains a function
"""
import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    This function sorts the contents of a list of floats

    args: n - number, max_delay - max number the function

    Return: sorted list
    """
    listfloat = []

    for i in range(n):
        listfloat.append(wait_random(max_delay))
    x = await asyncio.gather(*listfloat)
    return sorted(x)
