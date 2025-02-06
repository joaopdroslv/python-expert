# Duck typing is a way to achieve polymorphism without requiring inheritance.
# An object is considered valid if it has the necessary attributes/methods.
# "If it looks like a duck and quacks like a duck, it must be a duck."
# This allows objects of different types to be treated similarly 
# if they share the same behavior (method in this case).

class Animal:
    """Represents a generic living being."""
    alive = True  # Class attribute, animals are alive by default


class Dog(Animal):
    """Represents a dog, which is an animal."""

    def speak(self):
        """Dog makes a sound."""
        print('Woof!')


class Cat(Animal):
    """Represents a cat, which is an animal."""

    def speak(self):
        """Cat makes a sound."""
        print('Meow!')


class Car:
    """Represents a car, which is NOT an animal but has similar behavior."""

    # Unlike animals, cars are not alive, but we still use 'alive' for demonstration
    alive = False  

    def speak(self):
        """Car makes a sound (horn honking)."""
        print('Honk!')


# List of objects that share the same 'speak' method, demonstrating duck typing
# Duck typing allows these objects (Dog, Cat, Car) to be 
# treated the same, despite not being related by inheritance.
objects = [Dog(), Cat(), Car()]

# Looping through the objects and calling the 'speak' method on each
for obj in objects:
    obj.speak()  # Calls the speak method, regardless of the class
    # Prints the 'alive' attribute, which exists in both Animal and Car classes
    print(f'Alive: {obj.alive}')  
