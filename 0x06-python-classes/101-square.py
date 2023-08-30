#!/usr/bin/python3
"""This Script defines a custom Square class."""


class Square:
    """Represent a square object with size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square instance.

        Args:
            size (int): The size of the square.
            position (int, int): The position of the square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The position to be set.
        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square using '#' characters.

        The square is positioned based on the position attribute.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return a string representation of the square."""
        result = ""
        if self.__size == 0:
            result += "\n"
        else:
            for _ in range(self.__position[1]):
                result += "\n"
            for _ in range(self.__size):
                result += " " * self.__position[0] + "#" * self.__size
                result += "\n"
        return result

    def __format__(self, format_spec):
        """Format the square using specified format."""
        return str(self).__format__(format_spec)
