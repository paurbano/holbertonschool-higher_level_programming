#!/usr/bin/python3
""" Module Student  """


class Student:
    """ Student Class """
    def __init__(self, first_name, last_name, age):
        """ Init method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return class in JSON"""
        if not attrs:
            return self.__dict__

        new_list = [k for k in attrs if hasattr(self, k)]
        return {k: getattr(self, k) for k in new_list}
