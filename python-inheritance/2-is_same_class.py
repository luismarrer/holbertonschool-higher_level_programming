#!/usr/bin/python3
"""
This module contains the function is_same_class.
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is exactly an instance pf a_class,
        otherwise False.
    """
    return type(obj) is a_class
