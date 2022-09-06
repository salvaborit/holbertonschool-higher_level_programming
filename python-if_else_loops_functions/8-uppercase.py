#!/usr/bin/python3
# prints a string in uppercase


def uppercase(str):
    x = len(str)
    for i in range(0, x):
        a = ord(str[i])
        if a > 96 and a < 123:
            print("{}".format(chr(a - 32)), end=("\n" if i == x - 1 else ""))
        else:
            print("{}".format(str[i]), end=("\n" if i == x - 1 else ""))
