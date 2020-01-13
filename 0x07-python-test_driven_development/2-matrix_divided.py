#!/usr/bin/python3
def matrix_divided(matrix, div):
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) not in (int, float):
        raise TypeError(msg)

    for row in matrix:
        if len(row) == len(matrix[0]):
            pass
        else:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
