#!/usr/bin/python3
"""Python interpreter"""


from operator import not_


class Student:
    """class: Student"""

    def __init__(self, first_name, last_name, age):
        """Constructor"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""

        if attrs is None or type(attrs) is not list:
            return self.__dict__
        for item in attrs:
            if type(item) is not str:
                return self.__dict__

        keys = list(self.__dict__.keys())
        set_keys = set(keys)
        set_attrs = set(attrs)

        if len(set_keys.intersection(set_attrs)) > 0:
            common_keys = list(set_keys.intersection(set_attrs))
        else:
            return self.__dict__

        new_dict = {}
        for key in common_keys:
            new_dict[key] = self.__dict__[key]
        return new_dict
