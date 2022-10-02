#!/usr/bin/python3
"""Python interpreter"""


from turtle import width
from models.rectangle import Rectangle
"""to make square inherit from rectangle"""


class Square(Rectangle):
    """class: Square (inherits from 'Rectangle')"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)
        self.__size = size
        self.__width = size
        self.__height = size
        self.__x = x
        self.__y = y

    def __str__(self):
            string = '[Square]' + f' ({self.id}) '
            string += f'{self.__x}/{self.__y} - {self.__size}'
            return string
