#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    printed_items = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end='')
            printed_items += 1
        except(TypeError, ValueError):
            pass
    print()
    return printed_items
