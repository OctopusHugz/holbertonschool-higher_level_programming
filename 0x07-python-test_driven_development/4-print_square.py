#!/usr/bin/python3
def print_square(size):
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
