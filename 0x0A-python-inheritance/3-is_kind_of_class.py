#!/usr/bin/python3
"""
Object is an instance of or that inherited from a class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is the same class
    """
    if isinstance(obj, a_class):
        return True
    return False
