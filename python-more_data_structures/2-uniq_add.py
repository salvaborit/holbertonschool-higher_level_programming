#!/usr/bin/python3


def uniq_add(my_list=[]):
    uniq_addends = []
    sum = 0
    for elem in my_list:
        addend_found = False
        for addend in uniq_addends:
            if elem is addend:
                addend_found = True
        if addend_found is False:
            uniq_addends.append(elem)
            sum += elem
    return sum
