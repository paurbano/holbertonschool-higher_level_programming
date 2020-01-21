#!/usr/bin/python3
""" returns the JSON representation of an object (string)"""
import json


def save_to_json_file(my_obj, filename):
    """ write JSON representation of an object to text file"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
