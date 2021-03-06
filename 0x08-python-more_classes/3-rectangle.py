#!/usr/bin/python3
class Rectangle:
    '''Class that define a rectangle'''
    def __init__(self, width=0, height=0):
        """Init method"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for wigth"""
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
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width*2) + (self.__height*2)

    def __str__(self):
        """ print() __str__ method """
        rec = ""
        if self.__width == 0 or self.height == 0:
            return rec

        for i in range(self.__height):
            rec += ("#" * self.__width + '\n')
        rec = rec.rstrip()
        return rec
