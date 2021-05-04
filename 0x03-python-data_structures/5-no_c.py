#!/usr/bin/env python3
def no_c(my_string):
    cpy_string = my_string.translate({ord(i): None for i in 'cC'})
    return (cpy_string)
