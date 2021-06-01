#!/usr/bin/python3
"""
    is_kind_of_class
"""


class BaseGeometry():
    """ is_kind_of_class """

    def area(self):
        """ area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer_validator """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
