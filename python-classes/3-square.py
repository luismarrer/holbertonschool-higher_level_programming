#!/usr/bin/python3
"""
This module defines the Square class.
The Square class can be used to represent a
geometric square and calculate its area.
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
    __init__(self, size=0):
        Initializes the Square with a specific size.
    area(self):
        Calculates the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes the Square with a specific size.

        Parameters
        ----------
        size : int, optional
            The size of one side of the square (default is 0).

        Raises
        ------
        TypeError
            If size is not an integer.
        ValueError
            If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns
        -------
        int
            The area of the square.
        """
        return self.__size ** 2
