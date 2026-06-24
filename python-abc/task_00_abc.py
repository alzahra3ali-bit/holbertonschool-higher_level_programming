#!/usr/bin/env python3
"""
Module for abstract animal classes
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class representing an animal"""

    @abstractmethod
    def sound(self):
        """Abstract method to get the animal's sound"""
        pass


class Dog(Animal):
    """Subclass representing a dog"""

    def sound(self):
        """Returns the sound of a dog"""
        return "Bark"


class Cat(Animal):
    """Subclass representing a cat"""

    def sound(self):
        """Returns the sound of a cat"""
        return "Meow"
