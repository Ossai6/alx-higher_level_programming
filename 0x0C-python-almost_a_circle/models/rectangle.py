#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    def _init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) == int:
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) == int:
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) == int:
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be > 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) == int:
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be > 0")
        else:
            raise TypeError("y must be an integer")
