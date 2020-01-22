#!/usr/bin/python3
"""This module defines a function that calculates
The pascal's triangle"""

def pascal_triangle(n):
    """Returns a matrix with the nth level of the
    pascal's triangle"""
    if type(n) is not int:
        raise TypeError("n must be an integer")
    if n <= 0:
        return []

    matrix = [[1]]
    if n == 1:
        return matrix
    for i in range (1, n):
        matrix.append([])
        prev, next = -1 , 0
        while next <= i:
            if prev == -1 or next == i:
                matrix[i].append(1)
            else:
                matrix[i].append(matrix[i - 1][prev] + matrix[i - 1][next])
            prev += 1
            next += 1
    return matrix