#!/usr/bin/python3
"""
This module defines the Square class.
The Square class can be used to represent a geometric square,
manipulate its size, and calculate its area.
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
    size(self):
        Gets the current size of the square.
    size(self, value):
        Sets the size of the square.
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

    @property
    def size(self):
        """
        Gets the current size of the square.

        Returns
        -------
        int
            The size of one side of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Parameters
        ----------
        value : int
            The size to set for one side of the square.

        Raises
        ------
        TypeError
            If value is not an integer.
        ValueError
            If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns
        -------
        int
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#'.

        If the size of the square is 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
