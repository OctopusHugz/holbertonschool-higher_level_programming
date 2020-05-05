#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0 or len(my_list) < idx:
        return new_list
    for i in my_list:
        if i == idx:
            new_list[i] = element
    return new_list
