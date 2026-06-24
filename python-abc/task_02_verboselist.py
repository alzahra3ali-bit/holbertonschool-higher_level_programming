#!/usr/bin/env python3
"""
Module for VerboseList class that extends the built-in list.
"""


class VerboseList(list):
    """A list subclass that prints notifications when modified."""

    def append(self, item):
        """Append an item and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list and print a notification with the count."""
        initial_length = len(self)
        super().extend(iterable)
        items_added = len(self) - initial_length
        print(f"Extended the list with [{items_added}] items.")

    def remove(self, item):
        """Remove an item and print a notification before removing."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item from the given index and print a notification."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
