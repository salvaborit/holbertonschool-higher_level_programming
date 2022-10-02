#!/usr/bin/python3
"""Python interpreter"""


from fileinput import filename
import json
from typing import Dict, List
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
        json_list = []
        if list_objs is None:
            with open(filename, 'w') as file:
                file.write(json.dumps(json_list))
        for instance in list_objs:
            json_list.append(cls.to_json_string(instance.to_dictionary()))
        with open(filename, 'w') as file:
                file.write(str(json_list))
