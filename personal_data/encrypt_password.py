#!/usr/bin/env python3
"""
Module to hash a password using bcrypt
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with a salt and returns the hashed password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Checks if the provided password matches the hashed password.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
