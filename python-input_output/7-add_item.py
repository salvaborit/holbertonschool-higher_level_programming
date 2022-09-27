#!/usr/bin/python3
"""Python interpreter"""



import os.path, sys, json
"""sys module"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == '__main__':
    json_list = []
    if os.path.exists('add_item.json'):
        with open('add_item.json') as file:
            json_list = load_from_json_file('add_item.json')

    for i in range(1, len(sys.argv)):
        json_list.append(sys.argv[i])

    save_to_json_file(json_list, 'add_item.json')
