#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for full_row in matrix:
        idx = 0
        for i in full_row:
            print("{:d}".format(i), end=" " if idx < 2 else "\n")
            idx += 1
