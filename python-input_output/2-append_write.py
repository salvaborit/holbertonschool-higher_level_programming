#!/usr/bin/python3
"""Python interpreter"""


def append_write(filename="", text=""):
    """Appends a string to a text file
    Returns: number of characters added"""
    with open(filename, "a") as file:
        write_len = file.write(text)
    return write_len
