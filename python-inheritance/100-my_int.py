#!/usr/bin/python3
"""
This module contains the subclass MyInt of class int.
"""


class MyInt(int):
    """
     A subclass of int that inverts the == and != operators.
    """
    def __eq__(self, other):
        """
        Inverts the behavior of the equality operator (==).
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the behavior of the inequality operator (!=).
        """
        return super().__eq__(other)
