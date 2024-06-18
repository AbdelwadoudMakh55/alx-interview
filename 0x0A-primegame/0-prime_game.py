#!/usr/bin/python3
"""
Solve the prime game problem
"""


def SieveOfEratosthenes(n):
    """Count number of prime nums up to n"""
    prime = [True for i in range(n+1)]
    p = 2
    primes = 0
    while (p * p <= n):
        if prime[p]:
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    for p in range(2, n+1):
        if prime[p]:
            primes += 1
    return primes


def isWinner(x, nums):
    """Solution function"""
    if x == 0 or len(nums) == 0:
        return None
    if x != len(nums):
        return None
    maria_wins = 0
    ben_wins = 0
    for i in range(x):
        primes_count = SieveOfEratosthenes(nums[i])
        if primes_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return 'Maria'
    return 'Ben'
