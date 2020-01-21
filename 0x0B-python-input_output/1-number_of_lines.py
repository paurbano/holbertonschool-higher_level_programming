#!/usr/bin/python3
""" Module get number of lines"""


def number_of_lines(filename=""):
    """return number of lines """
    cont = 0
    with open(filename) as f:
        for line in f:
            cont += 1
    f.close
    return cont
