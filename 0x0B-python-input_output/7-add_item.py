#!/usr/bin/python3
import os.path
import sys
import json

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
the_list = []

if os.path.exists(filename) and os.path.getsize(filename) > 0:
    the_list = load_from_json_file(filename)

if len(sys.argv) > 1:
    for i in sys.argv[:1]:
        the_list.append(i)
save_to_json_file(the_list, filename)
