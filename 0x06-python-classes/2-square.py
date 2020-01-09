#!/usr/bin/python3
class Square:
    """class Square that defines a square.

    Attributes:
              __size (int): size of side of square
    """
    __size = None

    def __init__(self, size=0):
        """__init__ method.
        Args:
            size (int): size of square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
