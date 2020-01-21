#!/usr/bin/python3
"""Module that defines a function to open a file"""


def read_file(filename=""):
    """Open an file and prints it to stdout"""
    with open(filename, encoding='utf-8', mode='r') as file:
        for line in file:
            print(line, end="")
