#!/usr/bin/python3
"""
Father class
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
