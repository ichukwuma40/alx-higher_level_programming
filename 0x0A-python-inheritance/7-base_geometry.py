#!/usr/bin/python3
"""This defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """This reprsent base geometry."""

    def area(self):
        """It is not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This validate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.i
        """
        if type(value) != int:
            raise TypeError("{} it must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} it must be greater than 0".format(name))
