#!/usr/bin/python3
"""This module implements the number_of_lines function"""


def number_of_lines(filename=""):
    """This function reads from the provided file and counts the
number of lines"""
    count = 0
    with open(filename, "r") as fp:
        text = fp.read()
    for chars in text:
        if chars == "\n":
            count += 1
    return count
