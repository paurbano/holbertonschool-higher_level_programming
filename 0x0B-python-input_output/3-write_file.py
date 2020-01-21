#!/usr/bin/python3
""" module  writes a string to a text file (UTF8)
and returns the number of characters written:
"""


def write_file(filename="", text=""):
    with open(filename, 'w+') as f:
        num_chac = f.write(text)

    return num_chac
