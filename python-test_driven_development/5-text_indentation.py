#!/usr/bin/python3
"""
This module provides a function to print a text with 2 new lines
after each of these characters: ., ? and :
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.

    Examples:
        >>> text_indentation("Hello. How are you? I'm fine:")
        Hello.

        How are you?

        I'm fine:
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    for char in text:
        if char in ['.', '?', ':']:
            print(char)
            print()
        else:
            print(char, end="")
