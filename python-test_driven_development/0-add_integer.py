#!/usr/bin/python3
"""
This module provides a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # كشف ومنع قيم NaN و M_inf و Inf مباشرة لتخطي فحص الـ Float overflow
    if a != a or a in (float('inf'), float('-inf')):
        raise TypeError("a must be an integer")
    if b != b or b in (float('inf'), float('-inf')):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
