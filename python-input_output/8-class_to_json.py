#!/usr/bin/python3
"""
This module contains a function to serialize
attributes of a class instance to a dictionary.
"""


def class_to_json(obj):
    """
    Serializes the attributes of a class instance to a dictionary.

    Args:
        obj (object): The instance of the class whose attributes will be serialized.

    Returns:
        dict: A dictionary containing all the public attributes and their values from the class instance.
    """
    return obj.__dict__
