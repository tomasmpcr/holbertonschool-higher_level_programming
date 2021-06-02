#!/usr/bin/python3
"""
    save_to_json_file
"""


import json


def save_to_json_file(my_obj, filename):
    """ Function that writes an Object to a text file """
    with open(filename, mode="w+", encoding="utf-8") as f:
        json.dump(my_obj, f)
    return
