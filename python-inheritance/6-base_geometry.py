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
    """
    def area(self):
        """
        Base function.

        Raises:
            Exception: Always raises an exception with the
            message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
