#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """this is a square class."""

    def __init__(self, size=0, position=(0, 0)):
        """A methos that initialize a new square.
        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """A method that gets the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """A method that sets the size of a square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """a methos that get the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """A method that sets the value of a tuple"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """A method that return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """A method that print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
