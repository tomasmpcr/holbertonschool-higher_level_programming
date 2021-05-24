#!/usr/bin/python3
"""
    In this method a class is defined
"""


class Rectangle:
    """
        In this class several functions are defined
    """

    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        """ This is the construct of the Rectangle class """
        self.height = height
        self.width = width
        return

    "======================================================================="

    @property
    def width(self):
        """ This is the prototype of get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ This is the prototype of setter width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    "======================================================================="

    @property
    def height(self):
        """ This is the prototype of get height """
        return self.__height

    @height.setter
    def height(self, value):
        """ This is the prototype of setter height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
