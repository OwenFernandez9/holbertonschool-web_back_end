#!/usr/bin/env python3
"""
In this module, the function to_kv is defined.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    The to_kv function is used to returns tupla
    """
    return (k, v ** 2)
