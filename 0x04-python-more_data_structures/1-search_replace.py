#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for n, i in enumerate(my_list):
        if i == search:
            my_list[n] = replace
    return my_list
