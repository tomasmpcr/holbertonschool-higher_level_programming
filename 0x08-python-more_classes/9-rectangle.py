#!/usr/bin/python3
"""
    In this method a class is defined
"""


class Rectangle:
    """
        In this class several functions are defined
    """

    __width = 0
    __height = 0
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ This is the construct of the Rectangle class """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1
        return

    "======================================================================="

    def area(self):
        """ In this function the area of the rectangle is calculated """
        return (self.__width * self.__height)

    "======================================================================="

    def perimeter(self):
        """ In this function the perimeter of the rectangle is calculated """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width + self.__height) * 2)

    "======================================================================="

    @property
    def width(self):
        """ This is the prototype of get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ This is the prototype of setter width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    "======================================================================="

    @property
    def height(self):
        """ This is the prototype of get height """
        return self.__height

    @height.setter
    def height(self, value):
        """ This is the prototype of setter height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    "======================================================================="

    def __str__(self):
        """ In this function, create a string containing the rectangle """
        rec = ""
        if self.__width == 0 or self.__height == 0:
            return (rec)
        for i in range(self.__height):
            rec += (str(self.print_symbol) * self.__width)
            if i != self.__height - 1:
                rec += "\n"
        return (rec)

    "======================================================================="

    def __repr__(self):
        """
            In this function, create a string
            containing the description of the rectangle
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    "======================================================================="

    def __del__(self):
        """ This function runs when this class is removed """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
        return

    "======================================================================="

    def bigger_or_equal(rect_1, rect_2):
        """ This function runs when this class is removed """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    "======================================================================="

    @classmethod
    def square(cls, size=0):
        """ This function runs when this class is removed """
        ram = Rectangle(size, size)
        return (ram)
