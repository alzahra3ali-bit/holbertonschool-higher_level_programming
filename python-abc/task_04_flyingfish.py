#!/usr/bin/env python3
"""
Module for exploring multiple inheritance via Fish, Bird, and FlyingFish.
"""


class Fish:
    """Class representing a fish."""

    def swim(self):
        """Prints swimming behavior of a fish."""
        print("The fish is swimming")

    def habitat(self):
        """Prints habitat of a fish."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""

    def fly(self):
        """Prints flying behavior of a bird."""
        print("The bird is flying")

    def habitat(self):
        """Prints habitat of a bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a flying fish, inheriting from Fish and Bird."""

    def fly(self):
        """Prints flying behavior of a flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Prints swimming behavior of a flying fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Prints habitat of a flying fish."""
        print("The flying fish lives both in water and the sky!")
