#!/usr/bin/env python3
"""
coroutine collects 10 random numbers, then returns 10 random numbers
"""

from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Async comprehension
    """
    return [_ async for _ in async_generator()]
