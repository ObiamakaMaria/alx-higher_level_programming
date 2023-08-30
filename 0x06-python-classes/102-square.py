#!/usr/bin/python3

class Square:
    """This script defines a square."""

    def __init__(self, size=0):
        """Initializing  the square with the given size."""
        self.size = size

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Implements the == comparator based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Implements the != comparator based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Implements the < comparator based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Implements the <= comparator based on area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Implements the > comparator based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Implements the >= comparator based on area."""
        return self.area() >= other.area()
