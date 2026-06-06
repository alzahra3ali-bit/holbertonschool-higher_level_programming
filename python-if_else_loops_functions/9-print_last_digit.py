#!/usr/bin/python3
def print_last_digit(number):
    """Prints and returns the value of the last digit of a number."""
    # Handle negative numbers to get the absolute value of the last digit
    if number < 0:
        last_digit = (-number) % 10
    else:
        last_digit = number % 10
        
    print("{}".format(last_digit), end="")
    return last_digit
