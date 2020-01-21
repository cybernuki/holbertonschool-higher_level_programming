#!/usr/bin/python3
"""This module define a function that append a string
To a text file (UTF-8)
"""


def append_write(filename="", text=""):
    """Append a string to a text file (UTF8) and returns
        the number of characters written:
    """
    with open(filename, encoding='utf-8', mode='a') as file:
        return file.write(text)
