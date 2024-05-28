#!/usr/bin/python3
"""
This module provides a function to convert a Python
object into a JSON formatted string.
"""


import json


def to_json_string(my_obj):
    """
        Converts a Python object into a JSON formatted string.

    Args:
        my_obj (Any): The Python object to convert.
                        This can be any object that is serializable to JSON,
                        such as dictionaries, lists, tuples,
                        strings, numbers, booleans, etc.

    Returns:
        str: A JSON formatted string representing `my_obj`.
    """
    return json.dumps(my_obj)
