#!/usr/bin/python3
class Rectangle:
    '''Class that define a rectangle'''
    def __init__(self, width=0, height=0):
        """Init method
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter for width"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter for height"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
