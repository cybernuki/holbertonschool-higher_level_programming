#!/usr/bin/python3
# 3-is_kind_of_class.py
# Jhonatan Arenas <1164@holbertonschool.com>
"""
Defines a method that evaluates if a object is an instance
of the specified class
"""


def is_kind_of_class(obj, a_class):
    """Evaluate if obj is an instance or subclass instance of a_class"""
    return isinstance(obj, a_class)
