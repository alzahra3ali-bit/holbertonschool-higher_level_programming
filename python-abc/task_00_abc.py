import abc from ABCmeta,abstracmethod
class Animal(metaclass=ABCmeta):
    @abstracmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Bark")
class Cat(Animal):
    def sound(self):
        print("Meow")
