#!/usr/bin/python3


def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0

    main = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    exc = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    exc_keys = exc.keys()
    sum = 0

    # find idx of exceptions and save in list: (index of exc, "exc literal")
    #                                    list of tuples
    exc_indexes = []
    start = 0
    while start < len(roman_string) and start != -1:
        for key in exc_keys:
            exc_index = roman_string.find(key)
            if exc_index != -1:
                exc_indexes.append((exc_index, key))
            start += 1

    # start adding while taking exceptions into account
    roman_idx = 0
    exc_found = False
    while roman_idx < len(roman_string):
        for exc_idx in exc_indexes:
            if roman_idx == exc_idx[0]:
                sum += exc[exc_idx[1]]
                exc_found = True
                break
        if exc_found is False:
            sum += main[roman_string[roman_idx]]
        roman_idx += 1

    return sum
