#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if (matrix[0]):
        num_lists = len(matrix)
        for i in range(num_lists):
            list_items = len(matrix[i])
            for j in range(list_items):
                if j != list_items - 1:
                    print("{:d} ".format(matrix[i][j]), end='')
                else:
                    print("{:d}".format(matrix[i][j]))
    else:
        print("")
