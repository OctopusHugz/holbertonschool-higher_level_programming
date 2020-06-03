#!/usr/bin/python3
"""This module implements the write_file function"""


def write_file(filename="", text=""):
    """This function writes the text string to the file filename"""
    with open(filename, "w", encoding="UTF8") as fp:
        fp.write(text)
    return len(text)
