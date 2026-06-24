#!/usr/bin/env python3
"""
Module for CountedIterator class that tracks iteration counts.
"""


class CountedIterator:
    """An iterator wrapper that keeps track of how many items were fetched."""

    def __init__(self, iterable):
        """Initialize the iterator object and the counter."""
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """Return the current value of the counter."""
        return self.counter

    def __next__(self):
        """Fetch the next item and increment the counter."""
        item = next(self.iterator)
        self.counter += 1
        return item
