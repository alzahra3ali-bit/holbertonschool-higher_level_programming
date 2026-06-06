#!/usr/bin/python3
def uppercase(str):
    """Prints a string in uppercase followed by a new line."""
    for char in str:
        # Check if the character is lowercase (between 'a' and 'z')
        if 97 <= ord(char) <= 122:
            # Subtract 32 to get the uppercase equivalent
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
