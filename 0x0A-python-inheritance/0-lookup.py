#!/usr/bin/python3
# 0-lookup.py
# Jhonatan Arenas <1164@holbertonschool.com>
"""Defines an object attribute lookup function"""


def lookup(obj):
    """returns a list object with all atributes an methods
        of the given object.
    """
    return dir(obj)
