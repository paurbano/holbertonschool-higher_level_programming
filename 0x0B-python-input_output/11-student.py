#!/usr/bin/python3
""" Module Student  """


class Student:
    """ Student Class """
    def __init__(self, first_name, last_name, age):
        """ Init method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ return class dic in JSON"""
        return self.__dict__
