#!/usr/bin/env python3
"""
In this module, the function element_length is defined.
"""
from typing import Iterable,List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    The element_length function is used to return values with the appropriate types
    """
    return [(i, len(i)) for i in lst]
