#!/usr/bin/python3
"""Python interpreter"""


import json
"""JSON package"""


def save_to_json_file(my_obj, filename):
    """Serializes an object to a text file"""
    with open(filename, 'a') as file:
        json.dump(my_obj, file)
