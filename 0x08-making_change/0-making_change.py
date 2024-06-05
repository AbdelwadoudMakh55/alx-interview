#!/usr/bin/python3
"""
Implement a solution for making change problem
"""


def makeChange(coins, total):
    """Function for the solution"""
    if total <= 0:
        return -1
    coins_count = 0
    sum = 0
    while sum < total and len(coins) > 0:
        if max(coins) + sum < total:
            sum += max(coins)
            coins_count += 1
        elif max(coins) + sum == total:
            sum += max(coins)
            coins_count += 1
        else:
            if len(coins) > 0:
                coins.pop(coins.index(max(coins)))
    if sum != total:
        return -1
    return coins_count
