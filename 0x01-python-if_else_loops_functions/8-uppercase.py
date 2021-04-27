#!/usr/bin/python3
def uppercase(str):
    a = 0
    for i in range(0, len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            a = 32
        else:
            a = 0
        print("{}".format(chr(ord(str[i]) - a)), end="")
    print("")
