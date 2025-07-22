#!/usr/bin/env python3
"""
the module contains the function filter_datum
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    The function should use a regex to replace occurrences of certain field
    values.
    """
    return re.sub(f"({'|'.join(fields)})=.*?{separator}",
                  f"\\1={redaction}{separator}", message)
