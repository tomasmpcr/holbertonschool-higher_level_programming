#!/usr/bin/python3
"""In this module you will find a class
"Square" at the moment it does nothing"""


class Square:
    """In this class we save a data"""
    __size = 0

    def __init__(self, size=0):
        """This is the constructor of the class"""
        self.size = size

    def area(self):
        """This function return area"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """This property get size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """This property set size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """This function print square"""
        if (self.__size == 0):
            print()
            return
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()
