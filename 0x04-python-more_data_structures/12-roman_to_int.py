#!/usr/bin/python3
def roman_to_int(roman_string):
    new_list = []
    result = 0
    count = 0
    last = 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) != str and type(roman_string) is not None:
        return 0
    for char in roman_string:
        for key, value in roman_dict.items():
            if char == key:
                new_list.append(value)
    first = new_list[0]
    if len(new_list) > 1:
        last = new_list[-1]
    for values in new_list:
        if first > last:
            result += values
    if result == 0:
        for values in reversed(new_list):
            if count == 0 or result == values:
                result += values
            else:
                result -= values
            count += 1
        """ result += int(value)
print(new_list)
print(new_list[-1:])
print(new_list[:1])
if new_list[-1:] > new_list[:1]:
    print("Need to subtract!")
    print("Result is {}".format(result))
    for nums in reversed(new_list):
        print("Nums is {}".format(nums))
        if count != 0:
            diff += nums
            print("Diff is {}".format(diff))
        result -= diff
        count += 1 """
    return result
