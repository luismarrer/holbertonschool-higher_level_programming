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
        <BLANKLINE>
        How are you?
        <BLANKLINE>
        I'm fine:
    """

    error1 = "text must be a string"
    if type(text) is not str:
        raise TypeError(error1)

    brk = True
    for i in text.strip():
        if brk and i == ' ':
            continue
        print(i, end="")
        brk = False
        if i in ['.', '?', ':']:
            print("\n")
            brk = True
