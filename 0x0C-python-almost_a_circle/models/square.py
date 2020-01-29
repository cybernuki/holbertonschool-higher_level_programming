#!/usr/bin/python3
# Author: Jhonatan Arenas <1164@holbertonschool.com>
# models/square.py
"""This module contains a Square class that
inherits from the Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor method
        Args:
            size (int): is the width of the rectangle
            x (int): is the coordinate x of the rectangle
            y (int): is the coordinate y of the rectangle
            id (int): is the id of the new instance
        Raise:
            ValueError:
                if width or height are less or equals to cero
                if x or y are less than cero
            TypeError:
                if width, height, x, y or id is not int
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        """Returns an string representation of a Rectangle"""
        return "[{}] ({}) {}/{} - {}".format(
            type(self).__name__, self.id,
            self.x, self.y, self.width)
