#!/usr/bin/env python3
"""
type annoted function that takes a list of float as argument
and returns thier sum as float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    takes list of loat as argument
    """
    return float(sum(input_list))

