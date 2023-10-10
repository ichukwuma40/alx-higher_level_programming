#!/usr/bin/python3
"""It defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """This checks if an object is an inherited instance of a class.

    Args:
        obj (any): This is the object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise it will be - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
