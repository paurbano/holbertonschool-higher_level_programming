#!/usr/bin/python3
""" Module print a file"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout: """
    with open(filename) as f:
        for line in f:
            print(line, end="")
    f.closed
