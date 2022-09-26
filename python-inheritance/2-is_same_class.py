#!/usr/bin/python3
"""Python interpreter"""


def is_same_class(obj, a_class):
    """Returns True if object is exactly an instance of specified class"""
    return True if type(obj) is a_class else False
