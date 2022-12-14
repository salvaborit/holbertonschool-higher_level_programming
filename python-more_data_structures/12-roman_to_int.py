#!/usr/bin/python3


def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0

    roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,
                      "M": 1000}
    roman_exceptions = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400,
                        "CM": 900}
    sum = 0

    # find idx of exceptions and save in list: (index of exc, "exc literal")
    #                                    list of tuples
    exception_indices = []
    i = 0
    while i < len(roman_string) and i != -1:
        for key in roman_exceptions.keys():
            exception_index = roman_string.find(key)
            if exception_index != -1:
                exception_indices.append((exception_index, key))
                i += 1
            i += 1

    # start adding while taking exceptions into account
    idx = 0
    exception_found = False
    while idx < len(roman_string):
        for e in exception_indices:
            if idx == e[0]:
                sum += roman_exceptions[e[1]]
                exception_found = True
                break
        if exception_found is False:
            sum += roman_numerals[roman_string[idx]]
        idx += 1

    return sum
