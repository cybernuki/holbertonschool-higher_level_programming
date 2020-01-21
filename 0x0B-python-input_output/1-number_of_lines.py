#!/usr/bin/python3
"""Defines a function that returns the number of lines of a text file"""


def number_of_lines(filename=""):
    """Returns the number of lines of a text file"""
    n_lines = 0
    with open(filename, encoding='utf-8', mode='r') as file:
        for lines in file:
            n_lines += 1
    return n_lines
