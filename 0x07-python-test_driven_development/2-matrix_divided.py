#!/usr/bin/python3
"""2-matrix_divided  module"""


def matrix_divided(matrix, div):
    "function that divides all elements of a matrix."

    new_matrix = []
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
            for num in row:
                if type(num) not in (int, float):
                    raise TypeError(msg)

    for row in matrix:
        if len(row) == len(matrix[0]):
            tmp_lista = []
            for num in row:
                if type(num) not in (int, float):
                    raise TypeError(msg)
                else:
                    tmp_lista.append(round(num / div, 2))
        else:
            raise TypeError("Each row of the matrix must have the same size")

        new_matrix.append(tmp_lista)

    return new_matrix
