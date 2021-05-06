#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_direct = {}
    for key in sorted(a_dictionary.keys()):
        cont = a_dictionary[key] * 2
        new_direct[key] = cont
    return (new_direct)
