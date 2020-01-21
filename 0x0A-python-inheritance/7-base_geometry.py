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
        Returns the area of an descendent object
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

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")
