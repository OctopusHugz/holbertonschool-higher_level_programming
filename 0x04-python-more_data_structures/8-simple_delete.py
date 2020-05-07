#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_dict = a_dictionary.copy()
    for keys in a_dictionary:
        if keys == key:
            del new_dict[keys]
    return new_dict
