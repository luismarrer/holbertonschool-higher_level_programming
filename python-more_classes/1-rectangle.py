#!/usr/bin/python3
"""
This module defines the Rectangle Class.
The Rectangle class is a rectangle.
"""


class Rectangle:
    """
    Rectangle class

    Attributes
    ----------
    __width: int
    __height: int

    Methods
    -------
    __init__(self, width=0, height=0):
        constructor, initializes the rectangle
        with a width and height.
    width(self):
        Gets the current width.
    width(self, value):
        Sets the width of the rectangle.
    height(self):
        Gets the current height.
    height(self, value):
        Sets the height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle with a specific width and height.

        Parameters
        ----------
        width: width
        height: height

        Raises
        ------
        TypeError
            If parameters are not integers.
        ValueError
            If parameter are less than 0.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        Gets the current width.

        Returns
        -------
        int
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width.

        Parameters
        ----------
        value: int
            The width to set.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the current height.

        Returns
        -------
        int
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height.

        Parameters
        ----------
        value: int
            the height to set.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
