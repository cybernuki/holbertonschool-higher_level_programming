#!/usr/bin/python3
# 4-inherits_from.py
# Jhonatan Arenas <1164@holbertonschool.com>
"""
Defines a method that evaluates if a object is an sub class instance
of the specified class
"""


def inherits_from(obj, a_class):
    """Evaluates if obj is a sub class instance of a_class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
