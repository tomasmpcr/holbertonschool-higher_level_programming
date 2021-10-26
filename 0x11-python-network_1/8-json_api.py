#!/usr/bin/python3
"""ASASDSDFGSDF JSDIFJDS IFJDSFDSF"""

import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) == 2:
        ar1 = argv[1]
    else:
        ar1 = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': ar1})
    try:
        dirrct = r.json()
        id = dirrct.get('id')
        name = dirrct.get('name')
        if len(dirrct) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(dirrct.get('id'), dirrct.get('name')))
    except:
        print("Not a valid JSON")
