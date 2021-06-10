#!/usr/bin/python3
"""
    Class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Funcion init """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Funcion """
        return("[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.height
        ))

    @property
    def size(self):
        """ Funcion """
        return(self.width)

    @size.setter
    def size(self, value):
        """ Funcion """
        self.width = value
        self.height = value
        return
