"""
This module contains the Animal class
and its subclasses Cat and Dog.
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Animal is an abstract class that defines an
    abstract method 'sound'.
    All subclasses must implement this method.
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses
        to define the sound the animal makes.
        """
        pass


class Dog(Animal):
    """
    Dog is a subclass of Animal that implements the 'sound' method.
    """
    def sound(self):
        """
        Returns the sound a dog makes.
        """
        return "Bark"


class Cat(Animal):
    """
    Cat is a subclass of Animal that implements the 'sound'
    method.
    """
    def sound(self):
        """
        Returns the sound a cat makes.
        """
        return "Meow"
