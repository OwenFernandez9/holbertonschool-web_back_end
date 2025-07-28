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
