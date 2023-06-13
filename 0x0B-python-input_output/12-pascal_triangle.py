#!/usr/bin/python3
"""
    This module contains the pascal_triangle function
"""


def pascal_triangle(n):
    """
        returns the pascals triangle of n in a list of lists
    """
    if n <= 0:
        return []

    result = []
    for i in range(n):
        row = []
        for j in range(i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(result[i-1][j-1] + result[i-1][j])
        result.append(row)

    return result
