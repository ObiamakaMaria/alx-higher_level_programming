#!/usr/bin/python3
"""This script returns JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """Converting to json strinf

    Args:
        my_obj: The python data structure

    Returns:
        The json object representation
    """
    return (json.dumps(my_obj))
