#!/usr/bin/python3
"""
    Class rectangle
"""
from models.base import Base


class Rectangle(Base):
    """ Class rectangle """

    __width = None
    __height = None
    __x = None
    __y = None

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Funcion init """
        super().__init__(id)
        self.width = width
        self.heigh = height
        self.x = x
        self.y = y
        pass

    @property
    def width(self):
        """ Funcion """
        return(self.__width)

    @width.setter
    def width(self, value):
        """ Funcion """
        self.__width = value
        return

    @property
    def heigh(self):
        """ Funcion """
        return(self.__heigh)

    @heigh.setter
    def heigh(self, value):
        """ Funcion """
        self.__heigh = value
        return

    @property
    def x(self):
        """ Funcion """
        return(self.__x)

    @x.setter
    def x(self, value):
        """ Funcion """
        self.__x = value
        return

    @property
    def y(self):
        """ Funcion """
        return(self.__y)

    @y.setter
    def y(self, value):
        """ Funcion """
        self.__y = value
        return
