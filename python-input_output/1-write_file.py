#!/usr/bin/python3
"""Python interpreter"""


def write_file(filename="", text=""):
    """Writes a str to a text file and returns characters written"""
    with open(filename, "w+") as file:
        file.write(text)
    return len(text)
