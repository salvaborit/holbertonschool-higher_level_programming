#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string is None or str(isinstance(roman_string, str)) is True:
        return None
    roman_dict = {'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for numeral in roman_string:
        if numeral
