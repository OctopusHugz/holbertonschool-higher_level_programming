#!/usr/bin/python3
from sys import argv
pass
if __name__ == "__main__":
    length = len(argv)
    if length == 1:
        print("0 arguments.")
    if length == 2:
        print("1 argument:\n{:d}: {}".format(length - 1, argv[1]))
    if length > 2:
        print("{:d} arguments:".format(length - 1))
        i = 1
        while i < length:
            print("{:d}: {}".format(i, str(argv[i])))
            i += 1
