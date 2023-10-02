#!/usr/bin/python3
"""This defines a Rectangle class."""


class Rectangle:
    """It represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Thw initialize a new Rectangle.

        Args:
            width (int): This the width of the new rectangle.
            height (int): This is the height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """To get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("The width must be an integer")
        if value < 0:
            raise ValueError("The width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """To get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("The height must be an integer")
        if value < 0:
            raise ValueError("The height must be >= 0")
        self.__height = value

