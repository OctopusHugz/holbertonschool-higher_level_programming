#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    if matrix:
        for lists in range(len(matrix)):
            new_matrix.append(list(map(lambda x: x * x, matrix[lists])))
    return new_matrix
