#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = []
    result = 0
    for i in my_list:
        if i not in uniq_list:
            result += i
            uniq_list.append(i)
    return result
