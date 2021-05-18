#!/usr/bin/python3
"""In this module you will find a class
"Square" at the moment it does nothing"""


class Square:
    """In this class we save a data"""
    __size = 0

    def __init__(self, size=0):
        """This is the constructor of the class"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        return
