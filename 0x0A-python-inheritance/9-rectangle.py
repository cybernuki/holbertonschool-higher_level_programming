#!/usr/bin/python3
# 9-rectagle.py
# Jhonatan Arenas <1164@holbertonschool.com>
"""
Defines a Rectangle class that inherits by Base_Geometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Class that represents a Rectangle"""
    def __init__(self, width, height):
        """Constructor method
        Args:
            size (int): is the sizes of the square
        Raise:
            TypeError - if size is not an int
            ValueError - if size is less or equals to zero
        """
        super
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of this Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a informal representation of Rectangle Class"""
        return "[{}] {}/{}".format("Rectangle", self.__width, self.__height)
