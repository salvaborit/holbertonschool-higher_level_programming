#!/usr/bin/python3
"""Python interpreter"""


import json
"""JSON package"""


def load_from_json_file(filename):
    """Creates an object from a JSON file"""
    with open(filename) as json_file:
        new_obj = json.load(json_file)
    return new_obj
