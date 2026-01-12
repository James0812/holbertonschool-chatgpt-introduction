#!/usr/bin/python3
import sys

def factorial(n):
    """
    factorial - computes the factorial of a given number using recursion

    Parameters:
        n (int): the number for which the factorial is calculated

    Returns:
        int: the factorial of n
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)

