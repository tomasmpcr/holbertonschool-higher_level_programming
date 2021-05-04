#!/usr/bin/python3
def max_integer(my_list=[]):
    max_num = None
    for i in my_list:
        if max_num < i:
            max_num = i
    return max_num
