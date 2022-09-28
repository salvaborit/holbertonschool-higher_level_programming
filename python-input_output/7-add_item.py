#!/usr/bin/python3
"""Python interpreter"""


import sys, json
"""sys module"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == '__main__':
    json_list = []
    filename = 'add_item.json'
    try:
        json_list = load_from_json_file(filename)
    except Exception:
        pass
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            json_list.append(arg)
        save_to_json_file(json_list, filename)
