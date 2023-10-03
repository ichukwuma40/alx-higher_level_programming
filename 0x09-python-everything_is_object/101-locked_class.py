#!/usr/bin/python3
"""It helps to defines a locked class."""


class LockedClass:
    """
   This help to prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
