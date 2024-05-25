#!/usr/bin/python3
"""
This module provides a function to print a person's full name.

Function:
    say_my_name(first_name, last_name="")
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the full name composed of first name and last name,
    handling type errors.

    Args:
        first_name (str): The first name of the person.
        last_name (str, optional): The last name of the person.
                                   Defaults to an empty string.

    Raises:
        TypeError: If first_name or last_name are not strings.

    Example:
        >>> say_my_name("John", "Doe")
        My name is John Doe

        >>> say_my_name("Alice")
        My name is Alice
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
