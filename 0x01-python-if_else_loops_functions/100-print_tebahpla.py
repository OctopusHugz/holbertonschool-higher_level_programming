#!/usr/bin/python3
j = 0
for i in range(122, 96, -1):
    j += 1
    print("{:c}".format(i) if j % 2 != 0 else "{:c}".format(i - 32), end='')
