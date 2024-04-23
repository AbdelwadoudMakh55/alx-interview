#!/usr/bin/python3
"""
Solution file for the minimum operations problem.
"""


def check_prime(n: int) -> bool:
    """ Check if integer is prime """
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True


def minOperations(n: int) -> int:
    """ Count number of minimum operations """
    if n <= 0:
        return 0
    sum_prime_factors = []
    i = 2
    while n != 1:
        if check_prime(i) and n % i == 0:
            n = n // i
            sum_prime_factors.append(i)
        else:
            i += 1

    return sum(sum_prime_factors)
