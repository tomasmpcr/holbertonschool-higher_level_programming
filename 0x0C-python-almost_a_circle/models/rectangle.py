#!/usr/bin/python3
"""
    Class rectangle
"""
from models.base import Base


class Rectangle(Base):
    """ Class rectangle """

    __width = 1
    __height = 1
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Funcion init """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
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
    def height(self):
        """ Funcion """
        return(self.__height)

    @height.setter
    def height(self, value):
        """ Funcion """
        self.value_valid("height", value)
        self.__height = value
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
        return (self.__height * self.__width)

    def display(self):
        """ Funcion """
        print((("#" * self.__width) + "\n") * self.__height, end="")
        return

    def __str__(self):
        return("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id, self.x, self.y, self.width, self.height))
