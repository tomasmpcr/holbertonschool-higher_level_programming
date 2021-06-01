#!/usr/bin/python3
"""
    is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """ is_kind_of_class """
    return(isinstance(obj, a_class) or issubclass(type(obj), a_class))
