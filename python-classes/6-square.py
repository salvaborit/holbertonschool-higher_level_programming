#!/usr/bin/python3
""" Python interpreter """


class Square:
    """On instantiation
    Args:
        size (int): size of square
    """

    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        if type(position) != tuple or not position[0] or not position[1]:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Gets size of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets size of position
        Args:
            value (tuple): a tuple of 2 positive ints
        """
        if type(value) is not tuple or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    def area(self):
        """Returns area of instance (square)"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with # (hashbangs)"""
        if self.__size == 0:
            print()
            return

        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print()

        for row in range(self.__size):
            if self.__position[0] > 0:
                for i in range(self.__position[0]):
                    print(' ', end='')
            for cols in range(self.__size):
                print("#", end='' if cols < self.__size - 1 else '\n')
