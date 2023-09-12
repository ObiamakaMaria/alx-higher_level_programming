#!/usr/bin/python3
"""This script converts class to json"""


def class_to_json(obj):
    """class to json

    Args:
        obj: Instance of the class
    """
    return (obj.__dict__)
