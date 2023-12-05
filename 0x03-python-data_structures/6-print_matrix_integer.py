#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for r in range(len(matrix[0])):
            print("{:d}".format(matrix[row][r]), end='')
            if r + 1 < len(matrix[0]):
                print(" ", end="")

        print()
