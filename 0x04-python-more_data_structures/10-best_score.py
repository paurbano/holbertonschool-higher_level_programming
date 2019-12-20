#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        val = list(a_dictionary.values())
        ke = list(a_dictionary.keys())
        return ke[v.index(max(val))]
    else:
        return None
