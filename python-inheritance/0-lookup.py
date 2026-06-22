#!/usr/bin/python3
"""Define an object attribute and method lookup function."""


def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    return dir(obj)
