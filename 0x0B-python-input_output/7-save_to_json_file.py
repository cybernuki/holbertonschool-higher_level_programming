#!/usr/bin/python3
"""This module defines a function that writes an Object to a 
text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation
    """
    with open(filename, encoding='utf-8', mode='w') as file:
        json.dump(my_obj, file)
