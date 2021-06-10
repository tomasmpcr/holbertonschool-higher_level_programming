#!/usr/bin/python3
"""
    Class base
"""


import json


class Base():
    """ Class base """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Funcion init """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ Funcion """
        if list_dictionaries is None:
            return("[]")
        return(json.dumps(list_dictionaries))
