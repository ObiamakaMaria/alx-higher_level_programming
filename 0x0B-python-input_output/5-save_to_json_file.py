#!/usr/bin/python3
"""This script saves the json representation in a text file"""
import json


def save_to_json_file(my_obj, filename):
    """saving json to text file

    Args:
        my_obj: The python object
        filename: The file to write to
    """
    with open(filename, 'w') as myfile:
        json.dump(my_obj, myfile)
