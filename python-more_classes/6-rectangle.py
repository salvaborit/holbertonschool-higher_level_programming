#!/usr/bin/python3
"""Python interpreter"""


class Rectangle:
    """class: Rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """On instantiation"""

        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')

        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        string = ""
        for row in range(self.__height):
            if row > 0:
                string += '\n'
            for col in range(self.__width):
                string += '#'
        return string

    def __repr__(self):
        string = "Rectangle(" + str(self.__width) + ", "
        string += str(self.__height) + ")"
        return string

    def __del__(self):
        print('Bye rectangle...')
        type(self).number_of_instances -= 1
