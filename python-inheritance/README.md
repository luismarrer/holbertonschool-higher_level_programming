# Python - Inheritance

This project focuses on the concepts of inheritance in Python. It covers how to define subclasses, the use of multiple base classes, and the default behaviors inherited from Python's base class.

## Learning Objectives

By the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- What a superclass, baseclass, or parentclass is
- What a subclass is
- How to list all attributes and methods of a class or instance
- When an instance can have new attributes
- How to inherit a class from another
- How to define a class with multiple base classes
- What the default class every class inherits from is
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What the purpose of inheritance is
- What are, when and how to use `isinstance`, `issubclass`, `type` and `super` built-in functions

## Requirements

### Python Scripts
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### Python Test Cases
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder named `tests`
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)

## Tasks

### 0. Lookup
Write a function that returns the list of available attributes and methods of an object.
- Location: `python-inheritance/0-lookup.py`

### 1. My list
Write a class `MyList` that inherits from list, which can print the list in ascending order.
- Location: `python-inheritance/1-my_list.py`, tests: `tests/1-my_list.txt`

### 2. Exact same object
Write a function that returns `True` if the object is exactly an instance of the specified class; otherwise `False`.
- Location: `python-inheritance/2-is_same_class.py`

### 3. Same class or inherit from
Write a function that checks if an object is an instance of, or if the object is an instance of a class that inherited from, the specified class.
- Location: `python-inheritance/3-is_kind_of_class.py`

### 4. Only sub class of
Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False.
- Location: `python-inheritance/4-inherits_from.py`

### 5. Geometry module
Write an empty class `BaseGeometry`.
- Location: `python-inheritance/5-base_geometry.py`

### 6. Improve Geometry
Enhance the `BaseGeometry` class by adding a method that raises an exception with a message indicating that the area is not implemented.
- Location: `python-inheritance/6-base_geometry.py`

### 7. Integer validator
Expand the `BaseGeometry` class with a method that validates if a value is an integer greater than zero.
- Location: `python-inheritance/7-base_geometry.py`, tests: `tests/7-base_geometry.txt`

### 8. Rectangle
Write a class `Rectangle` that inherits from `BaseGeometry` and initializes with width and height validated through `integer_validator`.
- Location: `python-inheritance/8-rectangle.py`

### 9. Full rectangle
Modify the `Rectangle` class to implement the `area` method and to print the rectangle description in a specific format.
- Location: `python-inheritance/9-rectangle.py`

### 10. Square #1
Write a class `Square` that inherits from `Rectangle` and initializes with size validated through `integer_validator`.
- Location: `python-inheritance/10-square.py`

### 11. Square #2
Modify the `Square` class to print the square description in a specific format.
- Location: `python-inheritance/11-square.py`

### 12. My integer
Write a class `MyInt` that inherits from `int` but inverts the behavior of `==` and `!=`.
- Location: `python-inheritance/100-my_int.py`

### 13. Can I?
Write a function that adds a new attribute to an object if it's possible, raising a TypeError if the object can't accept new attributes.
- Location: `python-inheritance/101-add_attribute.py`

## Author

- **Luis** - Holberton School student

## Acknowledgments

- Holberton School for providing a project-based learning approach to software engineering.

