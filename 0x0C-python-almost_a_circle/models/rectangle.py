#!/usr/bin/python3
# Author: Jhonatan Arenas <1164@holbertonschool.com>
# models/rectangle.py
from models.base import Base
"""This module contains a Rectangle class that
inherits from the Base class"""


class Rectangle(Base):
    """A class that represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor method
        
        Args:
            width (int): is the width of the rectangle
            height (int): is the height of the rectangle
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
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        self.__y = y
