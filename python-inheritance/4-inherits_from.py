#!/usr/bin/python3
"""Define a function that checks if an object is a strict subclass."""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherited from.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class,
              otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
