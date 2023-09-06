#!/usr/bin/python3
"""This script locks a class against props"""


class LockedClass:
    """Here the locked class
    prevents creaion of another prop
    """

    __slots__ = ["first_name"]
