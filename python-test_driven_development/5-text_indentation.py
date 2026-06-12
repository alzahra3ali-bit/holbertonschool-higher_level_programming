#!/usr/bin/python3
"""
This module provides a function that indents text based on specific characters.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    Ensures there are no spaces at the beginning or end of each printed line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cleaned_text = ""
    for char in text:
        cleaned_text += char
        if char in [".", "?", ":"]:
            cleaned_text += "\n\n"

    lines = cleaned_text.split("\n")
    formatted_lines = []
    
    for line in lines:
        formatted_lines.append(line.strip(" "))

    print("\n".join(formatted_lines), end="")
