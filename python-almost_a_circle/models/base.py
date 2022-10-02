#!/usr/bin/python3
"""Python interpreter"""


import json
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
            return '[]'
        return json.dumps(list_dictionaries)
