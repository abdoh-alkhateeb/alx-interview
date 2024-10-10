#!/usr/bin/python3
"""
Defines `canUnlockAll`.
"""

from collections import deque
from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Returns True if the boxes can all be unlocked.
    """

    if not boxes:
        return True

    is_open = [False for _ in range(len(boxes))]
    is_open[0] = True

    to_check = deque([0])

    while to_check:
        keys = boxes[to_check.popleft()]

        for key in keys:
            try:
                if is_open[key]:
                    continue

                is_open[key] = True
                to_check.append(key)
            except IndexError:
                pass

    return all(is_open)
