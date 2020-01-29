#!/usr/bin/python3
# Author: Jhonatan Arenas <1164@holbertonschool.com>
# models/base.py
"""This module contains a base class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """This method creates a json string of a instance"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
