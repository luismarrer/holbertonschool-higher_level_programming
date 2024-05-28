#!/usr/bin/python3
"""
This module defines the Student class,
which represents a student
with attributes for the first name, last name, and age.
"""


class Student:
    """
    Represents a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Serializes the Student instance's attributes to a dictionary.

        Returns:
            dict: A dictionary containing keys and values
            corresponding to the attributes of the Student.
        """
        return self.__dict__
