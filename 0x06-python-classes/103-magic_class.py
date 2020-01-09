#!/usr/bin/python3
"""Magic class"""
import math


class MagicClass:
    """A Circle class."""

    def __init__(self, radius=0):
        """Init class."""
        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Return the area of the MagicClass."""
        return self.__radius ** 2 * math.pi

    def circunference(self):
        """Return The circumference of the MagicClass."""
        return 2 * math.pi * self.__radius
