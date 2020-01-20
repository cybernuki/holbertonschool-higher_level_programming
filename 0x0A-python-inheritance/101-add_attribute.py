#!/usr/bin/python3
# 101-add_attribute.py
# Jhonatan Arenas <1164@holbertonschool.com>
"""Try to adds a new attribute to a class"""


def add_attribute(obj, att, value):
    """Try to add a new attribute to a class
    Args:
        obj (any): is the objet target
        att (string): is the name of the attribute
        value (any): is the value of the attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
