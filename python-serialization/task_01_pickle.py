#!/usr/bin/python3


import pickle


class CustomObject:
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
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"An error occurred while deserializing: {e}")
            return None
