#!/usr/bin/python3
"""This module contains the matrix_divided function"""


def matrix_divided(matrix, div):
    """ This function that divides all elements of a matrix
    and returns a new matrix
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    second_error_msg = "Each row of the matrix must have the same size"

    if type(matrix) is list:
        for item in matrix:
            if type(item) is not list:
                raise TypeError(error_msg)

            for element in item:
                if type(element) not in [int, float]:
                    raise TypeError(error_msg)

            if len(item) != len(matrix[0]):
                raise TypeError(second_error_msg)

        if type(div) not in [int, float]:
            raise TypeError("div must be a number")

        if div == 0:
            raise ZeroDivisionError("division by zero")

        new_matrix = []
        for row in matrix:
            new_row = []
            for element in row:
                result = round((element / div), 2)
                new_row.append(result)
            new_matrix.append(new_row)

        return new_matrix

    else:
        raise TypeError(error_msg)
