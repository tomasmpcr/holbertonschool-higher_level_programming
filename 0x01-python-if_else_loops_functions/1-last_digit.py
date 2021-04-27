#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = 1
r_number = number
if number < 0:
    last_digit = last_digit * -1
    r_number = r_number * -1
last_digit = (r_number % 10) * last_digit
print("Last digit of {:d} is {:d} ".format(number, last_digit), end="")
if last_digit == 0:
    print("and is 0")
elif last_digit < 6:
    print("and is less than 6 and not 0")
else:
    print("and is greater than 5")
