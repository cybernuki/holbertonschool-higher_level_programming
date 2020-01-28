#!/usr/bin/python3
# Author: Jhonatan Arenas <1164@holbertonschool.com>
# models/base.py
"""This module contains a base class"""


class Base:
    """A base class for the other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
