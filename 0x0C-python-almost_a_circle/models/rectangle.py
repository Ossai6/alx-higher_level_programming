#!/usr/bin/python3
"""Defines a rectangle class."""

from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        Args:
            width: The width of the new Rectangle.
            height: The height of the new Rectangle.
            x: The x coordinate of the new Rectangle.
            y: The y coordinate of the new Rectangle.
            id: The identity of the new Rectangle.
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
        """ gets the width of the Rectangle. """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ gets the height of the Rectangle. """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ gets the x coordinate of the Rectangle. """
        return self.__x

    @x.setter
    def x(self, value):
        """ sets the x coordinate """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ gets the y coordinate of the Rectangle. """
        return self.__y

    @y.setter
    def y(self, value):
        """ sets the y coordinate """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area of a Rectangle instance """
        return self.__width * self.__height

    def display(self):
        """
        This method prints in stdout the Rectangle instance
        with the character #
        """
        print(("#" * self.__width + "\n") * self.__height, end="")

    def __str__(self):
        """ returns the string representation of the rectangle """
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)
