#!/usr/bin/python3
"""This defines a file-writing function."""


def write_file(filename="", text=""):
    """It write a string to a UTF8 text file.

    Args:
       The filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
