#!/usr/bin/python3
""" Module Rectangle"""
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def integer_validator(self, name, value):
        """
        Validates an integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    @property
    def width(self):
        """ getter width """
        return self.__width

    @width.setter
    def width(self, width):
        """ setter width """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ getter heigth """
        return self.__height

    @height.setter
    def height(self, height):
        """ setter height """
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ getter x """
        return self.__x

    @x.setter
    def x(self, x):
        """ setter x"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ getter y """
        return self.__y

    @y.setter
    def y(self, y):
        """ setter y """
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        Returns the area
        """
        return self.__width * self.__height

    def display(self):
        """ print rectangle"""
        rec = ""
        if self.__width == 0 or self.height == 0:
            return rec

        for y in range(self.__y):
            print()

        for i in range(self.__height):
            print((' ' * self.__x) + ('#' * self.__width))

    def __str__(self):
        """Return class representation """
        txt = '[Rectangle] ({}) {}/{} - {}/{}'
        txt = txt.format(self.id, self.__x, self.__y, self.width, self.height)
        return txt

    def update(self, *args, **kwargs):
        """ Udpdate attributes """
        if args:
            params = ('id', 'width', 'height', 'x', 'y')
            index = 0
            for arg in args:
                setattr(self, params[index], arg)
                index += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        return {'x': self.x, 'y':  self.y, 'id': self.id,
                'height': self.height, 'width':  self.width}
