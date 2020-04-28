#!/usr/bin/python3
for i in range(0, 100):
    if i < 99:
        print("0{:d}, ".format(i) if i < 10 else "{:d}, ".format(i), end='')
    else:
        print("{:d}".format(i))
