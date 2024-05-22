#!/usr/bin/python3
"""
This module contains BaseGeometry class.
"""


class BaseGeometry:
    """
    Base class.

    Methods:
        area(self): Raises an Exception indicating
        that it is not implemented.

        integer_validator(self, name, value): Validates that
        a parameter is a positive integer.
    """

    def integer_validator(self, name, value):
        """
        Validates that a parameter is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value of the parameter to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def area(self):
        """
        Base function.

        Raises:
            Exception: Always raises an exception with the
            message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
