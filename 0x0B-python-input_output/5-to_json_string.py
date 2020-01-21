#!/usr/bin/python3
"""This module defines a function that returns a JSON
Representation of an object"""
import json


def to_json_string(my_obj):
    """Returns a JSON representation of an object"""
    return json.dumps(my_obj)
