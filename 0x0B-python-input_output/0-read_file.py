#!/usr/bin/python3
"""This script reads element from the file"""


def read_file(filename=""):
    """Read element to the file

    Args:
        filename: This is the file name
    """
    with open(filename, encoding="utf-8") as myfile:
        line = myfile.readlines()
        for i in line:
            print(i, end='')
