#!/usr/bin/python3
"""

"""

import json
from sys import argv
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
file_name = "add_item.json"

if (path.exists(file_name)):
    obj = load_from_json_file(file_name)
else:
    obj = []

for i in range(1, len(argv)):
    obj.append(argv[i])
save_to_json_file(obj, file_name)
