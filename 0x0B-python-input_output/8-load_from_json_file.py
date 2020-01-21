#!/usr/bin/python3
"""This module defines a function that creates an
Object from a 'JSON file'"""
import json


def load_from_json_file(filename):
    """Returns an Object created from a 'JSON file'"""
    with open(filename, encoding='utf-8', mode='r') as file:
        return json.load(file)
