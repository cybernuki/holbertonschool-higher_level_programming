#!/usr/bin/python3
# Author: Jhonatan Arenas <1164@holbertonschool.com>
# models/rectangle.py
"""This module contains a Rectangle class that
inherits from the Base class"""
from models.base import Base


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

    def area(self):
        return self.__width * self.__height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def display(self):
        """prints the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        print("\n" * self.y, end="")
        for i in range(self.width):
            print(" " * self.x, end="")
            print("#" * self.height)

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(
            type(self).__name__, self.id,
            self.x, self.y, self.width, self.height)
