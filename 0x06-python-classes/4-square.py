#!/usr/bin/python3
class Square:
    """class Square that defines a square."""
    def __init__(self, size=0):
        """__init__ method.
        Args:
            size (int): size of square
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """area return current square area"""
        return self.__size * self.__size
