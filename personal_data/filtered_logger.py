#!/usr/bin/env python3
"""
the module contains the function filter_datum
and class RedactingFormatter
"""
import re
from typing import List
import logging


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    The function should use a regex to replace occurrences of certain field
    values.
    """
    return re.sub(f"({'|'.join(fields)})=.*?{separator}",
                  f"\\1={redaction}{separator}", message)



class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        original = super().format(record)
        return filter_datum(self.fields, self.REDACTION, original, self.SEPARATOR)
