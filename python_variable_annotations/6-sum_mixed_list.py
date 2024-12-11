#!/usr/bin/env python3
"""
In this module, the function sum_mixed_list is defined.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[(int, float]]) -> float:
    """
    The sum_mixed_list function is used to returns their sum as a float.
    """
    return sum(mxd_lst)
