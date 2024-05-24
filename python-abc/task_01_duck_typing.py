"""
This modules contains the abstract class Shape and its subclasses Circle
and Rectangle. It defines the blueprint for geometric shapes and includes
methods for calculating the area and perimeter. It also includes
a function to print the area and perimeter
of any shape using duck typing.
"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Shape is an abstract class that defines the blueprint
    for geometric shapes. It includes abstract methods for
    calculating the area and perimeter.
    """
    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area
        of the shape.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        Must be implemented by subclasses.
        """
        pass


class Circle(Shape):
    """
    Circle is a subclass of Shape that represents a circle.
    """
    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        """
        Calculate the area of the circle.
        """
        return math.pi * self.radius * self.radius

    def perimeter(self):
        """
        Calculate the perimeter (circumference)
        of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle is a subclass of Shape that represents a rectangle.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape.
    This function uses duck typing to handle different shapes uniformly.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
