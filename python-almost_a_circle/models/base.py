#!/usr/bin/python3
"""Python interpreter"""


import json, os.path
"""JSON package"""


class Base:
    """class: Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Serialize JSON to string"""
        if list_dictionaries is None:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Serialize JSON to file"""
        filename = f'{cls.__name__}.json'
        if list_objs is None:
            with open(filename, 'w') as file:
                file.write('[]')
            return
        string = '['
        for num, instance in enumerate(list_objs):
            if num != 0:
                string += ", "
            string += cls.to_json_string(instance.to_dictionary())
        string += ']'
        with open(filename, 'w') as file:
                file.write(string)

    @staticmethod
    def from_json_string(json_string):
        """Returns list of JSON string representation"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            new_instance = cls(10, 10)
        if cls.__name__ == 'Square':
            new_instance = cls(10)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """Returns list of instances"""
        filename = cls.__name__ + '.json'
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as file:
            file_contents = file.read()
        instances = cls.from_json_string(file_contents)
        lst = []
        for dict in instances:
            lst.append(cls.create(**dict))
        return lst
