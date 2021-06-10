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
        print(
                (("\n" * self.y) +
                    ((" " * self.x) +
                        ("#" * self.__width) + "\n") * self.__height), end="")
        return

    def __str__(self):
        """ Funcion """
        return("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height
        ))

    def update(self, *args, **kwargs):
        """ Funcion """
        switcher = {
            1:
                lambda value: [None for self.id in [value]],
            "id":
                lambda value: [None for self.id in [value]],
            2:
                lambda value: [None for self.width in [value]],
            "width":
                lambda value: [None for self.width in [value]],
            3:
                lambda value: [None for self.height in [value]],
            "height":
                lambda value: [None for self.height in [value]],
            4:
                lambda value: [None for self.x in [value]],
            "x":
                lambda value: [None for self.x in [value]],
            5:
                lambda value: [None for self.y in [value]],
            "y":
                lambda value: [None for self.y in [value]]
        }

        if args is not None and len(args) > 0:
            i = 1
            for arg in args:
                func = switcher.get(i, "return")
                if func == "return":
                    return
                func(arg)
                i = i + 1
            return

        for item in kwargs.items():
            func = switcher.get(item[0], "return")
            if func == "return":
                return
            func(item[1])
        return
