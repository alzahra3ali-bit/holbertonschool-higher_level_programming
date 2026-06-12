#!/usr/bin/python3
"""Module containing add_integer function."""


def add_integer(a, b=98):
    """Add two integers."""
    for value, name in ((a, "a"), (b, "b")):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be an integer")

        if isinstance(value, float):
            if value == float("inf") or value == float("-inf"):
                raise TypeError(f"{name} must be an integer")

    return int(a) + int(b)
