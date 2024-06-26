#!/usr/bin/env python3
"""
type annoted function that a string and a float as arguments and
returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    returns a tuple when pass a stirng and float as arguments
    """
    return (k, float(v**2))
