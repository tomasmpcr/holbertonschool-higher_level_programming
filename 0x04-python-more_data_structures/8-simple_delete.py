#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    x = a_dictionary.get(key)
    if x is not None:
        del a_dictionary[key]
    return (a_dictionary)
