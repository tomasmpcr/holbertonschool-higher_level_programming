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

    def to_json(self):
        """ def to_json """
        return(self.__dict__)
