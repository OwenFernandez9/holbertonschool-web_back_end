#!/usr/bin/env python3
"""
this module contains a function
"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    This function create task
    Return: asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
