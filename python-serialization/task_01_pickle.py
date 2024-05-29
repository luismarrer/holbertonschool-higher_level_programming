#!/usr/bin/python3
"""
This module provides functionalities to serialize and deserialize
custom Python objects using the pickle module.

The module defines a CustomObject class with the following attributes:
- name: A string representing the name of the object.
- age: An integer representing the age of the object.
- is_student: A boolean indicating whether the object represents a student.

The CustomObject class includes methods for displaying the object's attributes,
serializing the object to a file, and deserializing the object from a file.
"""


import pickle


class CustomObject:
    """
    A custom Python class representing an object
    with attributes name, age, and is_student.

    Attributes:
    - name (str): The name of the object.
    - age (int): The age of the object.
    - is_student (bool): Indicates if the object represents a student.

    Methods:
    - display(): Prints the attributes of the object in a formatted string.
    - serialize(filename): Serializes the object to the specified filename.
    - deserialize(cls, filename): Class method to
    deserialize an object from the specified filename.
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the attributes of the object in the specified format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance of the object
        and saves it to the provided filename.

        :param filename: The filename where the object will be saved.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"An error occurred while serializing: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Loads and returns an instance
        of CustomObject from the provided filename.

        :param filename: The filename from which the object will be loaded.
        :return: An instance of CustomObject if successful, None otherwise.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                return obj
        except (FileNotFoundError,EOFError) as e:
            print(f"An error occurred while deserializing: {e}")
            return None
