#!/usr/bin/python3
"""
 reads n lines of a text file (UTF8) and prints it to stdout:
"""
number_of_lines = __import__('1-number_of_lines').number_of_lines


def read_lines(filename="", nb_lines=0):
    num_lines = number_of_lines(filename)
    """ reads n lines of a text file (UTF8) and prints it to stdout """
    with open(filename, 'r') as f:
        if nb_lines <= 0 or nb_lines >= num_lines:
            print(f.read(), end="")
        else:
            lines = f.readlines()
            for numline in range(nb_lines):
                print(lines[numline], end="")
