#!/usr/bin/python3
"""
Defines `pascal_triangle`.
"""

from typing import List


def pascal_triangle(n: int) -> List[int]:
    """
    Returns Pascal's triangle.
    """

    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        level = []

        for j in range(i + 1):
            if j == 0 or j == i:
                level.append(1)
            elif i > 0 and j > 0:
                level.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        triangle.append(level)

    return triangle
