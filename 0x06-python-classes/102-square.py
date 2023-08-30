#!/usr/bin/python3
"""This script defines a custom Square class."""


class Square:
    """Represent a square object with size attribute and comparison methods."""

    def __init__(self, size=0):
        """Initialize a new square instance.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size to be set.
        Raises:
            TypeError: If size is not a number (integer or float).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """Compare if two squares are equal in terms of area.

        Args:
            other (Square): The other square to compare with.
        Returns:
            bool: True if areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare if two squares are not equal in terms of area.

        Args:
            other (Square): The other square to compare with.
        Returns:
            bool: True if areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """Compare if the area of this square is less than the area of another square.

        Args:
            other (Square): The other square to compare with.
        Returns:
            bool: True if this square's area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if the area of this square is less than or equal to the area of another square.

        Args:
            other (Square): The other square to compare with.
        Returns:
            bool: True if this square's area is less than or equal, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compare if the area of this square is greater than the area of another square.

        Args:
            other (Square): The other square to compare with.
        Returns:
            bool: True if this square's area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare if the area of this square is greater than or equal to the area of another square.

        Args:
            other (Square): The other square to compare with.
        Returns:
            bool: True if this square's area is greater than or equal, False otherwise.
        """
        return self.area() >= other.area()
