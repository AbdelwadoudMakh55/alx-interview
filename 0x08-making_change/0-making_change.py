#!/usr/bin/python3
"""
Implement a solution for making change problem
"""


def makeChange(coins, total):
    """Function for the solution"""
    coins.sort()
    dp = [total + 1] * (total + 1)
    dp[0] = 0
    for i in range(1, total + 1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], 1 + dp[i - c])
    return dp[total] if dp[total] != total + 1 else -1
