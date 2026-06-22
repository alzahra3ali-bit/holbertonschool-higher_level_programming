#!/usr/bin/python3
"""Define a function that checks an object's class or inheritance."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of, or inherited from, a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match against.

    Returns:
        bool: True if obj is an instance or inherited from a_class,
              otherwise False.
    """
    return isinstance(obj, a_class)
