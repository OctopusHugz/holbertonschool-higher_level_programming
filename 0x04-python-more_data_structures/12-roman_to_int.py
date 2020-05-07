#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    if type(roman_string) != str and type(roman_string) is not None:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for char in roman_string:
        for key, value in roman_dict.items():
            if char == key:
                result += int(value)
    return result
