#!/usr/bin/python3
"""
This module defines the Square class.
The Square class can be used to represent a geometric square.
"""


class Square:
    """
    A class used to represent a Square.

    ...

    Attributes
    ----------
    __size : int
        The size of one side of the square.

    Methods
    -------
    __init__(self, size):
        Initializes the Square with a specific size.
    """

    def __init__(self, size):
        """
        Initializes the Square with a specific size.

        Parameters
        ----------
        size : int
            The size of one side of the square.
        """
        self.__size = size
