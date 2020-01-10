#!/usr/bin/python3
class Square:
    """class Square that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """__init__ method.
        Args:
            size (int): size of square.
            position (tuple): position of square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        msg = "position must be a tuple of 2 positive integers"
        if (type(value) != tuple or len(value) != 2):
            raise TypeError(msg)

        for item in value:
            if type(item) != int or item < 0:
                raise TypeError(msg)

        self.__position = value

    def area(self):
        """area return current square area"""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character #"""
        size = self.__size
        position = self.__position

        if self.size == 0:
            print()
            return

        print("\n" * position[1], end="")

        for i in range(size):
            """here the _ """
            print(" " * position[0], end="")
            print("#" * size)
