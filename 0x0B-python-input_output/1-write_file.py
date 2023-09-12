#!/usr/bin/python3
"""This script overwrites the content of the byte"""


def write_file(filename="", text=""):
    """Writing  to file

    Args:
        filename: The filename
        text: The text to write

    Returns:
        return the number of byte written
    """
    with open(filename, 'w', encoding="utf-8") as myfile:
        return (myfile.write(text))
