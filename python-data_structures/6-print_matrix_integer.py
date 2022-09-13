#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
        return
    for row in matrix:
        idx = 0
        for i in row:
            print("{:d}".format(i), end=" " if idx < len(row) - 1 else "\n")
            idx += 1
