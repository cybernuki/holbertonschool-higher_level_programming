#!/usr/bin/python3
# Author: Jhonatan Arenas <1164@holbertonschool.com>
# models/base.py
"""This module contains a base class"""
import json


class Base:
    """A base class for the other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """This method creates a json string of a instance"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write a JSON file to serializate an object"""

        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dict = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dict)
