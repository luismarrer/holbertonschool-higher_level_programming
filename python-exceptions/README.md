# Python - Exceptions

This project is part of the curriculum of Holberton School and dives into exceptions in Python, covering how to handle errors gracefully and robustly. This project emphasizes the differences between errors and exceptions, the use of exceptions, and best practices in Python error handling.

## Learning Objectives

By the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome
- The difference between errors and exceptions
- How to use exceptions and when to use them
- How to correctly handle exceptions
- The purpose of catching exceptions
- How to raise a built-in exception
- The necessity of implementing a clean-up action after an exception

## Requirements

### General
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

## Tasks

### 0. Safe list printing
Write a function that prints x elements of a list, handling exceptions to continue operation even if some elements cause errors.
- Location: `python-exceptions/0-safe_print_list.py`

### 1. Safe printing of an integers list
Write a function that prints an integer from any input, robustly handling incorrect types.
- Location: `python-exceptions/1-safe_print_integer.py`

### 2. Print and count integers
Print the first x integers of a list, safely handling types that cannot be printed as integers.
- Location: `python-exceptions/2-safe_print_list_integers.py`

### 3. Integers division with debug
A function that divides two integers and prints the result, handling division by zero and other errors gracefully.
- Location: `python-exceptions/3-safe_print_division.py`

### 4. Divide a list
Divide element by element from two lists, safely handling errors like wrong types and division by zero.
- Location: `python-exceptions/4-list_division.py`

### 5. Raise exception
A function that raises a type exception, to demonstrate raising exceptions manually.
- Location: `python-exceptions/5-raise_exception.py`

### 6. Raise a message
Raise a name exception with a custom message, demonstrating the control over exception messaging.
- Location: `python-exceptions/6-raise_exception_msg.py`

### Advanced Tasks:
### 7. Safe integer print with error message
Print an integer and handle exceptions, printing error messages to stderr if something goes wrong.
- Location: `python-exceptions/100-safe_print_integer_err.py`

### 8. Safe function
Execute a function safely, handling any exceptions that occur and printing an error message to stderr.
- Location: `python-exceptions/101-safe_function.py`

### 9. ByteCode -> Python #4
Translate a given Python bytecode back into Python code that performs the same function.
- Location: `python-exceptions/102-magic_calculation.py`

## Author

- **Luis** - Holberton School student

## Acknowledgments

- Holberton School for providing a project-based learning approach to software engineering.
