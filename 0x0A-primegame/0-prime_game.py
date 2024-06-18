#!/usr/bin/python3
"""
Solve the prime game problem
"""


def primes(numbers):
    """Check for prime number inside a list"""
    primes = 0
    for i in range(len(numbers)):
        j = 2
        check = 0
        while j < int(numbers[i]**0.5) + 1:
            if numbers[i] % j == 0:
                check = 1
                break
            j += 1
        if check == 0:
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
        numbers = list(range(2, nums[i] + 1))
        primes_count = primes(numbers)
        if primes_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return 'Maria'
    elif maria_wins == ben_wins:
        return None
    return 'Ben'
