#!/usr/bin/python3
"""
    write_file
"""


def write_file(filename="", text=""):
    """ Function that writes a string to a text file (UTF8) """
    with open(filename, mode="w+", encoding="utf-8") as f:
        f.write(text)
    return(len(text))
