#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        j = ord(str[i]) - 32
        print("{}".format(chr(j)) if ord(str[i]) >= 97 and ord(
            str[i]) <= 122 else "{}".format(str[i]), end='')
    print("")
