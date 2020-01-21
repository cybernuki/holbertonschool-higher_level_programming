#!/usr/bin/python3
"""
This module defines a function that reads n lines
of a text file
"""


def read_lines(filename="", nb_lines=0):
    """Reads n lines of a text file"""
    with open(filename, encoding='utf-8', mode='r') as file:
        size = sum(1 for line in file)
        file.seek(0)
        if nb_lines <= 0 or nb_lines >= size:
            print(file.read(), end='')
        else:
            for i in range(nb_lines):
                print(file.readline(), end='')
