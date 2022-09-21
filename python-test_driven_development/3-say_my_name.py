#!/usr/bin/python3
"""Python interpreter"""


from typing import Type


def say_my_name(first_name, last_name=""):
    """
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print(f"my name is {first_name} {last_name}")
