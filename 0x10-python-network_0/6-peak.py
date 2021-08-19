#!/usr/bin/python3
""" Comprobar picos """

def find_peak(list_of_integers):
    if list_of_integers is None or len(list_of_integers) == 0:
        return (None)
    pico = list_of_integers[0]
    for i in range(0, len(list_of_integers)):
        if i != 0 and list_of_integers[i] > list_of_integers[i-1]:
            if i < len(list_of_integers) and list_of_integers[i] > list_of_integers[i+1]:
                pico = list_of_integers[i]
    return(pico)
