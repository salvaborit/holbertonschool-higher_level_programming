#!/usr/bin/python3
""" Python interpreter """


class Square:
    """On instantiation
    Args:
        size (int): size of square
    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
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
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """Returns area of instance (square)"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with # (hashbangs)"""
        if self.__size == 0:
            print()
            return
        for i in range(0, self.__size):
            for i in range(0, self.__size):
                print(f"#", end='' if i < self.__size - 1 else '\n')
