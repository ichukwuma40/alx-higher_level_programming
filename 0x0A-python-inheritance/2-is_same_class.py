#!/usr/bin/python3
"""This defines: a class-checking function."""


def is_same_class(obj, a_class):
    """To check if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If the obj is exactly an instance of a_class - True.
        Otherwise it will be - False.
    """
    if type(obj) == a_class:
        return True
    return False
