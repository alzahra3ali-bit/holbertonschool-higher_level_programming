#!/usr/bin/python3
"""Define a class MyList that inherits from the built-in list class."""


class MyList(list):
    """A custom list class that extends the built-in list."""

    def print_sorted(self):
        """Print the elements of the list sorted in ascending order."""
        print(sorted(self))
