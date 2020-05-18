#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for items in my_list:
        try:
            if count < x:
                print("{}".format(items), end='')
                count += 1
        except IndexError as ie:
            print(ie)
    print()
    return count
