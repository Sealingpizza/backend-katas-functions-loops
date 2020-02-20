#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "Noah"


def add(x, y):
    """Add two integers. Handles negative values."""
    return (x + y)


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    product = 0
    if(y >= 0):
        for i in range(0, y):
            product = add(product, x)
        return product
    else:
        for i in range(y, 0):
            product = add(product, x)
        return -product    
    


def power(x, n):
    """Raise x to power n, where n >= 0"""
    powerProduct = 1
    for i in range(0, n):
        powerProduct = multiply(powerProduct, x)
    return powerProduct


def factorial(x):
    """Compute factorial of x, where x > 0"""
    facValue = 1
    for i in range(1, x + 1):
        facValue = multiply(facValue, i)
    return facValue


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    fibList = [0, 1]
    i = 2
    while(len(fibList) < n):
        fibList.append(add(fibList[i-1], fibList[i-2]))
        i = add(i, 1)
    return fibList[n - 1]


if __name__ == '__main__':
    print(add(2, 4))
    print(multiply(6, -8))
    print(power(2, 8))
    print(factorial(4))
    print(fibonacci(8))
