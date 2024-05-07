#!/usr/bin/env python3
"""
"""

import time
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension

async def measure_runtime() -> float:
    """

    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    finish = time.time() - start_time
    return finish
