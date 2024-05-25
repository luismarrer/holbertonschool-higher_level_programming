#!/usr/bin/python3
"""
This module defines a Rectangle class that represents a rectangle
with width and height, and includes methods for calculating its
area and perimeter, as well as string representation.
"""

class Rectangle:
    """
    A class used to represent a Rectangle

    ...

    Attributes
    ----------
    width : int
        The width of the rectangle (default 0)
    height : int
        The height of the rectangle (default 0)

    Methods
    -------
    area():
        Returns the area of the rectangle
    perimeter():
        Returns the perimeter of the rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Constructs all the necessary attributes for the rectangle object.

        Parameters
        ----------
            width : int
                The width of the rectangle (default 0)
            height : int
                The height of the rectangle (default 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self._width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self._height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self._width * self._height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def __str__(self):
        """Returns a string representation of the rectangle with '#' character"""
        if self._width == 0 or self._height == 0:
            return ""
        return "\n".join(["#" * self._width for _ in range(self._height)])

    def __repr__(self):
        """Returns a string representation of the rectangle to recreate a new instance"""
        return f"Rectangle({self._width}, {self._height})"
