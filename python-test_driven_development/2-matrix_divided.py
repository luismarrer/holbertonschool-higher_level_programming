#!/usr/bin/python3
"""
This module provides a function to divide all
elements of a matrix by a given number.

Function:
    matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of list of int/float): A matrix represented as
        a list of lists, where each sublist contains integers or floats.
        div (int/float): The divisor, a number
        by which each element of the matrix will be divided.

    Returns:
        list of list of float: A new matrix with each
        element divided by div and rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
        or if each row of the matrix does not have the same size,
                   or if div is not a number (integer or float).
        ZeroDivisionError: If div is zero.

    Example:
        >>> matrix = [
        ...     [1, 2, 3],
        ...     [4, 5, 6]
        ... ]
        >>> matrix_divided(matrix, 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    """
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
              "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(row)
        elif size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(
                  "matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
