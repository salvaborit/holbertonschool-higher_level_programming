#!/usr/bin/python3
"""Python interpreter"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class: Rectangle (inherits from 'BaseGeometry')"""
    def __init__(self, width, height):
        """Constructor"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f'[Rectangle] {self.__width}/{self.__height}'
