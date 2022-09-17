#!/usr/bin/python3


from logging import exception


def safe_print_list(my_list=[], x=0):
    try:
        numbers_printed = 0
        for item in my_list:
            if numbers_printed == x:
                break
            print(item, end='')
            numbers_printed += 1
        print()
        return numbers_printed
    except Exception:
        return numbers_printed
