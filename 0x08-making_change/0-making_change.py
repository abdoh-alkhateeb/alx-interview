#!/usr/bin/python3
"""
Defines `makeChange`.
"""

from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Returns fewest number of coins needed to meet `total`.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    result = 0

    for coin in coins:
        if coin <= total:
            n = total // coin
            result += n
            total -= coin * n

        if total == 0:
            return result

    return -1
