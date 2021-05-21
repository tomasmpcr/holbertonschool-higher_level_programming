#!/usr/bin/python3
"""
    Print square
    Fun:
        print_square
"""


def print_square(size):
    """
        Fun Print square
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    square = ""
    for i in range(0, size):
        square += "#" * size
        if i != size - 1:
            square += "\n"
    print(square)
