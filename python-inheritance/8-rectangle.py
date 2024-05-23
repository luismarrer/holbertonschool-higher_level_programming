#!/usr/bin/python3
"""
Module that defines a Rectangle class that inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.

    Methods:
        __init__(self, width, height): Initializes a
        Rectangle object with width and height.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle object with width and height.

        Args:
            width (int): The width of the rectangle,
            validated as a positive integer.
            height (int): The height of the rectangle,
            validated as a positive integer.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
