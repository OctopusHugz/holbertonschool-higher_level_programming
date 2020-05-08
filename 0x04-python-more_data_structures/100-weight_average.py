#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        numerator = 0
        denominator = 0
        for tuples in my_list:
            result = 1
            count = 0
            for nums in tuples:
                if count == 1:
                    denominator += nums
                result *= nums
                count += 1
            numerator += result
        average = numerator / denominator
    else:
        average = 0
    return average
