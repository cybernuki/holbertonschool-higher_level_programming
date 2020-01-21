#!/usr/bin/python3
"""This module define a function that write a string
To a text file (UTF-8)
"""
def write_file(filename="", text=""):
    """Write a string to a text file (UTF8) and returns
        the number of characters written:
    """
    with open(filename, encoding='utf-8', mode='w') as file:
        return file.write(text)
