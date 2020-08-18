#!/usr/bin/python3
"""This module contains a peak finding function"""
def find_peak(list_of_integers):
    """This function finds a peak in a list of unsorted integers"""
    if list_of_integers:
        return max(list_of_integers)
