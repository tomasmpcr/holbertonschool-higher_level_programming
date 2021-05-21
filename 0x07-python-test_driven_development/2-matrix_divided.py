#!/usr/bin/python3
"""
    Function div matrix
    Fun:
        matrix_divided
"""


def matrix_divided(matrix, div):
    """
        Fun create a new matrix/div
    """
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg2 = "Each row of the matrix must have the same size"
    if (type(matrix) != list):
        raise TypeError(msg1)
    new_matrix = []
    largo = -1
    for arr in matrix:
        if (type(arr) != list):
            raise TypeError(msg1)
        if largo != -1:
            if len(arr) != largo:
                raise TypeError(msg2)
        else:
            largo = len(arr)
        mini_array = []
        for i in arr:
            if type(i) != int and type != float:
                raise TypeError(msg1)
            mini_array.append(round(i / div, 2))
        new_matrix.append(mini_array)
    return (new_matrix)
