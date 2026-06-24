#!/usr/bin/env python3
"""
Module for demonstrating Mixins using SwimMixin, FlyMixin, and Dragon.
"""


class SwimMixin:
    """Mixin that provides swimming behavior."""

    def swim(self):
        """Prints swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying behavior."""

    def fly(self):
        """Prints flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class combining SwimMixin and FlyMixin capabilities."""

    def roar(self):
        """Prints dragon roaring message."""
        print("The dragon roars!")
