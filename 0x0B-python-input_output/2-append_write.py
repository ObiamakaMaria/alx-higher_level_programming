#!/usr/bin/python3
"""This script appends text to a file"""


def append_write(filename="", text=""):
    """Append text to the file

    Args:
        filename: The filename
        text: What to append

    Returns:
        The number of bytes
    """
    with open(filename, 'a', encoding="utf-8") as myfile:
        return (myfile.write(text))
