#!/usr/bin/python3
"""
Defines `island_perimeter`.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    m = len(grid)
    n = len(grid[0])

    perimeter = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                perimeter += 4

                if i < m - 1 and grid[i + 1][j] == 1:
                    perimeter -= 2

                if j < n - 1 and grid[i][j + 1] == 1:
                    perimeter -= 2

    return perimeter
