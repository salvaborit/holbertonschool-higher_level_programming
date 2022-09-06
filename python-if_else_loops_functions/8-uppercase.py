#!/usr/bin/python3
# prints a string in uppercase


def uppercase(str):
    x = len(str)
    for i in str:
        if i >= 'a' and i <= 'z':
            i = chr(ord(i) - 32)
        print("{:s}".format(i), end=("\n" if x < 2 else ""))
        x -= 1
