#!/usr/bin/python3
"""This module implements the read_lines function"""
number_of_lines = __import__('1-number_of_lines').number_of_lines


def read_lines(filename="", nb_lines=0):
    """This function reads nb_lines number of lines from the
provided file"""
    num_lines = number_of_lines(filename)
    count = 0
    if nb_lines <= 0 or nb_lines > num_lines:
        nb_lines = num_lines
    with open(filename, encoding="UTF8") as fp:
        while count < nb_lines:
            line = fp.readline()
            if not line:
                break
            print(line, end='')
            count += 1
