#!/usr/bin/python3
"""This module implements the text_indentation function"""


def text_indentation(text):
    """The text_indentation function verifies that parameter provided to
the function is a string. Then prints a square using that integer as size."""
    if type(text) is not str:
        raise TypeError("text must be a string")
    if text == "":
        print()
        return
    flag = 0
    count = 0
    while count < len(text):
        if flag == 1:
            count += 1
            flag = 0
            continue
        print("{}".format(text[count]), end='')
        if text[count] in {".", "?", ":"}:
            flag = 1
            print("\n")
        count += 1
