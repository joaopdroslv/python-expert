class Animal:
    """Base class representing an animal."""

    def __init__(self, name):
        """Initialize the animal with a name."""
        self.name = name

    def eat(self):
        print(f'{self.name} is eating.')

    def sleep(self):
        print(f'{self.name} is sleeping.')


class Prey(Animal):
    """Represents an animal that is prey."""

    def flee(self):
        """Simulate the prey fleeing from a predator."""
        print(f'{self.name} is fleeing.')


class Predator(Animal):
    """Represents an animal that is a predator."""

    def hunt(self):
        """Simulate the predator hunting prey."""
        print(f'{self.name} is hunting.')


class Rabbit(Prey):
    """A Rabbit is a Prey, so it can flee but not hunt."""
    pass


class Hawk(Predator):
    """A Hawk is a Predator, so it can hunt but not flee."""
    pass


class Fish(Prey, Predator):
    """A Fish can be both a Prey and a Predator, so it can hunt and flee."""
    pass


# Creating instances of different animals
rabbit = Rabbit('My rabbit')
hawk = Hawk('My hawk')
fish = Fish('My fish')

# Demonstrating behaviors
print("\nRabbit's behavior:")
rabbit.eat()  # Calls the 'eat' method from Animal
rabbit.sleep()  # Calls the 'sleep' method from Animal
rabbit.flee()  # Calls the 'flee' method from Prey
# rabbit.hunt()  # The rabbit can't hunt; it's only a prey.

print("\nHawk's behavior:")
hawk.eat()  # Calls the 'eat' method from Animal
hawk.sleep()  # Calls the 'sleep' method from Animal
hawk.hunt()  # Calls the 'hunt' method from Predator

print("\nFish's behavior:")
fish.eat()  # Calls the 'eat' method from Animal
fish.sleep()  # Calls the 'sleep' method from Animal
fish.hunt()  # Calls the 'hunt' method from Predator
fish.flee()  # Calls the 'flee' method from Prey
