#!/usr/bin/env python3
"""
this module contains a function
"""
import asyncio
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    this function return the 10 random numbers.
    """
    return [num async for num in async_generator()]
