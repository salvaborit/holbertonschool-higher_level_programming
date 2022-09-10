#!/usr/bin/python3


for letter in range(122, 96, -1):
    print("{}".format(chr(letter - 32) if letter % 2 != 0
          else chr(letter)), end="")
