#!/usr/bin/python3
"""This defines a class MyInt that inherits from int."""


class MyInt(int):
    """The invert int operators == and !=."""

    def __eq__(self, value):
        """The override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """The override != operator with == behavior."""
        return self.real == value
