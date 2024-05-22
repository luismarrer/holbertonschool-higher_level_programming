#!/usr/bin/python3
"""
This module contains the function lookup.
"""


def lookup(obj: object) -> list:
    """
    Returns a list of attributes and methods of an object.

    Args:
        obj (object): The object to inspect.

    Returns:
        list: A list of attributes and methods names.
    """
    return dir(obj)
