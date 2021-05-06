#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for sec_matrix in matrix:
        sec_new_matrix = []
        for item in sec_matrix:
            sec_new_matrix.append(item ** 2)
        new_matrix.append(sec_new_matrix)
    return (new_matrix)
