#!/usr/bin/python3
"""This module implements the print_square function"""


def print_square(size):
    """The print_square function verifies that parameter provided to
the function is an integer. Then prints a square using that integer as size."""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    rows = 0
    while rows < size:
        cols = 0
        while cols < size:
            print("#", end='')
            cols += 1
        print()
        rows += 1
