#!/usr/bin/python3

from dataclasses import asdict


def delete_at(my_list=[], idx=0):
    if idx in range(0, len(my_list)):
        del(my_list[idx])
    return my_list
