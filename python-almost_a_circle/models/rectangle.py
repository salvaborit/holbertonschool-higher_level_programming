#!/usr/bin/python3
"""Python interpreter"""


from models.base import Base
"""to be able to inherit Base to Ractangle"""


class Rectangle(Base):
    """class: Rectangle (inherits from 'Base')"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)

        self.type_validator("width", width)
        self.type_validator("height", height)
        self.type_validator("x", x)
        self.type_validator("y", y)
        self.wh_validator("width", width)
        self.wh_validator("height", height)
        self.xy_validator("x", x)
        self.xy_validator("y", y)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def type_validator(self, name, value):
        """Type validator (must be int)"""
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')

    def wh_validator(self, name, value):
        """Width/height validator (greater than 0)"""
        if value <= 0:
            raise ValueError(f'{name} must be > 0')

    def xy_validator(self, name, value):
        """X/Y validator (positive)"""
        if value < 0:
            raise ValueError(f'{name} must be >= 0')

    """WIDTH s/g"""
    @property
    def width(self):
        """Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter"""
        self.type_validator("width", value)
        self.wh_validator("width", value)
        self.__width = value

    """HEIGHT s/g"""
    @property
    def height(self):
        """Getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter"""
        self.type_validator("height", value)
        self.wh_validator("height", value)
        self.__height = value

    """X s/g"""
    @property
    def x(self):
        """Getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter"""
        self.type_validator("x", value)
        self.xy_validator("x", value)
        self.__x = value

    """Y s/g"""
    @property
    def y(self):
        """Getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter"""
        self.type_validator("y", value)
        self.xy_validator("y", value)
        self.__y = value

    def area(self):
        """Returns area of instance"""
        return self.__width * self.__height

    def display(self):
        """Prints a rectangle of hashbangs (#) to stdout"""
        for i in range(self.__y):
            print()
        for row in range(self.__height):
            for i in range(self.__x):
                print(' ', end='')
            for cols in range(self.__width):
                print('#', end='' if cols != self.__width - 1 else '\n')

    def __str__(self):
        string = '[Rectangle]' + f' ({self.id}) '
        string += f'{self.__x}/{self.__y} - {self.__width}/{self.__height}'
        return string

    def update(self, *args, **kwargs):
        """Updates instance attributes"""
        if len(args) != 0:
            for num, arg in enumerate(args):
                if num == 0:
                    self.id = arg
                if num == 1:
                    self.__width = arg
                if num == 2:
                    self.__height = arg
                if num == 3:
                    self.__x = arg
                if num == 4:
                    self.__y = arg
        else:
            for key in kwargs:
                if key == 'id':
                    self.id = kwargs.get(key)
                if key == 'width':
                    self.__width = kwargs.get(key)
                if key == 'height':
                    self.__height = kwargs.get(key)
                if key == 'x':
                    self.__x = kwargs.get(key)
                if key == 'y':
                    self.__y = kwargs.get(key)
