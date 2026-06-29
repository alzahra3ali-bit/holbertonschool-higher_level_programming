#!/usr/bin/python3
"""This module contains a function that reads a text file."""


def read_file(filename=""):
    """Reads a UTF8 text file and prints it to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
