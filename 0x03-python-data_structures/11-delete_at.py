#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list:
        new_list = my_list
        if idx < 0 or len(my_list) - 1 < idx:
            return my_list
        elif idx == 0:
            new_list.remove(new_list[0])
        else:
            count = 0
            for i in new_list:
                if count == idx - 1:
                    new_list.remove(new_list[i])
                count += 1
    return new_list
