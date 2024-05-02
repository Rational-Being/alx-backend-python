#!/usr/bin/env python3
"""
type annoted function that a given parameter
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    return values witht the appropriate types
    """
    return [(i, len(i)) for i in lst]
