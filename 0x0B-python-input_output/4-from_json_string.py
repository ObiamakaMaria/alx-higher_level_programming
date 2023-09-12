#!/usr/bin/python3
"""This is an object (Python data structure) represented by a JSON string"""
import json


def from_json_string(my_str):
    """Converting from json string to python data structure

    Args:
        my_str: The json string

    Returns:
        The python data structure
    """
    return (json.loads(my_str))
