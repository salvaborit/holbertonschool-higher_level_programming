#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    def bynum(x): return x * number
    new_list = list(map(bynum, my_list))
    return new_list
