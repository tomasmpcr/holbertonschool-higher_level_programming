#!/usr/bin/python3
"""ASASDSDFGSDF JSDIFJDS IFJDSFDSF"""

import requests
from sys import argv

if __name__ == '__main__':
    res = requests.post(argv[1], data={'email': argv[2]})
    print(res.text)
