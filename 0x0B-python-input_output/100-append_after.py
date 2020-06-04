#!/usr/bin/python3
"""This module implements the append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """This function appends the new_string after the search_string
is found in the file filename """
    line_num = 0
    with open(filename, "r+") as fp:
        while True:
            line = fp.readlines()
            line_num += 1
            if not line:
                break
            if search_string in line:
                fp.insert(line_num + 1, new_string)
