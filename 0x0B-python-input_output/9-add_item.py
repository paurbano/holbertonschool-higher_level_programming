#!/usr/bin/python3
"""Load, add, save """
from sys import argv

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


filename = "add_item.json"
try:
    lista = load_from_json_file(filename)
except Exception:
    lista = []

for n in range(len(argv)):
    if n != 0:
        lista.append(argv[n])

save_to_json_file(lista, filename)
