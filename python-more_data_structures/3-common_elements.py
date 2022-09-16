#!/usr/bin/python3


def common_elements(set_1, set_2):
    common_elems = []
    for elem_1 in set_1:
        for elem_2 in set_2:
            elem_added = False
            for elem_c in common_elems:
                if elem_c is elem_2:
                    elem_added = True
            if elem_1 is elem_2 and elem_added is False:
                common_elems.append(elem_2)
    return common_elems
