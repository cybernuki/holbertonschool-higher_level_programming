#!/usr/bin/python3
"""This module Defines a Student class"""


class Student():
    """Class that represents a student"""

    def __init__(self, first_name, last_name, age):
        """Constructor method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of a
        student instance.
        If attrs is a list of string, only attributes names
        contained in this list are retrieved.
        Otherwise, all attributes are retrieved.
        """
        if type(attrs) is list and all(type(val) == str for val in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
