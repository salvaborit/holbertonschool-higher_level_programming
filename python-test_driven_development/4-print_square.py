#!/usr/bin/python3
"""Python interpreter"""


def print_square(size):
    """Prints a square of hashbangs (#)"""

    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')

    for row in range(size):
        for col in range(size):
            print("#", end='' if col != size - 1 else '\n')
