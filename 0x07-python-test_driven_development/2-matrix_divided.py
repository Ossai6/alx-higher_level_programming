#!/usr/bin/python3
""". """

def matrix_divided(matrix, div):
    """. """
    if type(matrix) is list:
        for item in matrix:
            if type(item) is list:
                for elements in item:
                    if type(elements) not in [int, float]:
                        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                        first_row = matrix[0]
                        for row in matrix:
                            if len(row) != len(first_row):
                                raise TypeError("Each row of the matrix must have the same size")
                        if type(div) not in [int or float]:
                                raise TypeError("div must be a number")
                        if div == 0:
                            raise ZeroDivisionError("division by zero")
                        for item in matrix:
                            for elements in item:
                                new_matrix = elements/div
                        return new_matrix

            else:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    else:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
