#!/usr/bin/python3
"""
This module provides functionality to generate
Pascal's Triangle up to a specified number of rows.
Pascal's Triangle is a mathematical table of binomial coefficients
arranged in a triangular form. Each coefficient is the number of ways to choose
an element from a set, making it useful
in probability calculations and algebra.

The main function in this module, `pascal_triangle`,
computes the rows of Pascal's Triangle using a simple iterative approach.
This function is useful for educational purposes
to demonstrate the properties of
binomial coefficients, and it can also serve as a utility for
algorithms that require quick access to these coefficients.
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.

    Pascal's Triangle is a triangular array
    of the binomial coefficients. This function
    builds the triangle by starting with the top
    of the triangle and iteratively adding
    rows. Each number in the triangle is the sum
    of the two numbers directly above it
    on the previous row.

    Args:
        n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        list: A list of lists,
        where each inner list represents a row of Pascal's Triangle.
    """
    triangle = []  # This will store each row of the triangle
    for i in range(n):
        row = [1]  # Every row starts with 1
        if triangle:  # Check if there is at least one row already
            last_row = triangle[-1]  # Get the last row from the triangle
            row.extend([last_row[j] + last_row[j + 1]
                        for j in range(len(last_row) - 1)])
            row.append(1)  # Every row ends with 1
        triangle.append(row)  # Add the completed row to the triangle
    return triangle

# Example usage:
# print(pascal_triangle(5))
