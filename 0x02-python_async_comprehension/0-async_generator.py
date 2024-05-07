#!/usr/bin/env python3
"""
a coroutine that takes no argument
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Async Genrator
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
