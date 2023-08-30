#!/usr/bin/python3
"""This define a Square class."""


class Square:
    """Represent a square object with size and methods."""

    def __init__(self, size):
        """Initialize a new square instance.

        Args:
            size (int): The size of the square.
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
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square using '#' characters."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            [print("#", end="") for _ in range(self.__size)]
            print()
