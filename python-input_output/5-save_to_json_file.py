#!/usr/bin/python3
"""Python interpreter"""


import json
"""JSON package"""


def save_to_json_file(my_obj, filename):
    """Serializes an object to a text file"""
    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
