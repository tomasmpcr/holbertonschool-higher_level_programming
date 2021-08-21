#!/usr/bin/python3
""" Modul general compare """

import urllib.request

if __name__ != "__main__":
    exit

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    status = response.read()
    decode_response = status.decode('utf-8')
    print("Body response:")
    print("\t - type: {}".format(type(status)))
    print("\t - content: {}".format(status))
    print("\t - utf8 content: {}".format(decode_response))
