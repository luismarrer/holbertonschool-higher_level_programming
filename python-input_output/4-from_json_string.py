#!/usr/bin/python3
"""
This module provides a function to convert
a JSON formatted string into a Python object
"""


import json


def from_json_string(my_str):
    """
    Converts a JSON formatted string into a Python object.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        Any: The Python object obtained from the JSON string.
    """
    return json.loads(my_str)
