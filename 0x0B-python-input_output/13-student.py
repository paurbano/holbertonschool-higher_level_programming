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
        if attrs is None:
            return self.__dict__

        name_attrs = {}
        for key, val in self.__dict__.items():
            if key in attrs:
                name_attrs[key] = val
        return name_attrs

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
