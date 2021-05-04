#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    n01 = 0
    n02 = 0
    n11 = 0
    n12 = 0
    len_1 = len(tuple_a)
    len_2 = len(tuple_b)
    if len_1 >= 1:
        n01 = tuple_a[0]
    if len_1 >= 2:
        n02 = tuple_a[1]
    if len_2 >= 1:
        n11 = tuple_b[0]
    if len_2 >= 2:
        n12 = tuple_b[1]
    r0 = n01 + n11
    r1 = n02 + n12
    return ((r0, r1))
