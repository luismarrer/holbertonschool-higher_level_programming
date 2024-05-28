#!/usr/bin/python3
"""
This module provides functionality to write text to a file.
It includes a function write_file which takes a filename
and text as parameters, and writes the provided text to the specified file.
"""


def write_file(filename="", text=""):
    """
        Writes the given text to a file specified by the filename.
        If the file does not exist, it creates a new one.

    Args:
        filename (str): The path to the file where the text will be written.
                        If no filename is provided,
                        the function will not perform any operation.
        text (str): The text to be written to the file.
                    If no text is provided, an empty file will be created.

    Returns:
        int: The number of characters written to the file.

    Raises:
        IOError: If the file cannot be opened or written to.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
