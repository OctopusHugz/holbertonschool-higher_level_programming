#!/usr/bin/python3
"""This module implements the read_file function"""


def read_file(filename=""):
    """This function reads the provided file"""
    with open(filename, encoding="UTF8") as fp:
        text = fp.read()
    print(text, end='')
