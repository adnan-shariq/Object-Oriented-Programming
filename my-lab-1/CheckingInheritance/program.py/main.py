# Checking Inheritance

# Base class
class Animal:
    pass


# Derived classes
class Dog(Animal):
    pass


class Cat(Animal):
    pass


# Creating objects
dog = Dog()
cat = Cat()


# Checking if an object is an instance of a class
print(isinstance(dog, Dog))      # True
print(isinstance(dog, Animal))   # True
print(isinstance(cat, Cat))      # True
print(isinstance(cat, Dog))      # False


# Checking if a class is a subclass of another
print(issubclass(Dog, Animal))   # True
print(issubclass(Cat, Animal))   # True
print(issubclass(Dog, Cat))      # False
