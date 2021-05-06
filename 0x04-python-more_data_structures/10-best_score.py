#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    key_max = None
    value_max = 0

    for (key, value) in a_dictionary.items():
        if value > value_max:
            key_max = key
            value_max = value

    return (key_max)
