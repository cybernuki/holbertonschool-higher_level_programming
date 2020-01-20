#!/usr/bin/python3
# 1-my_list.py
# Jhonatan Arenas <1164@holbertonschool.com>
"""own inheritanced list"""


class MyList(list):
    """Inheritanced list"""

    def print_sorted(self):
        """Prints sorted the list"""
        copy = self[:]
        copy.sort()
        print(copy)
