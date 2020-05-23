#!/usr/bin/python3
"""This module implements matrix division."""


def matrix_divided(matrix, div):
    """This function verifies the parameters and performs matrix division
if valid."""
    new_matrix = [[], []]
    if type(matrix) is not list or len(matrix) < 2:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    elif type(matrix[0]) is not list or type(matrix[1]) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    elif type(div) not in [float, int]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        length = len(matrix[0])
        count = 0
        for lists in matrix:
            if type(lists) is not list:
                raise TypeError(
                    """matrix must be a matrix (list of lists) of
                    integers/floats""")
            if len(lists) != length:  # or not matrix[1]:
                raise TypeError(
                    "Each row of the matrix must have the same size")
            for items in lists:
                if type(items) not in [float, int]:
                    raise TypeError(
                        """matrix must be a matrix (list of lists) of
                        integers/floats""")
                new_item = round(items / div, 2)
                new_matrix[count].append(new_item)
            count += 1
    return new_matrix
