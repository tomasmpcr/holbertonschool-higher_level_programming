#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_del = []
    for (key, val) in a_dictionary.items():
        if val == value:
            list_del.append(key)
    for i in list_del:
        del a_dictionary[i]
    return (a_dictionary)
