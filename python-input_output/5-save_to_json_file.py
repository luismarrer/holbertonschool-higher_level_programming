#!/usr/bin/python3
"""
This module includes a function to save
a Python object as a JSON formatted string
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Saves a Python object to a file in JSON format.

    Args:
        my_obj (Any): The Python object to serialize to JSON.
        The object must be serializable.
        filename (str): The path to the file where the JSON
        data will be written.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(json.dumps(my_obj))
