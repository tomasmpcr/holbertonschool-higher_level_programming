#!/usr/bin/python3
"""
    append_write
"""


def append_write(filename="", text=""):
    """ Function that appends a string at the end of a text file (UTF8 """
    with open(filename, mode="a+", encoding="utf-8") as f:
        f.write(text)
    return(len(text))
