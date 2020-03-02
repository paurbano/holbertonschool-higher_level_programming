#!/usr/bin/python3
""" Module Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that defines a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """__init__ method.
        Args:
            size (int): size of square.
            position (tuple): position of square.
        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """Return class representation """
        i = self.id
        x = self.x
        y = self.y
        w = self.width
        # txt = txt.format(self.id, self.x, self.y, self.width)
        return '[Square] ({}) {}/{} - {}'.format(i, x, y, w)

    @property
    def size(self):
        """ getter size """
        return self.width

    @size.setter
    def size(self, value):
        """ setter size """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ assigns attributes: """
        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            params = ('id', 'size', 'x', 'y')
            index = 0
            for arg in args:
                setattr(self, params[index], arg)
                index += 1

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle"""
        return {'x': self.x, 'y':  self.y, 'id': self.id,
                'size': self.width}
