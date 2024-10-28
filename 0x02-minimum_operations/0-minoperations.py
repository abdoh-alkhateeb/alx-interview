#!/usr/bin/python3
"""
Defines `minOperations`.
"""


def minOperations(n: int) -> int:
    """
    Calculates the minimum number of operations required to reach `n`
    starting from 1, using only two operations: Copy All and Paste.

    Parameters:
    n (int): Target number of characters.

    Returns:
    int: Fewest number of operations needed, or 0 if `n` is less than 2.
    """
    if type(n) is not int or n < 2:
        return 0

    x = 2
    factors = []

    while n > 1:
        if n % x == 0:
            factors.append(x)
            n //= x
        else:
            x += 1

    return sum(factors)
