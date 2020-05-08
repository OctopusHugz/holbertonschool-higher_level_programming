#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = a_dictionary.copy()
    for key, values in new_dict.items():
        if values == value:
            a_dictionary.pop(key, new_dict)
    return a_dictionary
