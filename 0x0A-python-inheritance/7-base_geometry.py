#!/usr/bin/python3
# 7-base_geometry.py
# Jhonatan Arenas <1164@holbertonschool.com>
"""
Defines a BaseGeometry class
"""


class BaseGeometry():
    """A Class that represent a geometry form"""
    def area(self):
        """Returns the area of this Rectangle"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Evaluate if the given value is an integer or greater than 0
        Args:
            name (string): is the name associated to the value
            value (int): is an integer value
        Returns:
            (bool) - True if value is instance of int, False in otherwise
        Raise:
            TypeError - if value is not a instance of int class
            ValueError - if value is less or equals to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
