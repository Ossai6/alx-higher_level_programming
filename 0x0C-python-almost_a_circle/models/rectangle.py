#!/usr/bin/python3
"""
Defines a rectugular class
"""
from models.base import Base


class Rectangle(Base):
    """
    This represents a class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the Rectangle."""
        if type(value) == int:
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the Rectangle."""
        if type(value) == int:
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x coordinate of the Rectangle."""
        if type(value) == int:
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """gets the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the y coordinate of the Rectangle."""
        if type(value) == int:
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    def area(self):
        area = self.__width * self.__height
        return area

    def display(self):
        if self.width == 0 or self.height == 0:
            print("")
            return

        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
