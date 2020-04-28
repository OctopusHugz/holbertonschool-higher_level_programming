#!/usr/bin/python3
for i in range(0, 10):
    for j in range(1, 10):
        if j > i and i != 8:
            print("{:d}".format(i), end='')
            print("{:d}, ".format(j), end='')
        elif i == 8 and j == 9:
            print("89")
