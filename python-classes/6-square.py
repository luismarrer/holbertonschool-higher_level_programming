#!/usr/bin/python3
"""
This module defines the Square class.
The Square class can be used to represent a geometric square,
manipulate its size, calculate its area, and print the square using '#'.
"""


class Square:
    """
    A class used to represent a Square.

    ...

    Attributes
    ----------
    __size : int
        The size of one side of the square.
    __position : tuple
        The position of the square (default is (0, 0)).

    Methods
    -------
    __init__(self, size=0, position=(0, 0)):
        Initializes the Square with a specific size and position.
    size(self):
        Gets the current size of the square.
    size(self, value):
        Sets the size of the square.
    position(self):
        Gets the current position of the square.
    position(self, value):
        Sets the position of the square.
    area(self):
        Calculates the area of the square.
    my_print(self):
        Prints the square with the character '#'.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        A class used to represent a Square.

        ...

        Attributes
        ----------
        __size : int
        The size of one side of the square.
        __position : tuple
        The position of the square (default is (0, 0)).

        Methods
        -------
        __init__(self, size=0, position=(0, 0)):
        Initializes the Square with a specific size and position.
        size(self):
        Gets the current size of the square.
        size(self, value):
        Sets the size of the square.
        position(self):
        Gets the current position of the square.
        position(self, value):
        Sets the position of the square.
        area(self):
        Calculates the area of the square.
        my_print(self):
        Prints the square with the character '#'.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (not isinstance(position[0], int)
            or not isinstance(position[1], int) or
                position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Gets the current position of the square.

        Returns
        -------
        tuple
            The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Parameters
        ----------
        value : tuple
            The position to set for the square.

        Raises
        ------
        TypeError
            If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (not isinstance(value[1], int) or not isinstance(value[0], int) or
                intvalue[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            i = 0
            while i is not self.__position[1]:
                print()
                i += 1
            for i in range(self.__size):
                x = 0
                while x is not self.__position[0]:
                    print(" ", end="")
                    x += 1
                for j in range(self.__size):
                    print("#", end="")
                print()
