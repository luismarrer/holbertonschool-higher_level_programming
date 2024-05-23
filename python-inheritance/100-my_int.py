#!/usr/bin/python3
"""
"""


class MyInt(int):
    """
    """
    def __init__(self, value):
        """
        """
        self.value = value

    def __eq__(self, other):
        """
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        """
        return super().__eq__(other)
