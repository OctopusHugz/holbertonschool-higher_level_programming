#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    count = 0
    last_value = 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) != str and type(roman_string) is not None:
        return 0
    for char in roman_string:
        for key, value in roman_dict.items():
            if char == key:
                result += value
                if count == 0:
                    last_value = value
                    count += 1
                    continue
                if last_value < value:
                    result -= last_value
                    result -= last_value
                count += 1
                last_value = value
    return result
