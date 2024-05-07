#!/usr/bin/env python3
"""
Learning Asychronous funtion
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    funtion waits for a random time
    """
    time_to_wait = random.random() * max_delay
    await asyncio.sleep(time_to_wait)
    return time_to_wait
