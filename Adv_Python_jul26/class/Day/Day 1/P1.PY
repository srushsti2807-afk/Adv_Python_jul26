# Basic Python Classes and Objects
# Class is a blueprint using which we create objects

class Dog:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def bark(self):
        return f"{self.name} says woof! and it is {self.age} years old."

# Create objects
my_dog = Dog("Jerry", 3)
my_dog2 = Dog("Perry", 5)

# Call methods
print(my_dog.bark())
print(my_dog2.bark())