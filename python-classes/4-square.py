#!/usr/bin/python3
""" Python interpreter """


class Square:
    """ class: Square """

    def __init__(self, size):
        if type(size) is not int:
            raise TypeError('size must be >= 0')
        if size < 0:
            raise(ValueError('size must be >= 0'))
