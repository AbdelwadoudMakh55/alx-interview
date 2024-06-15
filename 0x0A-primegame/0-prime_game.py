#!/usr/bin/python3
"""
Solve the prime game problem
"""


def primes(numbers):
    """Check for prime number inside a list"""
    primes = 0
    for i in range(1, len(numbers)):
        j = 2
        check = 0
        while j < numbers[i]:
            if numbers[i] % j == 0:
                check = 1
            j += 1
        if check == 0:
            primes += 1
    return primes


def isWinner(x, nums):
    """Solution function"""
    maria_wins = 0
    ben_wins = 0
    for i in range(x):
        numbers = list(range(1, nums[i] + 1))
        primes_count = primes(numbers)
        if primes_count == 0:
            ben_wins += 1
        elif x % primes_count == 1:
            ben_wins += 1
        elif x % primes_count == 0:
            maria_wins += 1
    if maria_wins > ben_wins:
        return 'Maria'
    elif maria_wins == ben_wins:
        return None
    return 'Ben'
