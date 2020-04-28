#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
neg_flag = 0
if number < 0:
    neg_flag = 1
ld = abs(number) % 10
if neg_flag == 1:
    ld = -ld
print("Last digit of {:d} is {:d} and is ".format(number, ld), end='')
if ld > 5:
    print("greater than 5")
elif ld == 0:
    print("0")
elif ld != 0 and ld < 6:
    print("less than 6 and not 0")
