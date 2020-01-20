#!/usr/bin/python3
# 2-is_same_class.py
# Jhonatan Arenas <1164@holbertonschool.com>
"""
Defines a method that evaluates if a object is an instance
of the specified class
"""


def is_same_class(obj, a_class):
    """Evaluate if the given obj is an ''exactly''
    instance of the given class
    """
    return type(obj) is a_class
