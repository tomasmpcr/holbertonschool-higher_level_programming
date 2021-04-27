#!/usr/bin/python3
for i in range(ord('a'), ord('z')):
    if chr(i) not in "qe":
        print(chr(i), end='')
