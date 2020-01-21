#!/usr/bin/python3
"""
Module geometry
"""


class BaseGeometry:
    """
    A class geometry
    """
    def area(self):
        """
        Returns the area of a descendent object
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates an integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Rectangle is descendent of BaseGeometry
    """
    def __init__(self, width, height):
        """
        Rectangle init
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
