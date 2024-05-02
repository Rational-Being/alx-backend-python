#!/usr/bin/env python3
"""
type annoted function that takes a foat as argument and returns a funtion
that multiplies a float
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a funtion that multiplies a float by multiplier
    """

    def i_multiply_float(mul_F: float) -> float:
        return multiplier * mul_F

    return i_multiply_float
