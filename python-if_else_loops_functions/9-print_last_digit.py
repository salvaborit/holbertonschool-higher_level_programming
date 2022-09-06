#!/usr/bin/python3


def print_last_digit(number):
    number_u = number * -1
    if number < 0:
        print(f"{number_u % 10}", end="")
        return number_u % 10
    elif number > 0:
        print(f"{number % 10}", end="")
        return number % 10
    else:
        print(f"{number}", end="")
        return number