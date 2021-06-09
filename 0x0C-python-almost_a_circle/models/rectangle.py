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
        self.width = width
        self.heigh = height
        self.x = x
        self.y = y
        super().__init__(id)
        return

    @property
    def width(self):
        """ Funcion """
        return(self.__width)

    @width.setter
    def width(self, value):
        """ Funcion """
        self.value_valid("width", value)
        self.__width = value
        return

    @property
    def heigh(self):
        """ Funcion """
        return(self.__heigh)

    @heigh.setter
    def heigh(self, value):
        """ Funcion """
        self.value_valid("heigh", value)
        self.__heigh = value
        return

    @property
    def x(self):
        """ Funcion """
        return(self.__x)

    @x.setter
    def x(self, value):
        """ Funcion """
        self.value_valid("x", value)
        self.__x = value
        return

    @property
    def y(self):
        """ Funcion """
        return(self.__y)

    @y.setter
    def y(self, value):
        """ Funcion """
        self.value_valid("y", value)
        self.__y = value
        return

    def value_valid(self, name, value):
        """ Funcion """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif (name == "width" or name == "height") and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(name))
        return

    def area(self):
        """ Funcion """
        return (self.__heigh * self.__width)
