#!/usr/bin/python3
"""
This module provides functionality to read and display the contents of a file.
It contains a single function read_file which opens a file,
reads its content, and prints it to the standard output.
"""


def read_file(filename=""):
    """
    Reads the contents of a file and prints it to the standard output.

    Args:
        filename (str): The path to the file that needs to be read.
                        If no filename is provided,
                        the function will not perform any operation.

    Returns:
        None. The function directly prints
        the contents of the file to the output.

    Raises:
        FileNotFoundError: If the file does
        not exist or the path is incorrect.
        IOError: If the file cannot be opened due to an I/O error.
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
