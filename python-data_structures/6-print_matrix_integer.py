#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    r = len(matrix)
    c = len(matrix[0]) if matrix else 0

    for r in matrix:
        for i, element in enumerate(r):
            if i == c - 1:
                print("{:d}".format(element), end='')
            else:
                print("{:d}".format(element), end=' ')
        print()
