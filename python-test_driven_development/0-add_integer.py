#!/usr/bin/python3
"""
This file content the function add_integer


"""


def add_integer(a, b=98):
    """
    This function add a + b. If b is blank, b = 98
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a + b)
