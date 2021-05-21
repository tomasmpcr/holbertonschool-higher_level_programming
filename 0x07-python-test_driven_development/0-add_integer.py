#!/usr/bin/python3
"""
    Function sum integer
    Fun:
        add_integer
"""


def add_integer(a, b=98):
    """
        Function sum integer
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    else:
        return (int(a + b))
