#!/usr/bin/python3
"""
This module defines the Student class,
which is designed to represent student information
in a simple school management system.
It allows for the creation, serialization, and
updating of student data.

The Student class provides methods to
serialize student information to a dictionary,
which can then be used for storage or
transfer, and to update the student's information
from a dictionary, mimicking a simple
form of deserialization. This functionality
is especially useful in scenarios involving
JSON data handling, such as loading or
saving to a database or a file.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Serializes the attributes of the Student instance to a dictionary.

        Args:
            attrs (list, optional): A list of attribute names
                                    to be included in the result.
                                    If None, all attributes are included.

        Returns:
            dict: A dictionary containing keys and
                  values corresponding to the
                  specified attributes of the student.
                  If no attributes are specified,
                  returns all attributes.
        """
        if isinstance(attrs, list):
            return {k: getattr(self, k) for k in attrs if k in self.__dict__}
        # Return all attributes if no specific attributes are specified
        return self.__dict__

    def reload_from_json(self, json):
        """
        Updates the attributes of the Student instance from a dictionary.

        Args:
            json (dict): A dictionary where keys
                         are attribute names and values are the values
                         to be updated to those attributes.

        No return value; the instance is modified directly.
        """
        for k, v in json.items():
            setattr(self, k, v)
