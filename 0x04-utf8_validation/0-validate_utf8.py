#!/usr/bin/python3
"""
Defines `validUTF8`.
"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Returns True if data is a valid UTF-8 encoding, else return False.
    """
    if not data:
        return True

    def is_byte_invalid(data):
        return data.pop(0) >> 6 != 2

    while data:
        byte = data.pop(0) & 255

        try:
            if byte >> 7 == 0:
                pass
            elif byte >> 5 == 0b110:
                if is_byte_invalid(data):
                    return False
            elif byte >> 4 == 0b1110:
                for _ in range(2):
                    if is_byte_invalid(data):
                        return False
            elif byte >> 3 == 0b11110:
                for _ in range(3):
                    if is_byte_invalid(data):
                        return False
            else:
                return False
        except IndexError:
            return False

    return True
