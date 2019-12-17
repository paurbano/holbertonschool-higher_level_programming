#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    revlist = my_list.reverse()
    for i in revlist:
        print("{:d}".format(i))
