# Inheritance allows a class to inherit attributes and methods
# from another class, promoting code reusability and extensibility.

class Animal:
    """Base class for all animals."""
    
    def __init__(self, name):
        """Initialize the animal with a name and a default 'is_alive' status."""
        self.name = name
        self.is_alive = True

    def eat(self):
        """Simulate the animal eating."""
        print(f'{self.name} is eating.')

    def sleep(self):
        """Simulate the animal sleeping."""
        print(f'{self.name} is asleep.')


class Dog(Animal):
    """Dog class inheriting from Animal."""
    
    def speak(self):
        """Simulate the dog barking."""
        print('Woof!')


class Cat(Animal):
    """Cat class inheriting from Animal."""
    
    def speak(self):
        """Simulate the cat meowing."""
        print('Meow!')


# Creating instances of Dog and Cat
dog = Dog('Scooby')
cat = Cat('Garfield')

# Demonstrating inherited and unique behaviors
print(f'Dog name: {dog.name}')  # Accesses inherited 'name' attribute from Animal
print(f'Is it alive? {dog.is_alive}')  # Accesses inherited 'is_alive' attribute from Animal
dog.speak()  # Calls Dog's own 'speak' method
dog.eat()  # Calls inherited 'eat' method from Animal
dog.sleep()  # Calls inherited 'sleep' method from Animal

print(f'Cat name: {cat.name}')  # Accesses inherited 'name' attribute from Animal
print(f'Is it alive? {cat.is_alive}')  # Accesses inherited 'is_alive' attribute from Animal
cat.speak()  # Calls Cat's own 'speak' method
cat.eat()  # Calls inherited 'eat' method from Animal
cat.sleep()  # Calls inherited 'sleep' method from Animal
