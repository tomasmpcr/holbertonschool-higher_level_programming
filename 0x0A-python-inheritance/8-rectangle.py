#!/usr/bin/python3
"""
    Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ is_kind_of_class """

    __width = None
    __height = None

    def __init__(self, width, height):
        """ Constructor """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
