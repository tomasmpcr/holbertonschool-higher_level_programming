#!/usr/bin/python3
""" Modul general compare """

import sys
import urllib.request

if __name__ == '__main__':
    send = urllib.parse.urlencode({'email': sys.argv[2]})
    send = send.encode('utf-8')
    request = urllib.request.Request(sys.argv[1], send)

    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
