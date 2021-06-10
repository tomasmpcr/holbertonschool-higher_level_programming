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

    def update(self, *args, **kwargs):
        """ Funcion """
        switcher = {
            1:
                lambda value: [None for self.id in [value]],
            "id":
                lambda value: [None for self.id in [value]],
            2:
                lambda value:
                    [[None for self.width in [value]],
                        [None for self.height in [value]]],
            "size":
                lambda value:
                    [[None for self.width in [value]],
                        [None for self.height in [value]]],
            3:
                lambda value: [None for self.x in [value]],
            "x":
                lambda value: [None for self.x in [value]],
            4:
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
