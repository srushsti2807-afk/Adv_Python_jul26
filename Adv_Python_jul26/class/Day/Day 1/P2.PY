# Parent class / Base class

class Animal:
    def __init__(self, name):
        self.name = name

    def makeSound(self):
        return "Some sound"


# Child class / Derived class

class Cat(Animal):
    def makeSound(self):
        return f"{self.name} says meow"


# Child class / Derived class

class Cow(Animal):
    def makeSound(self):
        return f"{self.name} says moo"


# Create objects

cat = Cat("Tom")
cow = Cow("Jerry")

# Call methods

print(cat.makeSound())
print(cow.makeSound())
