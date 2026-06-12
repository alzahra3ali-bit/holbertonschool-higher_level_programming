cat << 'EOF' > 0-add_integer.py
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
    
    # التحقق من حالات الـ Float Overflow (inf و NaN)
    if a != a or b != b:  # للتحقق من NaN
        raise TypeError("a must be an integer" if a != a else "b must be an integer")
    if a in [float('inf'), float('-inf')]:
        raise TypeError("a must be an integer")
    if b in [float('inf'), float('-inf')]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
EOF
