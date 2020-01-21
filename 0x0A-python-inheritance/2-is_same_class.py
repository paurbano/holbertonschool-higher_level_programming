#!/usr/bin/python3
"""
Exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    Checks if an instance of the same class
    """
    if type(obj) is a_class:
        return True
    return False
