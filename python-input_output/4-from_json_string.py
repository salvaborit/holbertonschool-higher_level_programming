#!/usr/bin/python3
"""Python interpreter"""

import json
"""JSON module"""


def from_json_string(my_str):
    """Returns an Python object represented by a JSON string"""
    return json.loads(my_str)
