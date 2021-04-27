#!/usr/bin/python3
import random
number = str(random.randint(-10000, 10000))
last_digit = number[-1:]
if number[0] == "-" and last_digit != "0":
    last_digit = "-" + last_digit
print("Last digit of {} is {} ".format(number, last_digit), end="")
if last_digit == "0":
    print("and is 0")
elif last_digit < "6":
    print("and is less than 6 and not 0")
else:
    print("and is greater than 5")
