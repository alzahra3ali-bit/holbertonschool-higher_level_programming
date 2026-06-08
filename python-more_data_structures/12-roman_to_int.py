#!/usr/bin/python3
""" Module to convert Roman numerals to Integers
"""


def roman_to_int(roman_string):
    """Converts a Roman numeral string into an integer (1 to 3999).
    Returns 0 if the input is invalid or not a string.
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    length = len(roman_string)

    for i in range(length):
        current_val = roman_dict.get(roman_string[i], 0)

        # Split condition cleanly to stay well under 79 characters
        if (i + 1 < length and
                current_val < roman_dict.get(roman_string[i + 1], 0)):
            total -= current_val
        else:
            total += current_val

    return total
