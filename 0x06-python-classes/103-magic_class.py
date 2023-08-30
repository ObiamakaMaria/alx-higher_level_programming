#!/usr/bin/python3

"""This script defines  a MagicClass matching a bytecode."""

import math


class MagicClass:
    """This class represent a circle."""

    def __init__(self, radius=0):
        """Initializing  a MagicClass.

        Arg:
            radius ( eitherfloat or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """This will return the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """This will return eturn the circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
