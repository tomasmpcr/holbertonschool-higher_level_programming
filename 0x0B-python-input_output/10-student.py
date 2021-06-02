#!/usr/bin/python3
"""
    Student
"""


class Student():
    """ Class Student """

    first_name = None
    last_name = None
    age = None

    def __init__(self, first_name, last_name, age):
        """ Constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        return

    def to_json(self, attrs=None):
        """ def to_json """
        if attrs is None:
            return(self.__dict__)
        new_obj = {}
        for item in self.__dict__.keys():
            if item in attrs:
                new_obj[item] = self.__dict__[item]
        return(new_obj)
