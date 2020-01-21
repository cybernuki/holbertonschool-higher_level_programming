#!/usr/bin/python3
"""This module Defines a Student class"""


class Student():
    """Class that represents a student"""

    def __init__(self, first_name, last_name, age):
        """Constructor method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of a
        student instance"""
        return self.__dict__
