#!/usr/bin/python3
"""
    Function add new lines of text
    Fun:
        text_indentation
"""


def text_indentation(text):
    """
        Fun add new line
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    text = text.replace(".", ".\n\n")
    text = text.replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")
    ar = text.split("\n\n")
    for i in range(len(ar)):
        print("{}".format(ar[i].strip()), end="")
        if (i != len(ar) - 1):
            print("\n\n", end="")
