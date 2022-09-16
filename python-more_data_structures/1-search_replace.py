#!/usr/bin/python3

# @my_list: is the initial list
# @search: is the element to replace in the list
# @replace: is the new element


def search_replace(my_list, search, replace):
    new_list = []
    for elem in my_list:
        if elem is search:
            new_list.append(replace)
        else:
            new_list.append(elem)
    return new_list
