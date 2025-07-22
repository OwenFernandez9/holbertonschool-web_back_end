#!/usr/bin/env python3
import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    return re.sub(rf"({'|'.join(fields)})=.*?{separator}", rf"\1={redaction}{separator}", message)