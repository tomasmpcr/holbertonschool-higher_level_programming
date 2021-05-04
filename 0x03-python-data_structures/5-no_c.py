#!/usr/bin/env python3
def no_c(my_string):
    my_list = list(my_string)
    index_remove = []
    for i in range(0, len(my_list)):
        if (my_list[i] == "c" or my_list[i] == "C"):
            index_remove.append(i)

    for i in range(0, len(index_remove)):
        del my_list[index_remove[i]]
    cpy_string = ''.join(my_list)
    return (cpy_string)
