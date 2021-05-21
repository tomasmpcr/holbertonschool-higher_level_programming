#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (type(matrix) != list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    new_matrix = []
    largo = -1
    for arr in matrix:
        if (type(arr) != list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if largo != -1:
            if len(arr) != largo:
                raise TypeError("Each row of the matrix must have the same size")
        else:
            largo = len(arr)
        mini_array = []
        for i in arr:
            if type(i) != int and type != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            mini_array.append(round(i / div, 2))
        new_matrix.append(mini_array)
    return (new_matrix)
