#!/usr/bin/python3
"""
Solution for utf-8 validation problem
"""
from typing import List


def check_subsequent_bytes(data: List[int], j: int, sub: int) -> bool:
    """ Check the subsequent bytes """
    i = 0
    while i < sub and j < len(data):
        if not ((data[j] & (1 << 7)) != 0 and (data[j] & (1 << 6)) == 0):
            return False
        i += 1
        j += 1
    if i != sub:
        return False
    return True


def validUTF8(data: List[int]) -> bool:
    """ Validate UTF-8 encoding """
    j = 0
    while j < len(data):
        i = 7
        if (data[j] & (1 << i)) == 0:
            j += 1
        elif (data[j] & (1 << i)) != 0:
            i -= 1
            if (data[j] & (1 << i)) != 0:
                i -= 1
                if (data[j] & (1 << i)) == 0:
                    j += 1
                    result = check_subsequent_bytes(data, j, 1)
                    j += 1
                    if not result:
                        return False
                elif (data[j] & (1 << i)) != 0:
                    i -= 1
                    if (data[j] & (1 << i)) == 0:
                        j += 1
                        result = check_subsequent_bytes(data, j, 2)
                        j += 2
                        if not result:
                            return False
                    elif (data[j] & (1 << i)) != 0:
                        i -= 1
                        if (data[j] & (1 << i)) == 0:
                            j += 1
                            result = check_subsequent_bytes(data, j, 3)
                            j += 3
                            if not result:
                                return False
                        else:
                            return False
    return True
