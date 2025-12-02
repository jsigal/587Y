# Check object is a subclass of a particular class.

class Animal:
    pass

class Dog(Animal):
    pass

class Puppy(Dog):
    pass

class Cat:
    pass

print(issubclass(Dog, Animal))   # Output: True  (Dog is a subclass of Animal)
print(issubclass(Animal, Dog))   # Output: False (Animal is not a subclass of Dog)
print(issubclass(Cat, Animal))    # Output: False (Cat is not related to Animal)
print(issubclass(Puppy, Animal)) # Output: True (Puppy inherits from Dog, which inherits from Animal)