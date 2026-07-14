#!/usr/bin/python3
"""Module to write a string to a text file and return character count."""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8) and return character count."""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
        