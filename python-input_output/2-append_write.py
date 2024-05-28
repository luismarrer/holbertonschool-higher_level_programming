#!/usr/bin/python3
"""
This module provides a function to append text to a file.
"""


def append_write(filename="", text=""):
    """
    Appends text to a specified file. Creates a new file if it doesn't exist.

    Args:
        filename (str): Path to the file.
        text (str): Text to append.

    Returns:
        int: Number of characters written.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
