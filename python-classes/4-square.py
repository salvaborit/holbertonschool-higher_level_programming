#!/usr/bin/python3
""" Python interpreter """


class Square:

    def __init__(self, size=0):
        """On instantiation
        Args:
            size (int): size of square
        """
        if type(size) is not int:
            raise TypeError('size must be >= 0')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Gets size of instance"""
        return self.__size
    @size.setter
    def size(self, value):
        """Sets size of instance
        Args:
            value (int): value to assign to __size of instance
        """
        if type(value) is not int:
            raise TypeError('size must be >= 0')
        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """Returns area of instance (square)"""
        return self.__size * self.__size
