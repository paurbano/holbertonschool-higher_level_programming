#!/usr/bin/python3
class Rectangle():
    '''Class that define a rectangle'''
    def __init__(self, width=0, heigth=0):
        """Init method
            @width : width of rectangle
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(heigth) != int:
            raise TypeError("height must be an integer")
        if heigth < 0:
            raise ValueError("height must be >= 0")
        
        self.__heigth = heigth
        self.__width = width

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def heigth(self):
        """Getter for heigth"""
        return self.__heigth

    @heigth.setter
    def heigth(self, value):
        """Setter for heigth"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__heigth = value
