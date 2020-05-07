#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    count = 0
    if matrix:
        for element in matrix:
            new_matrix.append(list(map(lambda x: x * x, matrix[count])))
            count += 1
    return new_matrix
