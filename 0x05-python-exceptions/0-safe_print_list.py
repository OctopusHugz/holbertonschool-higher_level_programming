#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    length = 0
    while length < x:
        try:
            print("{}".format(my_list[length]), end='')
            count += 1
            length += 1
        except:
            length += 1
    print()
    return count
