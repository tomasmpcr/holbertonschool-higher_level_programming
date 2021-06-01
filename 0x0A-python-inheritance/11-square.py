#!/usr/bin/python3
"""
    Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class """

    __size = None

    def __init__(self, size):
        """ Constructor """
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """ area """
        return (self.__size * self.__size)

    def __str__(self):
        return("[Square] {:d}/{:d}".format(self.__size, self.__size))
