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
        Returns the area
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
    Rectangle descendent from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Initialization for a Rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        string info
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Returns the area
        """
        return self.__width * self.__height


class Square(Rectangle):
    """
    Square is descendent from Rectangle
    """
    def __init__(self, size):
        """
        Square init
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        string info
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """
        Returns the area
        """
        return self.__size ** 2
