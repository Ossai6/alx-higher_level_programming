 #!/usr/bin/python3                                                     """This module contains the class Rectangle"""


class Rectangle:
    """This class represents a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """checks which rectangle area is biggest"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance that is a square w/ h==w==size"""
        return cls(size, size)

    def __del__(self):
        """prints a message when an instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets and return the width to a new value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value
        return self.__width

    @property
    def height(self):
        """returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets and return the width to a new value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self. __height = value
        return self.__height

    def area(self):
        """returns the area of the triangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        result = 2*(self.__width + self.__height)
        return (result)

    def __str__(self):
        """print the rectangle with the character #"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join(str(self.print_symbol) * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
