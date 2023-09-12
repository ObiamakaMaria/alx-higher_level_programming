#!/usr/bin/python3
"""This script loads python from json file string"""
import json


def load_from_json_file(filename):
    """Loading  py data structure from file string

    Args:
        filename: The file name

    Returns:
        The python data structure
    """
    with open(filename, 'r') as myfile:
        return (json.load(myfile))
