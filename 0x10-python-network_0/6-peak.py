#!/usr/bin/python3
"""This module contains a peak finding function"""
def find_peak(list_of_integers):
    """This function finds a peak in a list of unsorted integers"""
    if list_of_integers:
        if list_of_integers[0] > list_of_integers[1]:
            return list_of_integers[0]
        elif list_of_integers[-1] > list_of_integers[-2]:
            return list_of_integers[-1]
        for index in range(1, len(list_of_integers) - 1):
            prev_num = list_of_integers[index - 1]
            curr_num = list_of_integers[index]
            next_num = list_of_integers[index + 1]
            if curr_num > prev_num and curr_num > next_num:
                return curr_num
            elif curr_num == prev_num and curr_num > next_num:
                return curr_num
            elif curr_num == next_num and curr_num > prev_num:
                return curr_num
            elif prev_num == curr_num == next_num:
                return curr_num
