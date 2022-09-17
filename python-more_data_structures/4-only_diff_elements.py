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


def only_diff_elements(set_1, set_2):

    common_elems = common_elements(set_1, set_2)
    diff_elems = []

    for elem_1 in set_1:
        # check if element is a common element
        pair_found = False
        for elem_c in common_elems:
            if elem_1 is elem_c:
                pair_found = True
        # check if element has already been added to list to return
        already_added = False
        for elem_d in diff_elems:
            if elem_1 is elem_d:
                already_added = True

        if pair_found is False and already_added is False:
            diff_elems.append(elem_1)

    for elem_2 in set_2:
        # check if element is a common element
        pair_found = False
        for elem_c in common_elems:
            if elem_2 is elem_c:
                pair_found = True
        # check if element has already been added to list to return
        already_added = False
        for elem_d in diff_elems:
            if elem_2 is elem_d:
                already_added = True

        if pair_found is False and already_added is False:
            diff_elems.append(elem_2)

    return diff_elems
