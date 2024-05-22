#!/usr/bin/python3
"""
This module contains the function is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """
    Verify if the object is an instance of a class
    or an instance of a subclass of the class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class
        or an instance of a subclass of a_class,
        otherwise False.
    """
    return isinstance(obj, a_class)
