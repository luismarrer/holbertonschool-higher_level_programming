#!/usr/bin/python3
"""
This module defines the MyList class.
"""


class MyList(list):
    """
    A subclass of list that includes a method
    to print the list in sorted order.
    """
    def print_sorted(self):
        """
        Prints the list in sorted ascending order.
        """
        print(sorted(self))
