#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    result = map(lambda x: x * number, my_list)
    print(list(result))
    return (result)
