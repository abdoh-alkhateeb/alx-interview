#!/usr/bin/python3
"""
Solves the N queens problem.
"""

import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

solutions = []


def is_valid(solution):
    if len(solution) == 0:
        return True

    last_row, last_col = solution[-1]

    for row, col in solution[:-1]:
        if col == last_col:
            return False

        if abs(last_row - row) == abs(last_col - col):
            return False

    return True


def backtrack(index, solution):
    if not is_valid(solution):
        return

    if index == n:
        solutions.append(solution)
        return

    for i in range(n):
        backtrack(index + 1, [*solution, [index, i]])


backtrack(0, [])

for solution in solutions:
    print(solution)
