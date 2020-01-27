#!/usr/bin/python3
""" Class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """constructor """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def integer_validator(self, name, value):
        """
        Validates an integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
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
            rec += (' ' * self.__x + '#' * self.__width + '\n')

        rec = rec.rstrip()
        print(rec)

    def __str__(self):
        """Return class representation """
        txt = '[Rectangle] ({}) {}/{} - {}/{}'
        txt = txt.format(self.id, self.__x, self.__y, self.width, self.height)
        return txt

    def update(self, *args, **kwargs):
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
        return {'x': self.x, 'y':  self.y, 'id': self.id,
                'height': self.height, 'width':  self.width}
