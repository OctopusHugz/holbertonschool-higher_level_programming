#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
if number < 0:
    ld = -ld
print("Last digit of {:d} is {:d} and is ".format(number, ld), end='')
print("greater than 5" if ld > 5 else "0"
      if ld == 0 else "less than 6 and not 0")
