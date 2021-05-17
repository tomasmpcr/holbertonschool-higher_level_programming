#!/usr/bin/python3
from typing import ValuesView


def safe_print_list_integers(my_list=[], x=0):
    imp = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            imp = imp + 1
        except TypeError:
            continue
        except ValueError:
            continue
    print("")
    return (imp)
