#!/usr/bin/python3
"""
This module provides a function to load
a Python object from a JSON formatted file.
"""


import json


def load_from_json_file(filename):
    """
    Loads a Python object from a JSON formatted file.

    Args:
        filename (str): The path to the JSON
        file from which to load the object.

    Returns:
        Any: The Python object loaded from the JSON file.
                The type of the object depends
                on the content of the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.loads(f.read())
