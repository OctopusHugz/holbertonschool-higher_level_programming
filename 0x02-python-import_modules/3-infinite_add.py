#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    length = len(argv)
    if length == 1:
        print("0")
    if length == 2:
        print(argv[1])
    if length > 2:
        i = 1
        result = 0
        while i < length:
            num = int(argv[i])
            result += num
            i += 1
        print(result)
