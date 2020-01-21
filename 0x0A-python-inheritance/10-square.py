#!/usr/bin/python3
"""
Module geometry
"""
Rectangle = __import__('9-rectangle').Rectangle


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

    def area(self):
        """
        Returns the area
        """
        return self.__size ** 2
