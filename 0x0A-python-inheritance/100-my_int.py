#!/usr/bin/python3
# 100-my_int.py
# Jhonatan Arenas <1164@holbertonschool.com>
"""
Defines a MyInt class that inherits by Int
But has == and != operators inverted
"""


class MyInt(int):
    """Class that has == and != operators inverted
        Also, it inheritance by int
    """

    def __eq__(self, other):
        """ compares if this instances is != of other instance"""
        return super().__ne__(other)

    def __ne__(self, other):
        """ compares if this instances is == of other instance"""
        return super().__eq__(other)
