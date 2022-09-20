#!/usr/bin/python3
"""Python interpreter"""


def matrix_divided(matrix, div):
    """Divides a matrix by a number
    Args:
        matrix (list of lists): have to measure the same, only numbers
        div (int): number to divide matrix items by
    """
    row_num = 0
    for row in matrix:
        if row_num != 0 and len(row) != row_length:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        row_length = len(row)
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        row_num += 1

    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError(' division by zero')

    new_matrix = []
    for row in matrix:
        new_list = []
        for item in row:
            new_list.append(round(item / div, 2))
        new_matrix.append(new_list)

    return new_matrix
