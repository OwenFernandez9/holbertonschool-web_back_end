#!/usr/bin/env python3
"""
the module contains the function filter_datum
and class RedactingFormatter
"""
import re
from typing import List
import logging
import os
import mysql.connector
from mysql.connector.connection import MySQLConnection


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    The function should use a regex to replace occurrences of certain field
    values.
    """
    return re.sub(f"({'|'.join(fields)})=.*?{separator}",
                  f"\\1={redaction}{separator}", message)


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"


def __init__(self, fields: List[str]):
    """
    Initialize RedactingFormatter with fields to redact.
    """
    super(RedactingFormatter, self).__init__(self.FORMAT)
    self.fields = fields


def format(self, record: logging.LogRecord) -> str:
    """
    filter values in incoming log records using filter_datum
    """
    original = super().format(record)
    return filter_datum(self.fields, self.REDACTION,
                        original, self.SEPARATOR)


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """
    function returns a logging.Logger object.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(stream_handler)

    return logger


def get_db() -> MySQLConnection:
    """
    Returns a connector to the database.
    """
    return mysql.connector.connect(
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        database=os.getenv("PERSONAL_DATA_DB_NAME")
    )
