#!/usr/bin/env python3
def no_c(my_string):
    str_new = ""
    for i in range(0, len(my_string)):
        if my_string[i] != "c" and my_string[i] != "C":
            str_new += my_string[i]
    return (str_new)
