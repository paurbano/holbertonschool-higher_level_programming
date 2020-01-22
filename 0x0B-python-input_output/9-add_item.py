#!/usr/bin/python3
"""Module for task9."""


from sys import argv

save_file = __import__('7-save_to_json_file').save_to_json_file
load_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    my_list = load_file(filename)
except FileNotFoundError:
    my_list = []

for n in range(1, len(argv)):
    my_list.append(argv[n])
save_file(my_list, filename)
