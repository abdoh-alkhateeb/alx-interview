#!/usr/bin/python3
"""
Defines `rotate_2d_matrix`.
"""

from typing import List


def rotate_2d_matrix(matrix: List[List[int]]):
    """
    Rotates a matrix 90 degrees clockwise.
    """
    n = len(matrix)

    rotated_matrix = []

    for i in range(n):
        row = []

        for j in range(n - 1, -1, -1):
            row.append(matrix[j][i])

        rotated_matrix.append(row)

    for i in range(n):
        for j in range(n):
            matrix[i][j] = rotated_matrix[i][j]
