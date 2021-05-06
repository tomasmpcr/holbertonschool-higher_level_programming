#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in range(0, len(my_list)):
        if i == search - 1:
            new_list.append(replace)
        else:
            new_list.append(my_list[i])
    return (new_list)
