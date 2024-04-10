#!/usr/bin/python3
"""
Pascal's triangle
"""


def pascal_triangle(n):
    """ Pascal's triangle """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(0, n - 1):
        row = [1]
        for j in range(len(triangle[-1]) - 1):
            row.append(triangle[-1][j] + triangle[-1][j + 1])
        row.append(1)
        triangle.append(row)
    return triangle
