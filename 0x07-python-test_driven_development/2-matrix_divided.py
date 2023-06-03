def matrix_divided(matrix, div):
    if type(matrix) is list:
        for item in matrix:
            if type(item) is not list:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

            for element in item:
                if type(element) not in [int, float]:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

            if len(item) != len(matrix[0]):
                raise TypeError("Each row of the matrix must have the same size")

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
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

