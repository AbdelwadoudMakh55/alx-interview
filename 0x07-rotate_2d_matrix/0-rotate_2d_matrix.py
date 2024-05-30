#!/usr/bin/python3
"""
Rotate a 2D Matrix by 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """Function that rotates a 2D Matrix"""
    length = len(matrix[0])
    # Transpose the 2D matrix
    for i in range(length):
        for j in range(i, length):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
        # Reverse
        matrix[i].reverse()
