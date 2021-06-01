#!/usr/bin/python3
"""
    MyInt
"""


class MyInt(int):
    """ Class """

    def __eq__(self, num):
        """ eq """
        return(super().__ne__(num))

    def __ne__(self, num):
        """ ne """
        return(super().__eq__(num))
