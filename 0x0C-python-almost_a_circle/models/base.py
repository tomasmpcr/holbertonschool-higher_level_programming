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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Funcion """
        if list_dictionaries is None:
            return("[]")
        return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ Funcion """
        new_list = []
        if list_objs is not None:
            for element in list_objs:
                new_list.append(element.to_dictionary())
        with open("{}.json".format(cls.__name__), "+w") as file:
            file.write(cls.to_json_string(new_list))
        return

    @staticmethod
    def from_json_string(json_string):
        """ Funcion """
        if json_string is None:
            return([])
        return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
    
