#!/usr/bin/env python3
"""
In this module, the function make_multiplier is defined.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier create a function called multiplier
    """
    def multiplier_function(n: float) -> float:
        """
        multiplier_function this is the internal function/
        that receives a number n of type float and returns the/
        result of multiplying n by multiplier.
        """
        return n * multiplier
    return multiplier_function

