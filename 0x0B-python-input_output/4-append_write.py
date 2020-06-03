#!/usr/bin/python3
"""This module implements the append_write function"""


def append_write(filename="", text=""):
    """This function appends the text string to the file filename"""
    with open(filename, "a", encoding="UTF8") as fp:
        fp.write(text)
    return len(text)
