#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(0, x+1):
        try:
            print(my_list[i], end="")
        except:
            break
    print("")
    return (i)
