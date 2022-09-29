#!/usr/bin/python3
"""Python interpreter"""


def pascal_triangle(n):
    """Returns a list of lists of ints representing Pascal's triangle (n)"""
    if n <= 0:
        return []

    triangle = []
    for outer in range(n):
        list = []

        if outer < 2:
            for x in range(outer + 1):
                list.append(1)
            triangle.append(list)
            prev_list = list.copy()
            continue

        for i in range(outer + 1):
            if i == 0 or i == outer:
                list.append(1)
                continue

            try:
                idx_0 = prev_list[i - 1]
            except IndexError:
                idx_0 = 0
            try:
                idx_1 = prev_list[i]
            except IndexError:
                idx_1 = 0
            if idx_0 == 0 and idx_1 == 0:
                sum = 1
            else:
                sum = idx_0 + idx_1
            list.append(sum)

        prev_list = list.copy()
        triangle.append(list)
    return triangle
