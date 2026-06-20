#!/usr/bin/python3
"""Define a class Rectangle with an instance counter."""


class Rectangle:
    """A class that defines a rectangle and tracks the number of instances."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize the rectangle and increment the instance counter.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation.

        Args:
            value (int): The new width.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation.

        Args:
            value (int): The new height.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the rectangle area.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the rectangle perimeter.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Return a string representation of the rectangle using #.

        Returns:
            str: The rectangle representation, or an empty string if size is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = []
        for i in range(self.__height):
            rect_str.append("#" * self.__width)
        return "\n".join(rect_str)

    def __repr__(self):
        """Return a string representation to recreate the instance via eval().

        Returns:
            str: A string in the format Rectangle(width, height).
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message and decrement the instance counter upon deletion."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
