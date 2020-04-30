#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    length = len(argv)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] != '+' and argv[2] != '-' and argv[2] != '*' and argv[2] != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    num1 = int(argv[1])
    num2 = int(argv[3])
    if argv[2] == '+':
        print("{:d} + {:d} = {:d}".format(num1, num2, add(num1, num2)))
    if argv[2] == '-':
        print("{:d} - {:d} = {:d}".format(num1, num2, sub(num1, num2)))
    if argv[2] == '*':
        print("{:d} * {:d} = {:d}".format(num1, num2, mul(num1, num2)))
    if argv[2] == '/':
        print("{:d} / {:d} = {:d}".format(num1, num2, div(num1, num2)))
