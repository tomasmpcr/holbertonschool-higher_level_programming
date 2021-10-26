#!/usr/bin/python3
"""ASASDSDFGSDF JSDIFJDS IFJDSFDSF"""

import urllib.error as error
import urllib.request as req
from sys import argv

if __name__ == "__main__":
    datos = req.Request(argv[1])
    try:
        with req.urlopen(datos) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
