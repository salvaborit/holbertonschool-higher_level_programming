#!/usr/bin/python3
"""Python interpreter"""


from models.base import Base


class Rectangle(Base):
    """class: Rectangle (inherits from 'Base')"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y


    """WIDTH s/g"""
    @property
    def width(self):
        """Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter"""
        self.__width = value


    """HEIGHT s/g"""
    @property
    def height(self):
        """Getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter"""
        self.__height = value


    """X s/g"""
    @property
    def x(self):
        """Getter"""
        return self.__x

    @height.setter
    def x(self, value):
        """Setter"""
        self.__x = value


    """Y s/g"""
    @property
    def y(self):
        """Getter"""
        return self.__y

    @height.setter
    def y(self, value):
        """Setter"""
        self.__y = value
