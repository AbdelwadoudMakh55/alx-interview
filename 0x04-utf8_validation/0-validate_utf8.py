#!/usr/bin/env python3
"""
Solution for utf-8 validatio problem
"""


def check_subsequent_bytes(data, j, sub):
    i = 0
    while i < sub and j < len(data):
        if not ((data[j] & (1 << 7)) != 0 and (data[j] & (1 << 6)) == 0):
            return False
        i += 1
        j += 1
    if i != sub:
        return False
    return True


def validUTF8(data):
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
                    if not result:
                        return False
                elif (data[j] & (1 << i)) != 0:
                    i -= 1
                    if (data[j] & (1 << i)) == 0:
                        j += 1
                        result = check_subsequent_bytes(data, j, 2)
                        if not result:
                            return False
                    elif (data[j] & (1 << i)) != 0:
                        i -= 1
                        if (data[j] & (1 << i)) == 0:
                            j += 1
                            result = check_subsequent_bytes(data, j, 3)
                            if not result:
                                return False
                        else:
                            return False
    return True
