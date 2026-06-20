#!/usr/bin/python3
"""Define a class Square with size and position attributes."""


class Square:
    """A class that defines a square with a position and printing method."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square.

        Args:
            size (int): The size of the square's side. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square.

        Returns:
            tuple: The position as a tuple of two integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character taking position into account.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        # Print the empty lines (vertical space from top)
        for _ in range(self.__position[1]):
            print("")

        # Print the square with horizontal spaces from left
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
