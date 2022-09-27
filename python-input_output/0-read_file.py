#!/usr/bin/python3
"""Python interpreter"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as file:
        buffer = file.read()
    print(buffer)
