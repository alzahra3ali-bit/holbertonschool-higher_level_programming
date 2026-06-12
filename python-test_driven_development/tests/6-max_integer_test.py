#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase class for the max_integer function."""

    def test_regular_list(self):
        """Test with a regular ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_one_element_list(self):
        """Test with a list containing only one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_all_negative_numbers(self):
        """Test with a list of all negative integers."""
        self.assertEqual(max_integer([-1, -5, -3, -9]), -1)

    def test_mixed_numbers(self):
        """Test with a list containing both positive and negative integers."""
        self.assertEqual(max_integer([-10, 5, -3, 0, 9]), 9)

    def test_max_at_the_beginning(self):
        """Test with a list where the maximum value is at the beginning."""
        self.assertEqual(max_integer([100, 50, 20, 10]), 100)

    def test_floats_list(self):
        """Test with a list of floats."""
        self.assertEqual(max_integer([1.53, 6.33, -2.5, 6.34]), 6.34)

    def test_mixed_ints_and_floats(self):
        """Test with a list of both integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 3, 4.2]), 4.2)


if __name__ == '__main__':
    unittest.main()
