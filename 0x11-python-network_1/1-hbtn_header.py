#!/usr/bin/python3
""" Modul general compare """

import sys
import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        x_request = response.getheader('X-Request-Id')

    print(x_request)
