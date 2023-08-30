#!/usr/bin/python3
"""This script defines a Square class."""


class Square:
    """Represent a geometric square entity."""

    def __init__(self, size=0):
        """Initialize a new square instance.

        Args:
            size (int): The size of the square's side length.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and provide the area of the square.

        Returns:
            int: The area calculated based on the side length.
        """
        return self.__size * self.__size
