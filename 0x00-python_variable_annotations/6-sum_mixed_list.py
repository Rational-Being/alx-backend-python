#!/usr/bin/env python3
"""
type annoted function that takes a list of integers and float
and returns their sum as float
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    returns the sil of list of int and float as float
    """
    return float(sum(mxd_lst))
