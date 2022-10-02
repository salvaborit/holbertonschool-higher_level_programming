#!/usr/bin/python3
"""Python interpreter"""


from models.rectangle import Rectangle
"""to make square inherit from rectangle"""


class Square(Rectangle):
    """class: Square (inherits from 'Rectangle')"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
            string = '[Square]' + f' ({self.id}) '
            string += f'{self.__x}/{self.__y} - {self.__width}'
            return string

    """SIZE s/g"""
    @property
    def size(self):
        """Getter"""
        return super().width

    @size.setter
    def size(self, value):
        """Setter"""
        super().type_validator("width", value)
        super().wh_validator("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates instance attributes"""
        if len(args) == 0:
            for key in kwargs:
                if key == 'size':
                    self.width = kwargs.get(key)
                    self.height = kwargs.get(key)
                if key == 'id':
                    self.id = kwargs.get(key)
                if key == 'x':
                    self.x = kwargs.get(key)
                if key == 'y':
                    self.y = kwargs.get(key)
        else:
            for num, arg in enumerate(args):
                if num == 0:
                    self.id = arg
                if num == 1:
                    self.width = arg
                    self.height = arg
                if num == 2:
                    self.x = arg
                if num == 3:
                    self.y = arg
