#!/usr/bin/python3
# 8-rectagle.py
# Jhonatan Arenas <1164@holbertonschool.com>
"""
Defines a Rectangle class that inherits by Base_Geometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
