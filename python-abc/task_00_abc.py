from abc import ABCmeta,abstracmethod
class Animal(ABC):
    @abstracmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return "Bark"
class Cat(Animal):
    def sound(self):
        return "Meow"
