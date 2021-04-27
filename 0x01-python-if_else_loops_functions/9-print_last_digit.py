#!/usr/bin/python3
def print_last_digit(number):
    n = 0
    if number < 0:
        n = -number % 10
    else:
        n = number % 10
    print("{:d}".format(n), end="")
    return n
