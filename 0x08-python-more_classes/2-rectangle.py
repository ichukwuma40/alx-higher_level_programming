A#!/usr/bin/python3
"""It defines a Rectangle class."""


class Rectangle:
    """the represent a rectangle."""

    def __init__(self, width=0, height=0):
        """the initialize a new Rectangle.

        Args:
            width (int): this the width of the new rectangle.
            height (int): this the height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """to get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("the width must be an integer")
        if value < 0:
            raise ValueError("the width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """the get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("the height must be an integer")
        if value < 0:
            raise ValueError("The height must be >= 0")
        self.__height = value

    def area(self):
        """This return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """It return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

