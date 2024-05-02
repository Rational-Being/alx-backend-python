#!/usr/bin/env python3
"""
augument the following code witht he correct duck-typed annotations
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    annotations solution in the parameters
    """
    if lst:
        return lst[0]
    else:
        return None
